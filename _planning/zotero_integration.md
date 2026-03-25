# Zotero integration research

Research conducted 2026-03-24 on the state of the local Zotero installation and how it relates to the bib repo.

## Zotero data location

The Zotero data directory is at `C:\Users\rober\Zotero\`. The SQLite database (`zotero.sqlite`) is readable from Python using `sqlite3` in immutable mode (`?immutable=1` URI parameter), which works even while Zotero is running. This is read-only and does not acquire locks.

```python
import sqlite3
conn = sqlite3.connect('file:///c:/Users/rober/Zotero/zotero.sqlite?immutable=1', uri=True)
```

## Library contents (as of 2026-03-24)

| What | Count |
|------|-------|
| Substantive items (papers, books, etc.) | 351 |
| PDF attachments | 384 |
| HTML snapshot attachments | 61 |
| Annotations (highlights/comments on PDFs) | 508 across 41 papers |
| Standalone notes | 16 |
| Collections | 6 (largest: "processed / read" with 215 items) |
| Distinct tags | ~60 |
| BibTeX auto-export entries | 351 |

## Installed plugins

| Plugin | Version | Status | Artifacts |
|--------|---------|--------|-----------|
| Better BibTeX | 9.0.10 | Active | Auto-exports `My Library (Zotero bibtex autoexport).bib` (~5,300 lines); generates citekeys; `better-bibtex/` folder |
| MarkDB-Connect | 0.1.8 | Active | Links Zotero items to external Markdown files by matching citekeys to filenames in a configured directory |
| Linter for Zotero | 3.0.3 | Active | No file artifacts; formats/normalizes metadata in-place |
| Better Notes | 3.0.3 | **Disabled** | Config remnants in prefs.js (see below) |
| DOI Manager | 1.5.0 | **Disabled** | No artifacts when disabled |

## Better Notes: what it does and why it matters

### How it integrates with Zotero

Better Notes enhances Zotero's built-in note system with:

1. **Workspace notes** — Standalone notes that act as knowledge hubs, aggregating highlights and notes from across multiple papers into a single structured document (like a living literature review).

2. **Annotation → Note pipeline** — "Quick Note" converts a PDF highlight + comment into a formatted note entry with one click. Templates control the formatting.

3. **Templates** — JavaScript snippets with access to the Zotero API. They can pull metadata from parent items, format annotations, generate YAML frontmatter, and control export filenames.

4. **Bidirectional links** — Notes can link to other notes and items, with hover-preview. Uses Zotero's standard relation system.

5. **Markdown sync** — The key feature for the bib repo. Better Notes can:
   - Export a Zotero note to a `.md` file at a specified path
   - Auto-sync: changes in Zotero propagate to the file (and optionally vice versa)
   - Templates control the YAML header, filename, and content format
   - Sync triggers when the note editor closes and on a configurable timer

### Intended workflow

1. Read a paper in Zotero's PDF reader, highlighting key passages
2. Quick Note each highlight into a structured note (template-formatted)
3. Link notes together across papers
4. Workspace note aggregates insights into a coherent narrative
5. Markdown sync keeps external copies in sync

The value proposition: stay in Zotero for reading and annotating, but get your knowledge out into portable Markdown automatically.

### Remnants in prefs.js

The plugin is disabled but left configuration:

- **Two sync targets were configured:**
  - Item 27 → synced to `I:\My Drive\zotero papers read\` (test file)
  - Item 29 → synced to `C:\Users\rober\Documents\GitHub\bib\paper\` as `lou2013accurate.md` (the experiment visible in git history)

- **Export settings:** markdown format, auto-sync enabled, YAML header enabled, auto-filename enabled, link mode standalone.

- **Templates in prefs:** `[ExportMDFileNameV2]`, `[ExportMDFileHeaderV2]`, `[ExportMDFileContent]`, `[QuickNoteV5]`, `[QuickInsertV3]`, `[QuickImportV2]`.

- **No database remnants** — Better Notes did not leave data in the SQLite tables beyond standard Zotero notes.

### Why it was disabled

Inferred from git history (September 2025): the sync was tested with `lou2013accurate.md`, but the citekey/filename conventions needed adjustment, and the exported format didn't map cleanly to the bib repo's existing entry structure (BibTeX blocks, manual notes, specific frontmatter). Better Notes wants to own the note content and sync it outward, but the bib repo entries have a different structure.

## Attachment storage

Zotero uses two storage patterns:

- **`storage:filename.pdf`** (210 files) — stored in Zotero's hash-named subdirectories under `C:\Users\rober\Zotero\storage\HASHCODE\`. These are opaque.
- **`attachments:filename.pdf`** (231 files) — linked files relative to a base directory configured in Zotero's preferences. The base directory is likely a Google Drive folder (possibly `I:\My Drive\zotero papers read\` or `U:\My Drive\zotero papers read\` — drive letter has changed over time).

The BibTeX auto-export includes `file` fields with full paths, showing both patterns:
- `U:\My Drive\zotero papers read\filename.pdf` (Google Drive, U: drive)
- `C:\Users\rober\Zotero\storage\HASHCODE\filename.pdf` (local storage)

**Note:** The Google Drive mount letter has changed over time (references to both `I:` and `U:` drives exist in the config). This needs to be checked — which letter is current on this machine?

## Bib repo vs. Zotero overlap

| | Count |
|--|-------|
| In both (matched by citekey to filename) | 93 |
| Bib repo only (no Zotero entry) | 132 |
| Zotero only (no bib repo page) | 258 |

The two systems have diverged significantly. Only about 27% of bib repo entries match a Zotero citekey. Zotero has 258 items that have never been added to the bib repo.

## Approaches to integration going forward

### Option A: Better Notes sync (re-enable plugin)

Re-enable Better Notes, write custom templates that generate frontmatter matching the new `bib` schema, and use auto-sync to push Zotero notes into the bib repo.

- Pros: Bidirectional sync; live updates; annotations flow through automatically.
- Cons: Plugin dependency; Better Notes controls the note format; fragile if the plugin updates or breaks; the plugin was already disabled once due to format mismatch.

### Option B: Direct database reader (standalone script)

Write a Python script that reads `zotero.sqlite` (immutable mode), extracts items, metadata, annotations, and notes, and generates/updates Markdown files in the bib repo.

- Pros: No plugin dependency; full control over output format; can run as a one-off or on a schedule; resilient to Zotero plugin changes.
- Cons: One-way only (Zotero → bib repo); no live sync; need to handle merge/update logic for entries that already have manual notes.

### Option C: BibTeX export as bridge

Use Better BibTeX's auto-export (already active) as the data source. Parse the `.bib` file to generate/update bib repo entries.

- Pros: Simpler than DB access; BibTeX format is stable and well-understood; Better BibTeX is mature and actively maintained.
- Cons: BibTeX doesn't contain annotations, notes, or highlights — only bibliographic metadata. Would need to be combined with DB access for the rich content.

### Option D: Hybrid

Use the BibTeX export for metadata and the DB for annotations/notes. A script reads both sources and generates complete bib repo entries. Better Notes can optionally be re-enabled for its workspace/linking features without relying on its sync.

- Pros: Best of both worlds; metadata from a stable format, rich content from the database; no dependency on Better Notes sync working correctly.
- Cons: More complex script; two data sources to coordinate.

## Next steps

These are recorded in CLAUDE.md. The immediate priority is finalizing the `bib` layout in JTD-RMW and the entry frontmatter schema before tackling migration or Zotero sync tooling.
