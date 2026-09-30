"""List unlinked read items and import new Markdown papers from Zotero.

Provenance: Created by OpenAI Codex for Robert Winslow's September 2026
bibliography cleanup. Developed through a one-paper pilot, then batch import: copy metadata,
notes, highlights, and annotation comments without rewriting Robert's words.
Existing Zotero links are skipped before fetching notes or BibTeX. This tool
only reads Zotero and never overwrites a Markdown file. See the repo-local
zotero-paper-import skill for the review step before adopting a draft.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import subprocess
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

import yaml

from standardize_papers import (
    ReviewNeeded, parse_authors, parse_bibtex, plain_text, split_frontmatter, bib_block, normalized,
    yaml_front, zotero_keys,
)

ROOT = Path(__file__).resolve().parents[1]
ENTRY_DIRS = ("paper", "article", "book", "report", "data", "zotero")
NONWORK_TYPES = {"attachment", "annotation", "note"}
BIB_FIELDS = (
    "title", "author", "year", "journal", "booktitle", "volume", "number",
    "pages", "publisher", "institution", "school", "organization", "editor",
    "edition", "series", "chapter", "address", "doi", "url", "eprint",
    "archiveprefix", "primaryclass", "isbn", "issn",
)


class Zotero:
    def __init__(self, base="http://127.0.0.1:23119/api/users/0"):
        self.base = base.rstrip("/")

    def text(self, path):
        with urllib.request.urlopen(self.base + path, timeout=15) as response:
            return response.read().decode("utf-8")

    def get(self, path):
        return json.loads(self.text(path))

    def all(self, path):
        rows, seen = [], set()
        while True:
            sep = "&" if "?" in path else "?"
            batch = self.get(f"{path}{sep}limit=100&start={len(rows)}")
            for row in batch:
                if row["key"] in seen:
                    raise ReviewNeeded("Zotero pagination repeated an item; retry the inventory")
                seen.add(row["key"])
            rows.extend(batch)
            if len(batch) < 100:
                return rows

    def read_collection(self):
        matches = [row for row in self.all("/collections")
                   if row["data"]["name"] == "processed / read"]
        if len(matches) != 1:
            raise ReviewNeeded("expected exactly one collection named processed / read")
        key = matches[0]["key"]
        return [row for row in self.all(f"/collections/{key}/items/top")
                if row["data"]["itemType"] not in NONWORK_TYPES]


def saved_links(root=ROOT):
    """Read only front matter, across entry folders; do not audit page bodies."""
    links = {}
    for directory in ENTRY_DIRS:
        for path in sorted((root / directory).rglob("*.md")):
            if "template" in path.name.lower():
                continue
            source = path.read_text(encoding="utf-8-sig")
            match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", source, re.S)
            if not match or not re.search(r"(?m)^zotero_key\s*:", match.group(1)):
                continue
            front = yaml.safe_load(match.group(1))
            for key in zotero_keys(front.get("zotero_key")):
                links.setdefault(key, []).append(path.relative_to(root).as_posix())
    return links


def clean_bibtex(source, expected_key=None):
    # Zotero can emit the same DOI twice (native field plus Extra). Remove only
    # identical complete DOI lines; conflicting values still stop for review.
    seen_doi_lines = set()
    kept = []
    for line in source.splitlines(keepends=True):
        if re.fullmatch(r"\s*doi\s*=\s*\{[^{}\r\n]+\},?\s*", line, re.I):
            value = re.search(r"\{([^{}]+)\}", line).group(1)
            if value in seen_doi_lines:
                continue
            seen_doi_lines.add(value)
        kept.append(line)
    source = "".join(kept)
    key, fields = parse_bibtex(source.strip())
    key = expected_key or key
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", key):
        raise ReviewNeeded(f"citation key needs a filename decision: {key!r}")
    for name in ("title", "author", "year"):
        if not fields.get(name):
            raise ReviewNeeded(f"BibTeX lacks {name}; verify the citation before drafting")
    if not re.fullmatch(r"\d{4}", fields["year"]):
        raise ReviewNeeded("BibTeX year needs review")
    kind = re.match(r"\s*@([A-Za-z]+)", source).group(1).lower()
    lines = [f"@{kind}{{{key},"]
    lines.extend(f"  {name} = {{{fields[name]}}}," for name in BIB_FIELDS if fields.get(name))
    lines.append("}")
    # Reparse the reduced entry to catch unsupported syntax before writing it.
    bib = "\n".join(lines)
    parse_bibtex(bib)
    return key, fields, bib


def note_markdown(value):
    """Convert rich text mechanically; stop on unsupported note contents."""
    if re.search(r"data-annotation|data-citation|<\s*(?:img|math|svg)\b", value, re.I):
        raise ReviewNeeded("note contains embedded annotations, citations, or images; review it to avoid loss or duplicate excerpts")
    if not re.search(r"</?[A-Za-z][^>]*>", value):
        return value.strip()
    # Zotero's editor wrapper is not content. Keeping it would stop Jekyll
    # from parsing the Markdown that Pandoc puts inside the raw HTML div.
    value = re.sub(r'\A\s*<div\s+(?:data-)?schema-version="\d+"\s*>(.*)</div>\s*\Z',
                   r'\1', value, flags=re.S)
    result = subprocess.run(
        ["pandoc", "--from=html", "--to=gfm", "--wrap=none"],
        input=value, text=True, encoding="utf-8", capture_output=True, check=True,
    )
    return result.stdout.strip()


def nested_note(value):
    """Place source headings below the level-three Zotero note heading."""
    lines = note_markdown(value).splitlines()
    fenced = False
    for i, line in enumerate(lines):
        if re.match(r"^\s*(```|~~~)", line):
            fenced = not fenced
        if not fenced:
            match = re.match(r"^(#{1,6}) (.*)$", line)
            if match:
                lines[i] = "#" * min(6, len(match[1]) + 3) + " " + match[2]
    return "\n".join(lines)


def quote(value):
    return "\n".join("> " + line if line else ">" for line in value.splitlines())


def web_link(label, url):
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme not in {"https", "http"} or not parsed.netloc:
        raise ReviewNeeded(f"not a public web link: {url!r}")
    return f"[{label}](<{url}>)"


def source_label(url, kind):
    """Name known hosts; otherwise show the actual hostname, without guessing."""
    host = (urllib.parse.urlsplit(url).hostname or "").lower().removeprefix("www.")
    name = "AEA" if host == "aeaweb.org" or host.endswith(".aeaweb.org") else host
    return f"{name} {kind}"


def collect_bundle(api, item):
    key = item["key"]
    children = api.all(f"/items/{key}/children")
    annotations = []
    for child in children:
        if child["data"]["itemType"] == "attachment":
            # The ordinary children endpoint omits annotations by default.
            annotations.extend(api.all(f"/items/{child['key']}/children?itemType=annotation"))
    _, _, bib = clean_bibtex(api.text(f"/items/{key}?format=bibtex"), item["data"].get("citationKey"))
    return {"item": item, "children": children, "annotations": annotations,
            "bibtex": bib, "source": api.base, "collection": "processed / read"}


def render(bundle, created, extra_links=(), verified_against=None):
    item = bundle["item"]
    data = item["data"]
    key, fields, bib = clean_bibtex(bundle["bibtex"], data.get("citationKey"))
    title = plain_text(fields["title"])
    authors = parse_authors(fields["author"])
    tags = sorted({tag["tag"] for tag in data.get("tags", []) if tag.get("tag")})
    front = yaml_front(title, authors, int(fields["year"]), created, created, tags, item["key"])
    provenance = f"Imported from Zotero item {item['key']} on {created}; citation source: Zotero BibTeX export."
    if verified_against:
        web_link("source", verified_against)
        provenance += f" Citation checked against: {verified_against}."
    lines = [front.rstrip(), "", f"<!-- {provenance} -->", ""]
    links, seen = [], set()
    candidates = []
    if data.get("DOI"):
        doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", data["DOI"], flags=re.I)
        candidates.append(("DOI", "https://doi.org/" + doi))
    if data.get("url"):
        candidates.append((source_label(data["url"], "paper page"), data["url"]))
    for child in bundle["children"]:
        d = child["data"]
        if d["itemType"] == "attachment" and d.get("contentType") == "application/pdf" and d.get("url"):
            candidates.append((source_label(d["url"], "PDF"), d["url"]))
    candidates.extend(extra_links)
    for label, url in candidates:
        if url not in seen:
            links.append(web_link(label, url))
            seen.add(url)
    if links:
        lines.extend([" · ".join(links), ""])
    lines.extend(["## BibTeX", "", "```bibtex", bib, "```", ""])
    abstract = note_markdown(data.get("abstractNote", ""))
    if abstract:
        lines.extend(["## Abstract", "", quote(abstract), ""])
    else:
        lines.extend(["<!--", "## Abstract", "-->", ""])
    notes = [row["data"] for row in bundle["children"] if row["data"]["itemType"] == "note"]
    annotations = sorted((row["data"] for row in bundle["annotations"]),
                         key=lambda d: (d["parentItem"], d.get("annotationSortIndex", ""), d["key"]))
    if len({d["key"] for d in annotations}) != len(annotations):
        raise ReviewNeeded("duplicate annotation keys in response")
    is_green = lambda d: d.get("annotationColor", "").lower() == "#5fb236"
    if not notes and not annotations:
        lines.extend(["<!--", "## Notes and Excerpts", "-->", ""])
    else:
        lines.extend(["## Notes and Excerpts", ""])
    for note in sorted(notes, key=lambda d: (d.get("dateAdded", ""), d["key"])):
        text = nested_note(note.get("note", ""))
        lines.extend([f"<!-- Zotero note {note['key']} -->", "### Zotero note", "", text, ""])
    visible_chunks = []
    color_names = {"#5fb236": "green", "#ff6666": "red", "#2ea8e5": "blue",
                   "#a28ae5": "purple", "#e56eee": "magenta", "#f19837": "orange",
                   "#aaaaaa": "gray"}
    for annotation in annotations:
        kind = annotation.get("annotationType")
        text = annotation.get("annotationText", "")
        comment = annotation.get("annotationComment", "")
        if kind not in {"highlight", "underline", "note", "text"} or not (text.strip() or comment.strip()):
            raise ReviewNeeded(f"annotation {annotation['key']} needs manual review: {kind}, no supported text representation")
        color = annotation.get("annotationColor", "").lower()
        provenance = f"Zotero annotation {annotation['key']}; attachment {annotation['parentItem']}"
        if color and color != "#ffd400":
            provenance += f"; color {'green ' if is_green(annotation) else ''}{color}"
        chunk = [f"<!-- {provenance} -->"]
        if text:
            excerpt = quote(text)
            if annotation.get("annotationPageLabel"):
                excerpt += "\n>\n> *p. " + annotation["annotationPageLabel"] + "*"
            chunk.append(excerpt)
            if color and color != "#ffd400":
                chunk.append("{: .zotero-" + color_names.get(color, "other") + "}")
            chunk.append("")
        elif annotation.get("annotationPageLabel"):
            chunk.extend(["*p. " + annotation["annotationPageLabel"] + "*", ""])
        if comment:
            chunk.extend([note_markdown(comment), ""])
        rendered = "\n".join(chunk).rstrip()
        visible_chunks.append(rendered)
    if visible_chunks:
        lines.extend(["\n\n---\n\n".join(visible_chunks), ""])
    return key, "\n".join(lines).rstrip() + "\n"


def write_new(path, source):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as output:
        output.write(source)


def batch_import(api, items, links, apply=False):
    """Create new paper pages only; uncertain identities and content need review."""
    existing = []
    before = {}
    for directory in ENTRY_DIRS:
        for path in sorted((ROOT / directory).rglob("*.md")):
            if "template" in path.name.lower():
                continue
            before[path] = path.read_bytes()
            try:
                front, body = split_frontmatter(before[path].decode("utf-8-sig"))
            except ReviewNeeded:
                continue
            fields = {}
            try:
                _, fields = parse_bibtex(bib_block(body))
            except ReviewNeeded:
                pass
            title = front.get("title") or fields.get("title", "")
            existing.append((path.relative_to(ROOT).as_posix(), normalized(str(title)),
                             fields.get("doi", "").lower().removeprefix("https://doi.org/")))
    counts = {"linked": 0, "ready": 0, "imported": 0, "review": 0}
    print("# Zotero batch import\n")
    print("Source: live processed / read collection; native Zotero keys. Metadata and links come from Zotero; no external publication verification is claimed. No JSON snapshots.\n")
    print("| Status | Item key | Page or title | Detail |\n|---|---|---|---|")
    for item in sorted(items, key=lambda row: row["data"].get("title", "").casefold()):
        key, data = item["key"], item["data"]
        if key in links:
            counts["linked"] += 1
            continue
        title = data.get("title", "(no title)")
        try:
            if data["itemType"] not in {"journalArticle", "preprint", "conferencePaper"}:
                raise ReviewNeeded("outside paper import: " + data["itemType"])
            # This record contains another paper's PDF, identified in the earlier review.
            if key == "NFGWLEB6":
                raise ReviewNeeded("known misfiled Aumann-Peleg attachment; resolve record first")
            norm_title = normalized(title)
            doi = data.get("DOI", "").lower().removeprefix("https://doi.org/")
            candidates = [p for p, t, d in existing if (doi and doi == d) or
                          (norm_title and t and (norm_title == t or difflib.SequenceMatcher(None, norm_title, t).ratio() >= 0.80))]
            # Reviewed in zotero-false-negative-review-2026-09-29.md:
            # Davidson/Woodbury and Hopenhayn/Nicolini are distinct papers.
            if key == "Y7C9KD24":
                candidates = [p for p in candidates if p != "paper/hopenhayn1997optimal.md"]
            if candidates:
                raise ReviewNeeded("possible existing paper/version: " + ", ".join(candidates))
            bundle = collect_bundle(api, item)
            citekey, source = render(bundle, date.today().isoformat())
            path = ROOT / "paper" / (citekey + ".md")
            if path.exists():
                raise ReviewNeeded("filename already exists: " + path.name)
            for row in bundle["annotations"]:
                annotation = row["data"]
                if source.count("Zotero annotation " + annotation["key"] + ";") != 1:
                    raise ReviewNeeded("annotation identity was not preserved exactly once")
                if annotation.get("annotationText") and quote(annotation["annotationText"]) not in source:
                    raise ReviewNeeded("annotation quotation was not preserved")
                if annotation.get("annotationComment") and note_markdown(annotation["annotationComment"]) not in source:
                    raise ReviewNeeded("annotation comment was not preserved")
            if apply:
                write_new(path, source)
            status = "imported" if apply else "ready"
            counts[status] += 1
            existing.append(("paper/" + path.name, norm_title, doi))
            detail = f"{len(bundle['annotations'])} annotations; {sum(r['data']['itemType']=='note' for r in bundle['children'])} notes"
            title = "paper/" + path.name
        except (ReviewNeeded, ValueError, OSError, subprocess.CalledProcessError) as exc:
            status, detail = "review", str(exc).replace("\n", " ")
            counts["review"] += 1
        cells = [status, key, title, detail]
        print("| " + " | ".join(str(c).replace("|", "\\|") for c in cells) + " |", flush=True)
    for path, original in before.items():
        if path.read_bytes() != original:
            raise RuntimeError("existing page changed during batch: " + str(path))
    print("\nSummary: " + "; ".join(f"{v} {k}" for k, v in counts.items()))
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("list", "draft", "batch"))
    parser.add_argument("--apply", action="store_true", help="batch: write new pages; otherwise preview only")
    parser.add_argument("item_key", nargs="?")
    parser.add_argument("--out", type=Path)
    parser.add_argument("--snapshot", type=Path, help="save the source data for checking this draft")
    parser.add_argument("--link", action="append", default=[], metavar="LABEL=URL")
    parser.add_argument("--verified-against", help="publication source already checked by the reviewer")
    args = parser.parse_args()
    links = saved_links()
    api = Zotero()
    if args.mode == "draft" and args.item_key in links:
        print(f"SKIP {args.item_key}: already linked in {', '.join(links[args.item_key])}")
        return 0
    items = api.read_collection()
    if args.mode == "batch":
        return batch_import(api, items, links, args.apply)
    if args.mode == "list":
        pending = [row for row in items if row["key"] not in links]
        print(f"processed / read: {len(items)} records; {len(items)-len(pending)} already linked; {len(pending)} to review")
        for row in sorted(pending, key=lambda r: r["data"].get("title", "").casefold()):
            d = row["data"]
            print(f"{row['key']} | {d['itemType']} | {d.get('title', '(no title)')}")
        return 0
    if not args.item_key or not args.out:
        parser.error("draft requires an item key and --out")
    zotero_keys(args.item_key)
    selected = [row for row in items if row["key"] == args.item_key]
    if len(selected) != 1:
        raise ReviewNeeded("item is not in processed / read")
    if args.out.exists() or (args.snapshot and args.snapshot.exists()):
        raise FileExistsError("draft or snapshot path already exists; review it rather than overwriting it")
    bundle = collect_bundle(api, selected[0])
    extra = []
    for value in args.link:
        label, separator, url = value.partition("=")
        if not separator or not label:
            parser.error("--link must be LABEL=URL")
        extra.append((label, url))
    key, source = render(bundle, date.today().isoformat(), extra, args.verified_against)
    if (ROOT / "paper" / f"{key}.md").exists():
        raise ReviewNeeded(f"paper/{key}.md already exists without this saved link; review before importing")
    if args.snapshot:
        bundle["draft_date"] = date.today().isoformat()
        bundle["verified_against"] = args.verified_against
        bundle["extra_links"] = extra
        write_new(args.snapshot, json.dumps(bundle, ensure_ascii=False, indent=2) + "\n")
    write_new(args.out, source)
    print(f"DRAFT {args.out}; eventual paper filename: {key}.md")
    print(f"Copied {len(bundle['annotations'])} annotations and {sum(r['data']['itemType']=='note' for r in bundle['children'])} separate notes. Review before adopting.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
