# Bibliography work plan

Recorded: 2026-09-27. Status: the paper-page standardization in Task 2 is implemented; Zotero edits and Task 1 have not begun.

This plan covers the personal bibliography repository and its link to Zotero reading status. It does not cover HIERARCHRAG, graduate-student notes, or JEP ingestion.

## Shared prerequisite: establish durable item identity

The filename or BibTeX citation key in a bib page can differ from the key that Better BibTeX now supplies. A missing key match therefore does not prove that a work is absent. Use Zotero's stable **item key** as the lasting link between a Zotero record and a bib page. Keep the citation key as a separate field for citations and filenames; do not treat it as the sole identity.

For existing pages, match in this order: an already recorded Zotero item key; exact DOI or another stable publication identifier; exact normalized title with author and year checks; then a short list of possible matches for review. Never accept an uncertain title match automatically. Record each approved link in the bib page, or in a checked-in crosswalk until the page format is settled. After that, later runs compare stable item keys and need no fuzzy rematch. Detect two pages linked to one Zotero item, or two Zotero items linked to one page, as conflicts.

The current Better BibTeX export lists citation keys for the whole library, while Zotero's database lists membership in `processed / read` by item key. Better BibTeX documents a read-only `item.citationkey` lookup from item keys; its local service must be available to use that route. Do not guess a key from title text if that lookup fails. A separate collection auto-export is another possible route to test.

## Task 1: bring read Zotero items into bib

**Goal:** A deterministic inventory identifies items in `processed / read` that do not yet have a linked bib page. An agent then creates only the missing pages.

**Plan:**

1. Build a small read-only inventory command. Query Zotero's `processed / read` collection, exclude child attachments and notes, fetch exact Better BibTeX citation keys, and compare stable item keys with linked bib pages.
2. Output `present`, `missing`, and `needs review` groups with Zotero item key, citation key, title, creators, year, DOI, and existing bib path when known. Report stale or unavailable sources instead of silently treating them as current.
3. For each truly missing item, let an agent inspect the Zotero record, notes, annotations, and source as needed, then draft a bib page. Distinguish Robert's reading notes from abstracts, imported annotations, and agent summaries. Verify bibliographic facts before writing them.
4. Add the stable Zotero item key to each new page. Re-run the inventory and check that the item moves from `missing` to `present`.

**Open decisions:** Whether every `processed / read` item deserves a page; the minimum useful page content; whether the script should write a report file or print it; whether the local Better BibTeX service or a collection export is the better key source.

## Task 2: remediate and standardize existing bib pages

**Goal:** Preserve the existing notes while making page identity and metadata consistent enough for reliable search, linking, and later maintenance.

**Plan:**

1. The paper-page frontmatter and BibTeX audit is complete. The 2026-09-27 file modification snapshot was saved before bulk edits.
2. Resolve each existing page against Zotero using the shared identity procedure. Put uncertain, missing, and duplicate links in a review list. Record approved Zotero item keys so the same ambiguity is not paid for again. This remains open.
3. The small paper-page format is implemented: `layout: bib`, `title` (publication title), `pub_authors`, `pub_year`, `date` (bib page creation), `modified` (last meaningful bib page edit), and optional `tags`. The BibTeX sections and other reading-note body text were preserved; 189 matching or reviewed H1 title lines were removed so the layout displays each title once. The durable Zotero item-key mapping remains planned for a separate checked-in crosswalk. Make `processed / read` collection membership the reading-status source for Zotero-linked items rather than requiring another field in each bib page.
4. The 194 paper pages were migrated and checked. The remaining article, book, report, and data pages have not been standardized. A local Jekyll build with the theme files verified sample titles, dates, breadcrumbs, sidebar behavior, and local search.
5. When the workflow is stable, install a repository-local skill that tells agents how to run the deterministic inventory and how to draft or repair individual pages. Keep matching and validation logic in scripts, not in repeated LLM instructions.

**Agreed direction:** Import Zotero tags when creating new pages and allow manual tags in bib. Hide individual entries from the sidebar with `nav_exclude: true`, preferably through directory defaults in `_config.yml`. Keep entries searchable in the site's own search. Prevent search-engine indexing of the entire bibliography site through a site-wide robots meta tag in the site's head include; verify the generated HTML when implemented. This has not been implemented yet. Local PDF links and custom protocol handling remain wishlist work, outside the current cleanup.

**Open decisions:** How to treat bib-only pages; whether to rename files to current Better BibTeX keys; exact historical dates where Git gives only an approximate answer; how to show a page title without duplicating existing body headings; whether to use a personal-notes notice.

## Order of work

Start with a small audit and identity-linking pilot from Task 2. That will settle the matching rule and page format needed by Task 1. Then build and test the inventory command. Expand either task only after the pilot demonstrates that existing notes and links remain intact.

The active pester remains unresolved until Robert explicitly says it is resolved.
