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
  zotero/              # 1 entry from Zotero Better Notes integration experiment
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

## Redesign goals (2026-03-23)

The user wants to revisit and redesign this repo. Key motivations:

1. **Zotero integration:** The user likes Zotero's PDF reader and note-taking but dislikes its opaque storage (hashed folders + SQLite). The goal is to use Markdown files as the durable, legible layer — resilient to breaking software updates — while leveraging Zotero's strengths for PDF annotation and metadata management.

2. **Local PDF links:** The user has PDFs synced via Google Drive across three computers. Bibliography entries should link to the corresponding local PDF when viewed on one of those machines.

3. **Structured entry format:** A new `bibentry` layout with rich YAML frontmatter (citekey, title, authors, year, tags, doi, pdf path, etc.) so that entries are easy to create and parse for both humans and AI agents.

4. **Collection pages:** A `collection` layout that auto-lists entries matching specified tags, replacing the current stub. Manual curation with optional auto-generation.

5. **Navigation cleanup:** Eliminate the "Other" catch-all; reorganize by type or lean on tag-based collections for discovery.

### Open design questions (awaiting user input)

- [ ] Two-layout structure (bibentry + collection) — confirmed or needs revision?
- [ ] PDF linking approach: localhost-detection JS (option D) or something else?
- [ ] Author format in frontmatter: compact "Last F" vs. full names vs. structured objects?
- [ ] Tags: free-form or controlled vocabulary?
- [ ] Break up "Other" nav group, or is sidebar hierarchy low-priority vs. tag-based collections?
- [ ] Migration strategy: bulk script or incremental as entries are touched?

### Earlier TODOs (pre-redesign)

- [ ] Fix `zotero/lou2013accurate.md` parent field (lowercase "papers" → "Papers") or migrate to new structure.
- [ ] Decide fate of `collections/test_collection_page.md`.
- [ ] Resolve inconsistent `layout: post` usage (4 of ~230 entries).
