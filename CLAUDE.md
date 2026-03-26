---
nav_exclude: true
search_exclude: true
---

# CLAUDE.md — bib repository

**This file should be kept up to date** as work progresses. It serves as the canonical reference for Claude sessions working in this repo.

## Project overview

This repository is a Jekyll-based bibliography tracker hosted on GitHub Pages. Each bibliographic entry is a Markdown file with YAML frontmatter, organized into directories by type. The site uses the JTD-RMW theme (a custom fork of Just the Docs) to render the entries as searchable, navigable web pages. The key trick is that JTD's Lunr.js search indexes every page into a single JSON file at build time, so the entire bibliography is full-text searchable from the browser.

- **Repository:** <https://github.com/RMWinslow/bib>
- **Author:** Robert Winslow
- **Theme:** `remote_theme: RMWinslow/JTD-RMW` (sister repo at `../JTD-RMW`)

## Directory structure

```
bib/
  _config.yml          # Jekyll config: title, remote_theme, search, math: katex
  _planning/           # Design documents and research notes (ignored by Jekyll)
  papers.md            # Nav parent page (has_children: true)
  books.md             # Nav parent page
  other.md             # Nav parent page (catch-all for articles, reports, data, etc.)
  collections.md       # Nav parent page (nav_order: 1, appears first in sidebar)
  README.md            # Brief project description and replication instructions
  paper/               # ~195 research paper entries
  article/             # ~15 article/news entries
  book/                # 6 book entries
  report/              # 6 report entries
  data/                # 6 dataset entries (CEX has a child page: cexdict.md)
  collections/         # 1 test collection page (search_exclude: True)
  zotero/              # 1 entry from Zotero Better Notes experiment (to be retired)
```

## Entry format

Most entries follow this pattern:

```markdown
---
parent: Papers          # Must match a nav parent page title exactly (case-sensitive)
---

# Paper Title

[Link to PDF or source](https://...)

## BibTeX
\```
@article{citekey, ...}
\```

## Notes and Excerpts
Personal reading notes, blockquotes, math, cross-references, etc.
```

- Templates exist at `article/__template.md` and `data/__template.md`.
- A few entries use `layout: post` (which adds title/subtitle header group and optional TOC). The vast majority use the default layout.
- The `data/cex.md` page has `has_children: true` and serves as a parent for `data/cexdict.md` (which uses `parent: BLS CEX`).

## Navigation hierarchy

JTD-RMW builds the sidebar from `parent` frontmatter values. The top-level parent pages are defined by the root `.md` files:

| Page | Title | Notes |
|------|-------|-------|
| `collections.md` | Collections | nav_order: 1 (pinned to top) |
| `papers.md` | Papers | Largest section (~195 children) |
| `books.md` | Books | 6 children |
| `other.md` | Other | Catch-all: articles, reports, data, etc. |

## Theme: JTD-RMW

The sister repo `../JTD-RMW` is a customized fork of Just the Docs. Key features used by this site:

- **Lunr.js search** — client-side full-text search across all pages, split at h2 boundaries
- **KaTeX math** — enabled site-wide via `math: katex` in `_config.yml`; supports `$...$` inline and `$$...$$` display
- **`<details>`-based sidebar nav** — supports up to 4 levels of nesting via `parent`, `grand_parent`, `great_grand_parent`
- **`layout: post`** — adds title/subtitle `<hgroup>`, date line, and optional collapsible TOC (`toc: true`)
- **`search_exclude: True`** — hides a page from the search index (used by collection pages)
- **Responsive design** — hamburger menu on narrow viewports, scrollable table wrappers
- **Dark mode** — automatic via `prefers-color-scheme` CSS media query

## Configuration notes

The `_config.yml` is minimal (11 lines):
- `compress_html: ignore: envs: all` effectively **disables** HTML compression.
- No Gemfile exists; the site relies entirely on GitHub Pages' built-in Jekyll and the remote theme.
- No custom plugins.

## Known issues and observations

1. **Lowercase parent in zotero entry:** `zotero/lou2013accurate.md` has `parent: papers` (lowercase). The nav parent page is titled `Papers` (capitalized). JTD-RMW's nav matching is case-sensitive, so this entry may be orphaned in the sidebar. This was likely an artifact of the Zotero Better Notes integration experiment.

2. **Zotero integration is experimental:** Recent commits (2025-09-27) tested the Zotero Better Notes plugin. The experiment concluded that the plugin requires either a YAML `citekey:` field or an `@citekey` filename prefix. The `zotero/` directory currently has only one entry.

3. **Collections section is a stub:** Only one test page exists (`collections/test_collection_page.md`), and it uses `search_exclude: True`.

4. **Inconsistent use of `layout: post`:** Only 4 out of ~230 entries explicitly set `layout: post`. The rest use the default layout, which means they lack the title/subtitle header group and the optional TOC feature.

## Redesign (2026-03-23)

The user wants to redesign this repo. Core motivations: Zotero's opaque storage (hashed folders + SQLite) is fragile; Markdown files are the durable, legible, version-controlled alternative. The goal is to leverage Zotero for PDF annotation and metadata management while using this repo as the permanent record.

### Confirmed design decisions

- **Layout name:** `bib` (not `bibentry` — shorter, unambiguous in context, matches repo name).
- **Two layouts:** `bib` for individual entries, `collection` for curated/auto-generated topic pages.
- **Authors in frontmatter:** Full names (e.g., `["Yin Lou", "Rich Caruana"]`).
- **Tags:** Free-form. LLMs make post-hoc cleanup easy if tag drift becomes a problem.
- **Navigation:** Individual `bib` entries should be `nav_exclude: true` — the current sidebar with ~195 papers is unusable. Entries are discoverable via Lunr search and collection pages. This can be set as a default in `_config.yml` per directory so entries don't need to specify it individually.
- **Local PDF linking:** Browsers block `file:///` from `https://` origins (confirmed via test). The leading approach is a custom protocol handler (`openpdf://`) registered in the Windows registry on each machine. See `_planning/local_pdf_linking.md` for full research and details. Not yet implemented.

### Proposed entry frontmatter schema

```yaml
---
layout: bib
parent: Papers

# Identity
citekey: lou2013accurate
title: "Accurate intelligible models with pairwise interactions"
authors: ["Yin Lou", "Rich Caruana", "Johannes Gehrke", "Giles Hooker"]
year: 2013

# Publication
publication: "KDD '13"
type: paper                  # paper | book | article | report | dataset

# Links
doi: "10.1145/2487575.2487579"
url: "https://dl.acm.org/doi/10.1145/2487575.2487579"
pdf: "papers/lou2013accurate.pdf"   # relative to configurable base path

# Organization
tags: [machine-learning, interpretability, GAMs]
---
```

Only `layout`, `citekey`, `title`, and `type` are required. Everything else is optional so stubs can be created quickly.

### Open questions

- [ ] Migration strategy: batched script (recommended), AI-assisted, incremental, or hybrid? See conversation notes for full pros/cons analysis.
- [ ] Navigation restructuring: break up "Other" into separate parents, or rely entirely on tag-based collections for discovery?
- [ ] `_config.yml` defaults: set `layout: bib` and `nav_exclude: true` per directory to minimize per-file frontmatter?

### Cleanup TODOs

- [x] ~~Remove `test_file_links.html`~~ (done 2026-03-24, confirmed `file:///` is blocked)
- [ ] Retire `zotero/` directory — move `lou2013accurate.md` to `paper/` with new frontmatter (the `citekey` field is now standard on every entry).
- [ ] Remove `collections/test_collection_page.md` or replace with a real collection page once the `collection` layout exists.
- [ ] Fix the 4 entries with `layout: post` to use `layout: bib` once the layout is created.
- [ ] Add a "messy personal notes" disclaimer banner to the `bib` layout. The banner should be visible by default (for anyone who finds a page via Google) but hideable via a Jekyll environment variable or site config flag, so the user can suppress it locally.

### Planning documents

- `_planning/local_pdf_linking.md` — Research on linking to local PDFs from GitHub Pages. Custom protocol handler (`openpdf://`) is the leading approach.
- `_planning/zotero_integration.md` — Full inventory of the local Zotero installation (351 items, 508 annotations, 5 plugins), overlap analysis with bib repo (93 shared, 132 bib-only, 258 Zotero-only), and four integration approaches (Better Notes sync, direct DB reader, BibTeX bridge, hybrid).
