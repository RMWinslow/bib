"""Compare processed/read Zotero citation keys with paper filenames, read-only.

Provenance: Created by OpenAI Codex for Robert Winslow's September 2026
bibliography-repo cleanup, in preparation for importing read papers from
Zotero. The task was to find existing repo pages despite changed citation
keys and paper titles, so later imports would not create duplicate pages.
The broad audit supported that initial review; --saved-keys is the simpler
repeatable inventory after native Zotero item keys were saved in front matter.
Task context: _planning/bibliography-work-plan.md.
Reviewed matches, source details, and attachment-filing exceptions:
_planning/zotero-false-negative-review-2026-09-29.md.

Zotero's live local API (or a closed database snapshot) gives collection
membership and stable item keys. Better BibTeX's full-library export gives
citation keys. Exact DOI or title joins the sources; uncertain joins are
reported, never guessed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sqlite3
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from functools import lru_cache
from pathlib import Path

import yaml

from standardize_papers import ReviewNeeded, bib_block, parse_bibtex, plain_text, split_outside_braces, zotero_keys


ROOT = Path(__file__).resolve().parents[1]
ZOTERO = Path.home() / "Zotero"
DEFAULT_DB = ZOTERO / "zotero.sqlite"
DEFAULT_BIB = ZOTERO / "My Library (Zotero bibtex autoexport).bib"
ENTRY = re.compile(r"(?m)^@[A-Za-z]+\s*[{(]")
NONWORK_TYPES = {"annotation", "attachment", "note"}


@dataclass(frozen=True)
class Item:
    key: str
    title: str
    kind: str
    year: str
    doi: str


@dataclass(frozen=True)
class Bib:
    citekey: str
    title: str
    year: str
    doi: str
    arxiv: str
    files: str
    authors: str


@dataclass(frozen=True)
class Page:
    key: str
    title: str
    year: str
    doi: str
    path: str
    arxiv: str
    authors: str
    zotero_keys: tuple[str, ...] = ()


@lru_cache(maxsize=4096)
def clean_title(value: str) -> str:
    value = re.sub(r"\\([&%_$#])", r"\1", value)
    try:
        value = plain_text(value)
    except ReviewNeeded:
        # Keep unhandled TeX visible in the report; do not invent a title.
        value = value.replace("{", "").replace("}", "")
    value = unicodedata.normalize("NFKD", value).casefold()
    value = "".join(char for char in value if not unicodedata.combining(char))
    return "".join(char for char in value if char.isalnum())


@lru_cache(maxsize=1024)
def author_names(raw: str) -> list[str]:
    if not raw.strip():
        return []
    names = []
    for part in split_outside_braces(raw, " and "):
        try:
            names.append(plain_text(part))
        except ReviewNeeded:
            names.append(part)
    return names


def author_overlap(a: str, b: str) -> tuple[int, int, int]:
    """Count shared names for review. Years play no part in this comparison.

    Use family names where BibTeX supplies a comma. For names without commas,
    also allow the other record's family name among their words. This catches
    the repo's existing 'McPherson Carl' form without rewriting the source.
    Full names remain in the report for manual checks of common surnames.
    """
    def parts(raw):
        result = []
        for name in author_names(raw):
            if clean_title(name) == "others":
                continue
            words = frozenset(clean_title(word) for word in name.replace(",", " ").split())
            surname = clean_title(name.split(",")[0]) if "," in name else clean_title(name.split()[-1])
            given = clean_title(name.split(",")[-1])[:1] if "," in name else ""
            result.append((surname, words, "," in name, given))
        return result

    left, right = parts(a), parts(b)
    assigned = {}

    def assign(i, seen):
        surname, words, comma, given = left[i]
        for j, (other, other_words, other_comma, other_given) in enumerate(right):
            compatible = words == other_words or surname == other or (not comma and other in words) or (not other_comma and surname in other_words)
            if words != other_words and given and other_given and given != other_given:
                compatible = False
            if compatible and j not in seen:
                seen.add(j)
                if j not in assigned or assign(assigned[j], seen):
                    assigned[j] = i
                    return True
        return False

    for i in range(len(left)):
        assign(i, set())
    return len(assigned), len(left), len(right)


def clean_doi(value: str) -> str:
    return re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value.strip(), flags=re.I).lower()


def year(value: str) -> str:
    match = re.search(r"(?:18|19|20)\d{2}", str(value))
    return match.group() if match else ""


def arxiv_id(*values: str) -> str:
    for value in values:
        match = re.search(r"(?:arxiv[.:/ ]+)?(\d{4}\.\d{4,5})(?:v\d+)?", value, re.I)
        if match:
            return match.group(1)
    return ""


def database_items(path: Path, collection: str) -> tuple[list[Item], Counter]:
    connection = sqlite3.connect(path.resolve().as_uri() + "?mode=ro&immutable=1", uri=True)
    try:
        rows = connection.execute(
            "SELECT collectionID FROM collections WHERE collectionName = ?", (collection,)
        ).fetchall()
        if len(rows) != 1:
            raise ValueError(f"expected one collection named {collection!r}; found {len(rows)}")
        query = """
            SELECT i.key, t.typeName,
                MAX(CASE WHEN f.fieldName = 'title' THEN v.value END),
                MAX(CASE WHEN f.fieldName = 'date' THEN v.value END),
                MAX(CASE WHEN f.fieldName = 'DOI' THEN v.value END)
            FROM collectionItems ci
            JOIN items i ON i.itemID = ci.itemID
            JOIN itemTypes t ON t.itemTypeID = i.itemTypeID
            LEFT JOIN itemData d ON d.itemID = i.itemID
            LEFT JOIN fields f ON f.fieldID = d.fieldID
            LEFT JOIN itemDataValues v ON v.valueID = d.valueID
            WHERE ci.collectionID = ?
              AND NOT EXISTS (SELECT 1 FROM deletedItems x WHERE x.itemID = i.itemID)
            GROUP BY i.itemID
            ORDER BY i.key
        """
        raw = connection.execute(query, (rows[0][0],)).fetchall()
    finally:
        connection.close()
    types = Counter(row[1] for row in raw)
    items = [Item(key, title or "", kind, year(date or ""), clean_doi(doi or ""))
             for key, kind, title, date, doi in raw if kind not in NONWORK_TYPES]
    return items, types


def live_items(collection: str) -> tuple[list[Item], Counter]:
    base = "http://127.0.0.1:23119/api/users/0"
    with urllib.request.urlopen(base + "/collections?limit=100", timeout=5) as response:
        collections = json.load(response)
    matches = [row for row in collections if row.get("data", row).get("name") == collection]
    if len(matches) != 1:
        raise ValueError(f"expected one live collection named {collection!r}; found {len(matches)}")
    key = matches[0]["key"]
    raw = []
    start = 0
    while True:
        query = urllib.parse.urlencode({"limit": 100, "start": start})
        url = f"{base}/collections/{key}/items/top?{query}"
        with urllib.request.urlopen(url, timeout=10) as response:
            batch = json.load(response)
        raw.extend(batch)
        if len(batch) < 100:
            break
        start += len(batch)
    types = Counter(row["data"]["itemType"] for row in raw)
    items = [Item(row["key"], data.get("title", ""), data["itemType"],
                  year(data.get("date", "")), clean_doi(data.get("DOI", "")))
             for row in raw for data in [row["data"]]
             if data["itemType"] not in NONWORK_TYPES]
    return sorted(items, key=lambda item: item.key), types


def exported_entries(path: Path) -> list[Bib]:
    source = path.read_text(encoding="utf-8-sig")
    starts = list(ENTRY.finditer(source))
    if not starts:
        raise ValueError("Better BibTeX export contains no entries")
    entries = []
    errors = []
    for index, start in enumerate(starts):
        chunk = source[start.start():starts[index + 1].start() if index + 1 < len(starts) else len(source)].strip()
        try:
            citekey, fields = parse_bibtex(chunk)
        except ReviewNeeded as exc:
            errors.append(f"entry {index + 1}: {exc}")
            continue
        title = fields.get("title", "")
        if not title:
            errors.append(f"{citekey}: missing title")
            continue
        entries.append(Bib(citekey, plain_text(title) if "\\" not in title else title,
                           year(fields.get("year", "")), clean_doi(fields.get("doi", "")),
                           arxiv_id(*(fields.get(name, "") for name in ("eprint", "doi", "url"))),
                           fields.get("file", ""), fields.get("author", "")))
    if errors:
        raise ValueError("Cannot parse full BibTeX export:\n" + "\n".join(errors[:15]))
    keys = [entry.citekey for entry in entries]
    if len(keys) != len(set(keys)):
        raise ValueError("Better BibTeX export contains duplicate citation keys")
    return entries


def paper_pages() -> list[Page]:
    pages = []
    for path in sorted((ROOT / "paper").glob("*.md")):
        if "template" in path.name.lower():
            continue
        source = path.read_text(encoding="utf-8-sig")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---", source, flags=re.S)
        if not match:
            raise ValueError(f"missing front matter: {path}")
        front = yaml.safe_load(match.group(1)) or {}
        title = front.get("title")
        if not isinstance(title, str) or not title:
            raise ValueError(f"missing title: {path}")
        try:
            _, fields = parse_bibtex(bib_block(source[match.end():]))
        except ReviewNeeded as exc:
            raise ValueError(f"cannot read paper BibTeX in {path}: {exc}") from exc
        doi = clean_doi(fields.get("doi", ""))
        pages.append(Page(path.stem, title, year(front.get("pub_year", "")), doi,
                          path.relative_to(ROOT).as_posix(),
                          arxiv_id(*(fields.get(name, "") for name in ("eprint", "doi", "url", "journal"))),
                          fields.get("author", ""), zotero_keys(front.get("zotero_key"))))
    return pages


def join_items(items: list[Item], entries: list[Bib]) -> tuple[list[tuple[Item, Bib, str]], list[tuple[Item, str]]]:
    by_doi = defaultdict(list)
    by_title = defaultdict(list)
    for entry in entries:
        if entry.doi:
            by_doi[entry.doi].append(entry)
        by_title[clean_title(entry.title)].append(entry)
    joined = []
    unresolved = []
    used = {}
    for item in items:
        candidates = by_doi.get(item.doi, []) if item.doi else []
        method = "DOI"
        if len(candidates) != 1:
            candidates = by_title.get(clean_title(item.title), []) if item.title else []
            method = "title"
        if len(candidates) > 1 and item.year:
            candidates = [entry for entry in candidates if entry.year == item.year]
            method += "+year"
        if len(candidates) != 1:
            reason = ("ambiguous export keys: " + ", ".join(entry.citekey for entry in candidates)) if candidates else "no export match"
            unresolved.append((item, reason))
            continue
        entry = candidates[0]
        if item.doi and entry.doi and item.doi != entry.doi:
            unresolved.append((item, f"title matched {entry.citekey}, but DOI differs"))
            continue
        if entry.citekey in used:
            unresolved.append((item, f"export key also matched Zotero item {used[entry.citekey]}"))
            continue
        used[entry.citekey] = item.key
        joined.append((item, entry, method))
    return joined, unresolved


def trigrams(title: str) -> Counter:
    value = f"  {clean_title(title)}  "
    return Counter(value[i:i + 3] for i in range(len(value) - 2))


def trigram_cosine(a: Counter, b: Counter) -> float:
    if not a or not b:
        return 0.0
    return sum(a[part] * b[part] for part in a.keys() & b.keys()) / math.sqrt(
        sum(value * value for value in a.values()) * sum(value * value for value in b.values())
    )


def unique_pairs(items: list[Item], pages: list[Page], value) -> list[tuple[Item, Page]]:
    """Return one-to-one exact value matches; leave collisions for review."""
    pages_by_value = defaultdict(list)
    for page in pages:
        if field := value(page):
            pages_by_value[field].append(page)
    items_by_page = defaultdict(list)
    page_by_key = {page.key: page for page in pages}
    for item in items:
        if field := value(item):
            matches = pages_by_value.get(field, [])
            if len(matches) == 1:
                items_by_page[matches[0].key].append(item)
    return [(matches[0], page_by_key[key]) for key, matches in items_by_page.items() if len(matches) == 1]


def page_match_cascade(items: list[Item], pages: list[Page],
                       joined: list[tuple[Item, Bib, str]]) -> tuple[dict[str, Page], list[tuple[Item, Page]], list[tuple[Item, Page]], list[Item], list[Page]]:
    page_by_key = {page.key: page for page in pages}
    key_pairs = {item.key: page_by_key[entry.citekey] for item, entry, _ in joined
                 if entry.citekey in page_by_key}
    remaining_items = [item for item in items if item.key not in key_pairs]
    used_pages = {page.key for page in key_pairs.values()}
    remaining_pages = [page for page in pages if page.key not in used_pages]
    doi_pairs = unique_pairs(remaining_items, remaining_pages, lambda record: record.doi)
    doi_items = {item.key for item, _ in doi_pairs}
    doi_pages = {page.key for _, page in doi_pairs}
    remaining_items = [item for item in remaining_items if item.key not in doi_items]
    remaining_pages = [page for page in remaining_pages if page.key not in doi_pages]
    title_pairs = unique_pairs(remaining_items, remaining_pages, lambda record: clean_title(record.title))
    export_by_item = {item.key: entry for item, entry, _ in joined}
    title_pairs = [(item, page) for item, page in title_pairs
                   if not (item.doi and page.doi and item.doi != page.doi)
                   and item.key in export_by_item
                   and author_overlap(page.authors, export_by_item[item.key].authors)[0]]
    title_items = {item.key for item, _ in title_pairs}
    title_pages = {page.key for _, page in title_pairs}
    remaining_items = [item for item in remaining_items if item.key not in title_items]
    remaining_pages = [page for page in remaining_pages if page.key not in title_pages]
    return key_pairs, doi_pairs, title_pairs, remaining_items, remaining_pages


def full_export_page_cascade(entries: list[Bib], pages: list[Page]) -> tuple[list[tuple[Bib, Page]], list[tuple[Bib, Page]], list[tuple[Bib, Page]], list[Page]]:
    by_key = {entry.citekey: entry for entry in entries}
    key_pairs = [(by_key[page.key], page) for page in pages if page.key in by_key]
    used_entries = {entry.citekey for entry, _ in key_pairs}
    used_pages = {page.key for _, page in key_pairs}
    remaining_entries = [entry for entry in entries if entry.citekey not in used_entries]
    remaining_pages = [page for page in pages if page.key not in used_pages]
    doi_pairs = unique_pairs(remaining_entries, remaining_pages, lambda record: record.doi)
    used_entries.update(entry.citekey for entry, _ in doi_pairs)
    used_pages.update(page.key for _, page in doi_pairs)
    remaining_entries = [entry for entry in entries if entry.citekey not in used_entries]
    remaining_pages = [page for page in pages if page.key not in used_pages]
    title_pairs = unique_pairs(remaining_entries, remaining_pages, lambda record: clean_title(record.title))
    title_pairs = [(entry, page) for entry, page in title_pairs
                   if not (entry.doi and page.doi and entry.doi != page.doi)
                   and author_overlap(page.authors, entry.authors)[0]]
    used_pages.update(page.key for _, page in title_pairs)
    remaining_pages = [page for page in pages if page.key not in used_pages]
    return key_pairs, doi_pairs, title_pairs, remaining_pages


def cell(value: str) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def full_export_leads(pages: list[Page], entries: list[Bib],
                      processed_keys: set[str], paired_keys: dict[str, str]):
    """Rank review leads without making an identity decision."""
    vectors = {entry.citekey: trigrams(entry.title) for entry in entries}
    attachment_titles = {entry.citekey: [re.split(r"[\\/]", part)[-1].removesuffix(".pdf")
                                       for part in entry.files.split(";") if part]
                         for entry in entries}
    leads = []
    for page in pages:
        page_vector = trigrams(page.title)
        for entry in entries:
            score = trigram_cosine(page_vector, vectors[entry.citekey])
            same_arxiv = bool(page.arxiv and page.arxiv == entry.arxiv)
            attachment = bool(re.search(r"\b" + re.escape(page.key) + r"(?=[^a-z0-9]|$)",
                                        entry.files, re.I))
            attachment = attachment or any(clean_title(name) == clean_title(page.title)
                                           for name in attachment_titles[entry.citekey])
            shared_authors = author_overlap(page.authors, entry.authors)
            if score >= 0.60 or same_arxiv or attachment or shared_authors[0]:
                leads.append((page, entry, score, same_arxiv, attachment,
                              entry.citekey in processed_keys,
                              paired_keys.get(entry.citekey, ""), shared_authors))
    return sorted(leads, key=lambda row: (-row[5], -row[3], -row[4], -row[2], row[0].key, row[1].citekey))


def report(items: list[Item], types: Counter, entries: list[Bib], pages: list[Page],
           joined: list[tuple[Item, Bib, str]], unresolved: list[tuple[Item, str]],
           source_label: str, export: Path) -> str:
    by_key = {page.key: page for page in pages}
    mapped_keys = {entry.citekey for _, entry, _ in joined}
    shared = [(item, entry, by_key[entry.citekey]) for item, entry, _ in joined if entry.citekey in by_key]
    zotero_only = [(item, entry) for item, entry, _ in joined if entry.citekey not in by_key]
    repo_only = [page for page in pages if page.key not in mapped_keys]
    zotero_vectors = {entry.citekey: trigrams(entry.title) for _, entry in zotero_only}
    page_vectors = {page.key: trigrams(page.title) for page in repo_only}
    candidates = []
    for item, entry in zotero_only:
        for page in repo_only:
            score = trigram_cosine(zotero_vectors[entry.citekey], page_vectors[page.key])
            if score >= 0.55 or (entry.doi and entry.doi == page.doi):
                candidates.append((score, bool(entry.doi and entry.doi == page.doi), item, entry, page))
    candidates.sort(key=lambda row: (-row[1], -row[0], row[3].citekey, row[4].key))
    high = [row for row in candidates if row[0] >= 0.9]
    high_zotero = {row[3].citekey for row in high}
    high_pages = {row[4].key for row in high}
    methods = Counter(method for _, _, method in joined)
    key_pairs, doi_pairs, title_pairs, remaining_items, remaining_pages = page_match_cascade(items, pages, joined)
    full_key, full_doi, full_title, full_remaining = full_export_page_cascade(entries, pages)
    processed_pages = {page.key for page in key_pairs.values()}
    processed_pages.update(page.key for _, page in doi_pairs + title_pairs)
    full_only = [(entry, page) for entry, page in full_key + full_doi + full_title
                 if page.key not in processed_pages]
    processed_keys = {entry.citekey for _, entry, _ in joined}
    paired_keys = {entry.citekey: page.key for entry, page in full_key + full_doi + full_title}
    leads = full_export_leads(full_remaining, entries, processed_keys, paired_keys)
    lines = ["# Zotero processed/read vs. paper filenames", "",
             f"Generated: {datetime.now().astimezone().isoformat(timespec='seconds')}",
             source_label,
             f"Better BibTeX export: `{export}` (modified {datetime.fromtimestamp(export.stat().st_mtime).astimezone().isoformat(timespec='seconds')})",
             f"Export SHA-256: `{hashlib.sha256(export.read_bytes()).hexdigest()}`.",
             "Repo titles come from paper-page YAML; repo authors and identifiers come from each page's BibTeX. Export titles, authors, identifiers, and attachment paths come from Better BibTeX. Collection membership comes from the separately identified Zotero source above.",
             "These are snapshots. This report changes no Zotero records or paper pages.", "",
             f"Collection: {sum(types.values())} items; {len(items)} substantive works. Types: " +
             ", ".join(f"{kind} {count}" for kind, count in types.most_common()) + ".",
             f"Export: {len(entries)} entries. Paper pages: {len(pages)}.",
             f"Joined to export by DOI/title: {len(joined)}; unresolved: {len(unresolved)}.",
             "Join methods: " + ", ".join(f"{method} {count}" for method, count in methods.most_common()) + ".",
             f"Exact citation-key/file-stem intersection: {len(shared)}.",
             f"Page match cascade: {len(key_pairs)} exact key, then {len(doi_pairs)} unique DOI, then {len(title_pairs)} unique normalized title.",
             f"After the cascade: {len(remaining_items)} processed/read works and {len(remaining_pages)} paper pages have no deterministic pair.",
             f"Against the full Zotero export: {len(full_key)} paper pages pair by key, {len(full_doi)} more by DOI, {len(full_title)} more by normalized title; {len(full_remaining)} paper pages have no deterministic pair.",
             f"Full-export pairs outside processed/read: {len(full_only)} paper pages.",
             f"Symmetric difference after source join: {len(zotero_only)} Zotero-only keys + {len(repo_only)} paper-only stems = {len(zotero_only) + len(repo_only)}.",
             f"Title candidates: {len(candidates)} pairs score at least 0.55; {len(high)} pairs score at least 0.90.",
             f"High-score pairs use {len(high_zotero)} distinct Zotero keys and {len(high_pages)} distinct paper stems.",
             "Unique normalized-title pairs are candidates for review, not approved identity links.",
             "An unmatched key does not by itself mean a missing work: names can differ, and the collection includes non-paper types.", "",
             "## Ranked possible key clashes", "",
             "Character-trigram cosine on lowercased, accent-folded titles. Scores rank review; they do not approve a link.", "",
             "| Score | DOI | Zotero item | Zotero key | Zotero title | Zotero year | Repo stem | Repo title | Repo year | Type |",
             "|---:|:---:|---|---|---|---:|---|---|---:|---|"]
    for score, same_doi, item, entry, page in candidates:
        lines.append(f"| {score:.3f} | {'yes' if same_doi else ''} | {cell(item.key)} | {cell(entry.citekey)} | {cell(entry.title)} | {cell(item.year)} | {cell(page.key)} | {cell(page.title)} | {cell(page.year)} | {cell(item.kind)} |")
    lines.extend(["", "## Review leads for pages without a deterministic full-export match", "",
                  f"Scanned all {len(full_remaining)} such pages against all {len(entries)} export entries, including entries already paired with another page.",
                  "Titles are converted from TeX, accent-folded, lowercased, and stripped to letters and numbers, including removal of spaces. Years do not enter fuzzy comparison.",
                  "Show every pair with a shared author surname and compatible first initial, regardless of title score; also show title scores at least 0.60, matching arXiv IDs, or attachment names matching the page stem or title. Full author lists are retained for checking name matches. An attachment may be filed under the wrong Zotero item.", "",
                  "| Page stem | Page title | Page authors | Export key | Export title | Export authors | Shared authors (page/export totals) | Title score | arXiv | Attachment name | Processed/read item key | Already paired page |",
                  "|---|---|---|---|---|---|---|---:|:---:|:---:|---|---|"])
    item_by_export = {entry.citekey: item.key for item, entry, _ in joined}
    for page, entry, score, same_arxiv, attachment, processed, paired_page, authors in leads:
        shared_count, page_count, export_count = authors
        lines.append(f"| {cell(page.key)} | {cell(page.title)} | {cell('; '.join(author_names(page.authors)))} | {cell(entry.citekey)} | {cell(entry.title)} | {cell('; '.join(author_names(entry.authors)))} | {shared_count} ({page_count}/{export_count}) | {score:.3f} | {'yes' if same_arxiv else ''} | {'yes' if attachment else ''} | {item_by_export.get(entry.citekey, 'not joined to processed/read')} | {cell(paired_page)} |")
    lines.extend(["", "## Coverage of every paper page without a deterministic pair", "",
                  "The closest title is shown even when it is a poor match. This records coverage; it does not recommend that pair.", "",
                  "| Page stem | Page title | Page authors | Closest export title | Export key | Title score | Shared authors |",
                  "|---|---|---|---|---|---:|---:|"])
    export_vectors = {entry.citekey: trigrams(entry.title) for entry in entries}
    for page in sorted(full_remaining, key=lambda page: page.key):
        vector = trigrams(page.title)
        closest = max(entries, key=lambda entry: trigram_cosine(vector, export_vectors[entry.citekey]))
        score = trigram_cosine(vector, export_vectors[closest.citekey])
        shared_count = author_overlap(page.authors, closest.authors)[0]
        lines.append(f"| {cell(page.key)} | {cell(page.title)} | {cell('; '.join(author_names(page.authors)))} | {cell(closest.title)} | {cell(closest.citekey)} | {score:.3f} | {shared_count} |")
    key_by_item = {item.key: entry.citekey for item, entry, _ in joined}
    lines.extend(["", "## Processed/read works still unmatched after the cascade", "",
                  "| Zotero item key | Better BibTeX key | Title | Type | Year |",
                  "|---|---|---|---|---:|"])
    for item in sorted(remaining_items, key=lambda item: (item.title.casefold(), item.key)):
        lines.append(f"| {cell(item.key)} | {cell(key_by_item.get(item.key, ''))} | {cell(item.title)} | {cell(item.kind)} | {cell(item.year)} |")
    lines.extend(["", "## Paper pages paired in the full export but not processed/read", "",
                  "| Paper stem | Export key | Title |", "|---|---|---|"])
    for entry, page in sorted(full_only, key=lambda pair: pair[1].key):
        lines.append(f"| {cell(page.key)} | {cell(entry.citekey)} | {cell(page.title)} |")
    lines.extend(["", "## Zotero-only keys", "", "| Key | Title | Type | Year | Zotero item key |", "|---|---|---|---:|---|"])
    for item, entry in sorted(zotero_only, key=lambda pair: pair[1].citekey):
        lines.append(f"| {cell(entry.citekey)} | {cell(entry.title)} | {cell(item.kind)} | {cell(item.year)} | {cell(item.key)} |")
    lines.extend(["", "## Paper-only stems", "", "| Stem | Title | Year | Path |", "|---|---|---:|---|"])
    for page in sorted(repo_only, key=lambda page: page.key):
        lines.append(f"| {cell(page.key)} | {cell(page.title)} | {cell(page.year)} | {cell(page.path)} |")
    lines.extend(["", "## Collection items without a unique Better BibTeX export match", "", "| Zotero item key | Title | Type | Reason |", "|---|---|---|---|"])
    for item, reason in unresolved:
        lines.append(f"| {cell(item.key)} | {cell(item.title)} | {cell(item.kind)} | {cell(reason)} |")
    return "\n".join(lines) + "\n"


def saved_key_report(items: list[Item], pages: list[Page], source_label: str) -> str:
    """Inventory by native Zotero keys; no export or fuzzy matching needed."""
    paths_by_key = defaultdict(list)
    for page in pages:
        for key in page.zotero_keys:
            paths_by_key[key].append(page.path)
    present = [item for item in items if item.key in paths_by_key]
    unlinked = [item for item in items if item.key not in paths_by_key]
    linked_pages = sum(bool(page.zotero_keys) for page in pages)
    lines = ["# Zotero read inventory by saved item key", "",
             f"Generated: {datetime.now().astimezone().isoformat(timespec='seconds')}", source_label,
             "Repo source: `zotero_key` in paper-page YAML. One string or a list is accepted. No Better BibTeX export or title matching was used.", "",
             f"Repo: {len(pages)} paper pages; {linked_pages} with saved keys; {len(pages) - linked_pages} without.",
             f"Saved identifiers: {len(paths_by_key)} distinct Zotero items.",
             f"Collection: {len(items)} substantive records; {len(present)} already represented; {len(unlinked)} without a saved paper-page link.",
             "Records without saved links need review before import, including the attachment-only cases in the false-negative review. This is not an automatic import list.", "",
             "## Already represented: skip when importing", "",
             "| Zotero item key | Zotero title | Repo pages |", "|---|---|---|"]
    for item in sorted(present, key=lambda item: item.title.casefold()):
        lines.append(f"| {item.key} | {cell(item.title)} | {cell(', '.join(paths_by_key[item.key]))} |")
    lines.extend(["", "## No saved paper-page link", "",
                  "| Zotero item key | Zotero title | Item type |", "|---|---|---|"])
    for item in sorted(unlinked, key=lambda item: item.title.casefold()):
        lines.append(f"| {item.key} | {cell(item.title)} | {item.kind} |")
    outside = set(paths_by_key) - {item.key for item in items}
    if outside:
        lines.extend(["", "## Saved keys outside this collection snapshot", "",
                      "These may still exist elsewhere in the library.", ""])
        for key in sorted(outside):
            lines.append(f"- {key}: {', '.join(paths_by_key[key])}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--bib", type=Path, default=DEFAULT_BIB)
    parser.add_argument("--collection", default="processed / read")
    parser.add_argument("--out", type=Path, help="write a Markdown report; otherwise print it")
    parser.add_argument("--saved-keys", action="store_true", help="inventory by saved Zotero item keys only; do not load the Better BibTeX export or run fuzzy comparisons")
    args = parser.parse_args()
    try:
        items, types = live_items(args.collection)
        source_label = f"Zotero collection: live read-only local API, `{args.collection}`."
    except (urllib.error.URLError, TimeoutError, ConnectionError):
        wal = Path(str(args.db) + "-wal")
        if wal.exists() and wal.stat().st_size:
            raise RuntimeError("Zotero's live API is unavailable and its write-ahead log is active; refusing a stale database snapshot")
        items, types = database_items(args.db, args.collection)
        source_label = (f"Zotero database snapshot: `{args.db}` "
                        f"(modified {datetime.fromtimestamp(args.db.stat().st_mtime).astimezone().isoformat(timespec='seconds')}).")
    pages = paper_pages()
    if args.saved_keys:
        output = saved_key_report(items, pages, source_label)
        if args.out:
            args.out.write_text(output, encoding="utf-8")
            print(f"Wrote {args.out}: inventory by saved Zotero keys")
        else:
            sys.stdout.write(output)
        return 0
    entries = exported_entries(args.bib)
    joined, unresolved = join_items(items, entries)
    output = report(items, types, entries, pages, joined, unresolved, source_label, args.bib)
    if args.out:
        args.out.write_text(output, encoding="utf-8")
        print(f"Wrote {args.out}: {len(joined)} joined, {len(unresolved)} unresolved")
    else:
        sys.stdout.write(output)
    return 0 if not unresolved else 1


if __name__ == "__main__":
    sys.exit(main())
