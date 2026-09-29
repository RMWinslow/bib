---
name: bib-paper-audit
description: Check and repair front matter in this bibliography repository's paper pages with the deterministic paper-standardization script. Use for paper-page audits, metadata cleanup, or format checks; Zotero matching and other entry types need separate work.
---

# Paper-page audit

Work from the repository root. Run `python scripts/standardize_papers.py check`. It scans the 194 non-template `paper/*.md` files and compares each page's front matter with its fenced BibTeX entry. It does not query Zotero. The script needs Python with PyYAML (`import yaml`) and Git. Keep the script at `scripts/standardize_papers.py`; this skill is the workflow guide, not a second copy of the code.

## Page format

Each paper page has `layout: bib`, `title`, `pub_authors` (a YAML list of full names), `pub_year`, `date`, and `modified`; `tags` and `zotero_key` are optional. The title, authors, and publication year come from BibTeX in the body. The dates describe this bibliography page, not the publication. Keep the BibTeX code block, abstracts, links, lower-level headings, and reading notes in the body. The `bib` layout displays the title, so a separate level-one title heading should not remain. `_config.yml` gives `paper/` the `Papers` parent and `nav_exclude: true`; individual pages stay in site search but leave the large sidebar.


`zotero_key` stores a native item key in Robert's personal Zotero library, not a Better BibTeX citation key. Use a quoted string for one item or a YAML list of quoted strings for multiple items. Omit it when no match is established. Preserve it during metadata cleanup; the audit checks its form and keeps it when rewriting front matter. Multiple pages may share a key, as the two Fisher version pages do.

## Run and review

1. Run `python scripts/standardize_papers.py check`. Exit code 0 means all scanned pages match the current format. Exit code 1 means at least one `READY` or `REVIEW` case. `READY` prints proposed title, year, author count, page dates, and the exact level-one heading line it would remove. `REVIEW` means the script did not prepare a change for that page.
2. Inspect each `READY` change before applying it, especially the proposed title, names, dates, tags, and `REMOVE` line. Review each `REVIEW` page against its BibTeX and, when needed, a reliable publication source. Do not infer a publication from a filename or citation key. If a heading differs from the BibTeX title and the BibTeX title is right, record that exact heading with `use_bibtex_title: true` in `_planning/paper-title-approvals.yml`; the script then permits its removal. An approved metadata exception is possible when BibTeX is missing, but record the source and reason. Prefer a correct BibTeX entry when one is available.
3. Once the proposed edits are sound, run `python scripts/standardize_papers.py apply`. It writes front matter and removes only approved level-one title headings. It prints the exact removed line. It skips unresolved `REVIEW` cases and exits 1 if any remain. Inspect the diff, run `check` again, and build the Jekyll site when layout or rendering changes warrant it. Verify that the BibTeX block and notes remain intact and that a page has one visible title.

The script converts supported TeX accents in BibTeX names to Unicode. An unknown TeX command or unusual author form becomes `REVIEW`; inspect and fix it rather than silently stripping it. A terminal's character display can differ from the UTF-8 file contents.

## Dates and limits

The first migration estimated `date` from the earliest Git change and `modified` from `_planning/file-modification-index-2026-09-27.md`, saved before the bulk edit. Both estimate **page-edit** dates. The script keeps valid existing dates, so migration runs do not advance `modified`. When a person makes a meaningful later page edit, set `modified` to that edit date. New, uncommitted pages have no Git creation date and may need script changes or a separate import flow before this command can handle them.

This command checks paper pages only. It does not cover `article/`, `book/`, `report/`, or `data/`, validate a publication against an external source, compare Zotero collections, or reconcile citation-key differences. For import preparation, run `python scripts/audit_zotero_paper_overlap.py --saved-keys`: it compares live `processed / read` item keys with saved front matter without loading Better BibTeX or doing fuzzy matching. Skip already represented items. An unlinked item still needs review before import. Use DOI or another stable identifier, then titles and author overlap, to establish new links; a changed year alone does not reject a match. The attachment-only cases in `_planning/zotero-false-negative-review-2026-09-29.md` need separate handling because the containing records describe other papers or a whole book. See `_planning/bibliography-work-plan.md` for that pending work.
