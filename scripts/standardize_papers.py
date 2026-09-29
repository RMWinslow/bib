"""Check or apply the one-time paper-page frontmatter migration.

Provenance: Created by OpenAI Codex for Robert Winslow's September 2026
bibliography-repo cleanup. The original task was to standardize 194 paper
pages using their embedded BibTeX, preserve reading notes and historical page
dates, and remove reviewed duplicate title headings. Kept as a repeatable
check/apply command; later extended to preserve the Zotero linkage field.
Task context: _planning/bibliography-work-plan.md.
Usage and migration exceptions: .codex/skills/bib-paper-audit/SKILL.md and
_planning/paper-title-approvals.yml.

The BibTeX parser below reads balanced braced and quoted values. It does not
rewrite BibTeX. Unsupported syntax and uncertain names stop that page for review.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "paper"
SNAPSHOT = ROOT / "_planning" / "file-modification-index-2026-09-27.md"
APPROVALS = ROOT / "_planning" / "paper-title-approvals.yml"
ALLOWED_OLD_FIELDS = {"parent", "title", "subtitle", "layout", "date", "modified", "pub_year", "pub_authors", "tags", "zotero_key"}
H1 = re.compile(r"^#\s+(.+?)(?:\s+#+)?\s*$")
BIB_HEADER = re.compile(r"^##\s+BibTeX\s*$", re.IGNORECASE | re.MULTILINE)
FIELD_NAME = re.compile(r"[A-Za-z][A-Za-z0-9_:-]*")


class ReviewNeeded(ValueError):
    pass


@dataclass
class Paper:
    path: Path
    before: str
    after: str | None
    title: str | None
    authors: list[str] | None
    year: int | None
    created: str
    modified: str
    heading_removed: str | None
    issues: list[str]


def split_frontmatter(text: str) -> tuple[dict, str]:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.DOTALL)
    if not match:
        raise ReviewNeeded("missing or malformed YAML front matter")
    try:
        front = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        # One old paper has a plain subtitle with an unquoted colon. Accept
        # only a simple key/value header here; the output will be valid YAML.
        front = {}
        for line in match.group(1).splitlines():
            field = re.fullmatch(r"([A-Za-z_][\w-]*):\s*(.+)", line)
            if not field or field.group(1) in front:
                raise ReviewNeeded("old front matter is not simple key/value YAML")
            front[field.group(1)] = field.group(2)
    if not isinstance(front, dict):
        raise ReviewNeeded("front matter is not a mapping")
    return front, text[match.end() :]


def bib_block(body: str) -> str:
    header = BIB_HEADER.search(body)
    if not header:
        raise ReviewNeeded("no BibTeX section")
    section = body[header.end() :]
    fence = re.search(r"(?m)^```(?:bibtex)?[ \t]*\r?\n(.*?)^```[ \t]*(?:\r?\n|\Z)", section, re.DOTALL | re.IGNORECASE)
    if not fence:
        raise ReviewNeeded("BibTeX section has no fenced code block")
    return fence.group(1).strip()


def read_delimited(source: str, at: int, opening: str, closing: str) -> tuple[str, int]:
    if source[at] != opening:
        raise ReviewNeeded(f"expected {opening!r} in BibTeX")
    depth = 1
    i = at + 1
    start = i
    while i < len(source):
        char = source[i]
        if char == "\\" and i + 1 < len(source):
            i += 2
            continue
        if char == opening:
            depth += 1
        elif char == closing:
            depth -= 1
            if depth == 0:
                return source[start:i], i + 1
        i += 1
    raise ReviewNeeded("unclosed BibTeX value")


def parse_bibtex(source: str) -> tuple[str, dict[str, str]]:
    match = re.match(r"\A@([A-Za-z]+)\s*([{(])", source)
    if not match:
        raise ReviewNeeded("BibTeX block has no entry")
    closing = "}" if match.group(2) == "{" else ")"
    content, end = read_delimited(source, match.end() - 1, match.group(2), closing)
    if source[end:].strip():
        raise ReviewNeeded("BibTeX block has more than one entry or trailing text")
    if "," not in content:
        raise ReviewNeeded("BibTeX entry has no fields")
    citekey, rest = content.split(",", 1)
    if not citekey.strip():
        raise ReviewNeeded("BibTeX entry has no citation key")
    fields: dict[str, str] = {}
    i = 0
    while i < len(rest):
        while i < len(rest) and (rest[i].isspace() or rest[i] == ","):
            i += 1
        if i == len(rest):
            break
        name_match = FIELD_NAME.match(rest, i)
        if not name_match:
            raise ReviewNeeded(f"cannot parse BibTeX field near {rest[i:i+30]!r}")
        name = name_match.group().lower()
        i = name_match.end()
        while i < len(rest) and rest[i].isspace():
            i += 1
        if i >= len(rest) or rest[i] != "=":
            raise ReviewNeeded(f"BibTeX field {name} has no equals sign")
        i += 1
        while i < len(rest) and rest[i].isspace():
            i += 1
        if i >= len(rest):
            raise ReviewNeeded(f"BibTeX field {name} has no value")
        if rest[i] == "{":
            value, i = read_delimited(rest, i, "{", "}")
        elif rest[i] == '"':
            value, i = read_delimited(rest, i, '"', '"')
        else:
            start = i
            while i < len(rest) and rest[i] != ",":
                i += 1
            value = rest[start:i].strip()
        if name in fields:
            raise ReviewNeeded(f"duplicate BibTeX field {name}")
        fields[name] = value.strip()
        while i < len(rest) and rest[i].isspace():
            i += 1
        if i < len(rest) and rest[i] != ",":
            raise ReviewNeeded(f"unsupported BibTeX expression after {name}")
    return citekey.strip(), fields


ACCENTS = {
    "'": "\u0301", '"': "\u0308", "`": "\u0300", "^": "\u0302", "~": "\u0303",
    "c": "\u0327", "u": "\u0306", "v": "\u030c", "H": "\u030b", "k": "\u0328",
    ".": "\u0307", "=": "\u0304",
}
SPECIAL = {"i": "ı", "j": "ȷ", "o": "ø", "O": "Ø", "l": "ł", "L": "Ł", "dh": "ð", "DH": "Ð", "ss": "ß", "ae": "æ", "AE": "Æ"}
ACCENT_RE = re.compile(r"\\(['\"`^~cuvHk.=])\s*(?:\{(\\?[A-Za-z])\}|(\\?[A-Za-z]))")


def plain_text(value: str) -> str:
    def convert(match: re.Match[str]) -> str:
        raw = match.group(2) or match.group(3)
        base = "i" if raw == "\\i" else "j" if raw == "\\j" else raw
        return unicodedata.normalize("NFC", base + ACCENTS[match.group(1)])

    value = ACCENT_RE.sub(convert, value)
    for command, replacement in sorted(SPECIAL.items(), key=lambda x: -len(x[0])):
        value = re.sub(r"\\" + command + r"(?![A-Za-z])", replacement, value)
    value = value.replace("{", "").replace("}", "")
    if "\\" in value:
        raise ReviewNeeded(f"unconverted TeX command in {value!r}")
    return re.sub(r"\s+", " ", value).strip()


def split_outside_braces(value: str, delimiter: str) -> list[str]:
    parts: list[str] = []
    depth = 0
    start = 0
    i = 0
    while i < len(value):
        if value[i] == "\\" and i + 1 < len(value):
            i += 2
            continue
        if value[i] == "{":
            depth += 1
        elif value[i] == "}":
            depth -= 1
            if depth < 0:
                raise ReviewNeeded("unbalanced author braces")
        elif depth == 0 and value[i : i + len(delimiter)].lower() == delimiter:
            parts.append(value[start:i].strip())
            i += len(delimiter)
            start = i
            continue
        i += 1
    if depth:
        raise ReviewNeeded("unbalanced author braces")
    parts.append(value[start:].strip())
    return parts


def parse_authors(value: str) -> list[str]:
    authors = []
    for raw in split_outside_braces(value, " and "):
        parts = split_outside_braces(raw, ",")
        if len(parts) == 1:
            display = plain_text(parts[0])
        elif len(parts) == 2:
            display = f"{plain_text(parts[1])} {plain_text(parts[0])}".strip()
        elif len(parts) == 3:
            display = f"{plain_text(parts[2])} {plain_text(parts[0])}, {plain_text(parts[1])}".strip()
        else:
            raise ReviewNeeded(f"unusual author form {raw!r}")
        if not display:
            raise ReviewNeeded("empty author name")
        authors.append(display)
    return authors


def snapshot_dates() -> dict[str, str]:
    dates = {}
    for line in SNAPSHOT.read_text(encoding="utf-8-sig").splitlines():
        if not line.startswith("| paper/"):
            continue
        cells = [part.strip() for part in line.split("|")[1:-1]]
        if len(cells) >= 2:
            dates[cells[0]] = cells[1][:10]
    return dates


def git_dates(path: Path) -> tuple[str, str]:
    rel = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "log", "--follow", "--reverse", "--format=%cI", "--", rel],
        cwd=ROOT, capture_output=True, text=True, check=True,
    )
    dates = [line for line in result.stdout.splitlines() if line.strip()]
    if not dates:
        raise ReviewNeeded("no Git creation date")
    return dates[0][:10], dates[-1][:10]


def find_h1(body: str) -> list[tuple[int, str, str]]:
    headings = []
    fenced = False
    for i, line in enumerate(body.splitlines(keepends=True)):
        if re.match(r"^\s*(```|~~~)", line):
            fenced = not fenced
        if not fenced:
            match = H1.match(line.rstrip("\r\n"))
            if match:
                headings.append((i, line, match.group(1)))
    return headings


def normalized(value: str) -> str:
    return "".join(char for char in unicodedata.normalize("NFKD", value).casefold() if char.isalnum())


def zotero_keys(value: str | list[str] | None) -> tuple[str, ...]:
    if value is None:
        return ()
    keys = [value] if isinstance(value, str) else value
    if not isinstance(keys, list) or not keys or any(
        not isinstance(key, str) or not re.fullmatch(r"[A-Z0-9]{8}", key) for key in keys
    ):
        raise ReviewNeeded("zotero_key must be an eight-character item key or a nonempty list of item keys")
    if len(keys) != len(set(keys)):
        raise ReviewNeeded("zotero_key contains repeated keys")
    return tuple(keys)


def yaml_front(title: str, authors: list[str], year: int, created: str, modified: str, tags: list[str] | None,
               zotero_key: str | list[str] | None = None) -> str:
    lines = ["---", "layout: bib", "title: " + json.dumps(title, ensure_ascii=False), "pub_authors:"]
    lines.extend("  - " + json.dumps(author, ensure_ascii=False) for author in authors)
    lines.extend([f"pub_year: {year}", f"date: {created}", f"modified: {modified}"])
    if tags:
        lines.append("tags:")
        lines.extend("  - " + json.dumps(tag, ensure_ascii=False) for tag in tags)
    zotero_keys(zotero_key)
    if isinstance(zotero_key, str):
        lines.append("zotero_key: " + json.dumps(zotero_key))
    elif zotero_key is not None:
        lines.append("zotero_key:")
        lines.extend("  - " + json.dumps(key) for key in zotero_key)
    lines.append("---")
    return "\n".join(lines) + "\n"


def load_approvals() -> dict:
    if not APPROVALS.exists():
        return {}
    data = yaml.safe_load(APPROVALS.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError("approval file must be a mapping")
    return data


def examine(path: Path, modified_dates: dict[str, str], approvals: dict) -> Paper:
    rel = path.relative_to(ROOT).as_posix()
    before = path.read_bytes().decode("utf-8-sig")
    issues: list[str] = []
    title = None
    authors = None
    year = None
    heading_removed = None
    after = None
    created = ""
    modified = modified_dates.get(rel, "")
    try:
        front, body = split_frontmatter(before)
        extra = set(front) - ALLOWED_OLD_FIELDS
        if extra:
            raise ReviewNeeded("unexpected frontmatter fields: " + ", ".join(sorted(extra)))
        tags = front.get("tags")
        if tags is not None and (not isinstance(tags, list) or any(not isinstance(tag, str) for tag in tags)):
            raise ReviewNeeded("tags must be a list of strings")
        approval = approvals.get(rel, {})
        if not isinstance(approval, dict):
            raise ReviewNeeded("approval must be a mapping")
        try:
            _, fields = parse_bibtex(bib_block(body))
            for key in ("title", "author", "year"):
                if not fields.get(key):
                    raise ReviewNeeded(f"BibTeX entry has no {key}")
            title = plain_text(fields["title"])
            authors = parse_authors(fields["author"])
            if not re.fullmatch(r"\d{4}", fields["year"]):
                raise ReviewNeeded("BibTeX year is not four digits")
            year = int(fields["year"])
        except ReviewNeeded:
            manual = approval.get("metadata")
            if not manual:
                raise
            title = manual.get("title")
            authors = manual.get("pub_authors")
            year = manual.get("pub_year")
            if not isinstance(title, str) or not title or not isinstance(authors, list) or not authors or not isinstance(year, int):
                raise ReviewNeeded("approved manual metadata is incomplete")
        first_commit, last_commit = git_dates(path)
        created = str(front.get("date") or first_commit)
        modified = str(front.get("modified") or modified or last_commit)
        for label, value in (("date", created), ("modified", modified)):
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                raise ReviewNeeded(f"{label} is not YYYY-MM-DD")
        headings = find_h1(body)
        if len(headings) > 1:
            raise ReviewNeeded("multiple level-one headings")
        new_body = body
        if headings:
            index, line, heading = headings[0]
            if normalized(heading) != normalized(title):
                approved_heading = approval.get("heading")
                if approved_heading != heading or approval.get("use_bibtex_title") is not True:
                    raise ReviewNeeded(f"heading differs from publication title: {heading!r} vs {title!r}")
            body_lines = body.splitlines(keepends=True)
            heading_removed = body_lines.pop(index).rstrip("\r\n")
            new_body = "".join(body_lines)
        after = yaml_front(title, authors, year, created, modified, tags, front.get("zotero_key")) + new_body
    except (ReviewNeeded, UnicodeDecodeError, subprocess.CalledProcessError) as exc:
        issues.append(str(exc))
    return Paper(path, before, after, title, authors, year, created, modified, heading_removed, issues)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("check", "apply"))
    args = parser.parse_args()
    dates = snapshot_dates()
    approvals = load_approvals()
    files = sorted(p for p in PAPERS.glob("*.md") if "template" not in p.name.lower())
    counts = Counter()
    for path in files:
        paper = examine(path, dates, approvals)
        rel = path.relative_to(ROOT).as_posix()
        if paper.issues:
            counts["review"] += 1
            print(f"REVIEW {rel}: {'; '.join(paper.issues)}")
            continue
        if paper.after == paper.before:
            counts["ok"] += 1
            continue
        counts["ready"] += 1
        print(f"{'APPLY' if args.mode == 'apply' else 'READY'} {rel}: {paper.title!r}; {paper.year}; {len(paper.authors or [])} authors; page {paper.created}, modified {paper.modified}")
        if paper.heading_removed is not None:
            print(f"  REMOVE {rel}: {paper.heading_removed}")
        if args.mode == "apply":
            path.write_bytes(paper.after.encode("utf-8"))
            counts["changed"] += 1
    print(f"Summary: {len(files)} pages; {counts['ok']} already standard; {counts['ready']} ready; {counts['review']} need review; {counts['changed']} changed")
    if args.mode == "check":
        return 1 if counts["review"] or counts["ready"] else 0
    return 1 if counts["review"] else 0


if __name__ == "__main__":
    sys.exit(main())
