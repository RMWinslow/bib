---
name: zotero-paper-import
description: Import unlinked papers from Robert's Zotero processed / read collection into this bibliography repository. Use the deterministic saved-key inventory, prepare one reviewed Markdown draft, and preserve Zotero notes and highlights.
---

# Import read Zotero papers

Created by OpenAI Codex for Robert Winslow's September 2026 bibliography import. Use `scripts/import_zotero_papers.py` for the tested create-and-skip workflow. Non-article follow-ups are listed in `_planning/zotero-non-article-imports.md`.

## Inventory

Run from the repository root with Zotero open and its local API enabled:

```powershell
python -X utf8 scripts/import_zotero_papers.py list
```

The script reads the live collection named `processed / read`. It excludes attachments and notes from the work list, and reads front matter in `paper`, `article`, `book`, `report`, `data`, and `zotero`. It compares native Zotero item keys with scalar or list `zotero_key` fields. Skip linked items without auditing their content. These keys belong to Robert's personal library; they are not Better BibTeX citation keys.

An unlinked record is a review candidate. It can be another version of an existing paper. For the selected candidate, check its title, authors, DOI, and attachments against likely existing pages. Do not repeat a whole-repo fuzzy audit. Some records contain misfiled attachments or describe a whole book; inspect the selected record when identity is uncertain. Resolve an uncertain identity before creating a page. Do not reject a match solely because years differ.

## Prepare one draft

Use the native Zotero BibTeX export as the starting citation. Check publication facts against a publisher or DOI source before claiming verification. No OpenAlex key is needed. The script retains ordinary citation fields and removes export fields such as local file paths, abstracts, and access dates from the copyable BibTeX. It validates required metadata and stops on unsupported TeX names. If metadata needs correction, record the source and keep the BibTeX and YAML consistent; do not silently invent missing fields.

Single-paper command (substitute the native item key and new output path):

```powershell
python -X utf8 scripts/import_zotero_papers.py draft ITEMKEY --out paper/CITATIONKEY.md
```

`--verified-against` records a source the agent has already checked; the script does not verify that page. Optional `--link 'Working paper=https://...'` adds an individually verified public link. Default DOI, paper-page, and PDF links come from the Zotero record; check them during review. Keep the DOI label. Name the source of the other links: for example, `AEA paper page` and `AEA PDF`. The script recognizes AEA hosts and otherwise uses the actual hostname. A reviewer can replace a hostname with a verified publisher or author name; do not guess the source from the paper title. Add author-hosted versions only when found and verified. Do not guess URLs or expose local file links.

Python needs PyYAML and the adjacent `standardize_papers.py` module. HTML notes require Pandoc on PATH. The script only reads Zotero. It refuses existing draft/snapshot paths and a conflicting paper filename.

## Page content and provenance

- Use `layout: bib`, publication `title`, full-name `pub_authors`, `pub_year`, page `date` and `modified`, source `tags` when present, and native `zotero_key`. New page dates are the page's creation date, not publication or Zotero dates. If a staged draft is adopted on another day, update its page dates to the adoption date.
- Use the citation key from the export as the filename. Do not infer one from the title. Keep a fenced BibTeX block under `## BibTeX`; no BibTeX in YAML and no duplicate level-one title.
- Keep the abstract under `## Abstract`. Keep notes under `## Notes and Excerpts`. An empty section heading stays inside an HTML comment.
- Copy quotations and Robert's comments without summarizing or improving their wording. Highlights become blockquotes with the page label inside the quote, on its own final paragraph. Separate visible excerpt blocks with horizontal rules. Put Robert's annotation comment after its quote and page label without a `My comment` label. Separate Zotero notes retain their own section and rich-text structure where Markdown supports it.
- Keep every excerpt visible in source order, regardless of color or attached commentary. For non-yellow quotes, put a Kramdown class marker such as `{: .zotero-green}` immediately after the quote. Preserve the exact source color in the hidden annotation provenance comment. Yellow uses ordinary quote styling. The stylesheet `assets/css/zotero-excerpts.css`, loaded by `_layouts/bib.html`, supplies muted Solarized accents for the standard non-yellow colors; unknown colors use the neutral `zotero-other` class. Do not infer future-reading status from green or move excerpts to a hidden section.
- Hidden comments retain the source item, note, attachment, and annotation keys. Optional JSON snapshots can preserve fetched data during debugging, but are not required for ordinary imports. Never present an abstract or an agent summary as Robert's own note.

Annotations must be fetched explicitly with `/items/<attachment-key>/children?itemType=annotation`; the default children response omits them. The script does this for each attachment and sorts by attachment and annotation order. It stops for unsupported graphical annotations or rich notes with embedded citations/annotations/images, so content is not silently lost or duplicated. Review these cases separately. Do not edit Zotero to make an import succeed without authorization.

## Check and adopt

Run the tests:

```powershell
python -X utf8 -m unittest discover -s tests -p test_import_zotero_papers.py -v
```

Compare the draft with the fetched Zotero data (or an optional source snapshot): metadata, tags, public links, number and exact text of highlights, page labels, comments, and separate notes. The first pilot retains all 11 highlights visibly, including three green quotes, plus Robert's one attached comment. There are no separate notes. Its citation was checked against the AEA page. Tests also cover empty sections, rich-text notes, explicit annotation requests, pagination, refusal to overwrite, and skipping existing links before content requests.

Robert approved the rendered format and authorized batch import on 2026-09-29. For later approved imports, copy the reviewed draft into `paper/<citation-key>.md` without overwriting any existing file or deleting the staged source. Check the adopted page with the `bib-paper-audit` procedure and run the inventory again: its native key must now be skipped. Existing linked pages are outside this import pass. Keep non-paper records and uncertain matches in the review report.

## Tags on existing pages

New imports retain Zotero tags automatically. Ordinary imports still skip linked pages. On 2026-09-29 Robert separately requested a tag backfill: 136 existing linked pages were checked and 34 received additional tags. For another explicitly requested backfill, union tags from all saved Zotero keys with existing page tags; retain manual tags, add each exact tag only once, and change no other fields or body bytes. Do not treat the absence of a Zotero tag as permission to remove a manual tag.

## Routine imports without extra files

Omit `--snapshot` for normal imports. Snapshots are for debugging and are not the routine output format. Check the fetched source in memory and save only the Markdown page unless a specific unresolved case needs a diagnostic snapshot. Existing pilot JSON files are retained; do not create another snapshot for a formatting change. Never overwrite a linked page as part of an ordinary import. Explicitly requested format migrations must first check for manual additions and preserve them.

## Deterministic batch command

Run `python -X utf8 scripts/import_zotero_papers.py batch` for a read-only preview, then `python -X utf8 scripts/import_zotero_papers.py batch --apply` to create new pages. Both skip saved native keys. The batch covers journal articles, preprints, and conference papers; other Zotero types stay for separate review. It blocks existing filenames, DOI/title matches, close-title candidates, and the known misfiled Aumann-Peleg attachment. Similarity is a review trigger, not proof of identity. The reviewed Davidson-Woodbury versus Hopenhayn-Nicolini same-title exception is explicit in the script.

Metadata and links come from the native Zotero export; the batch does not claim external verification. Identical repeated DOI fields are collapsed; conflicting duplicates still stop. Unsupported content or missing fields stops only that item. Ordinary runs print a table, not per-item JSON files. Save one report if needed. The script checks quotation/comment preservation and verifies that existing pages remain byte-for-byte unchanged. A second preview must propose no further imports among the completed set.

Rich-text notes have Zotero's editor wrapper removed before Markdown conversion. Note headings are nested below the level-three Zotero-note heading, without changing words. After a batch, run the unit tests and paper audit. Books, webpages, reports, duplicate versions, missing-author cases, and misfiled attachments need separate decisions; do not silently force them into the paper format.
