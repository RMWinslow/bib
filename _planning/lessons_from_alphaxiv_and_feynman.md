# Lessons from AlphaXiv and Feynman for Bib Design

> Generated 2026-03-27. Based on hands-on evaluation of the `alpha-hub` CLI,
> the `alphaxiv-skill` Python wrapper, and 10 Feynman research skills (deep-research,
> literature-review, peer-review, paper-writing, replication, etc.).

## Context

Robert is building a bespoke citation management system using Markdown files with
YAML frontmatter, version-controlled in Git and rendered via Jekyll. The system
prioritizes human-readable artifacts, durability, and searchability. This document
identifies design patterns from AlphaXiv's tooling and Feynman's research workflows
that are relevant to that project.

---

## 1. Annotation Storage: One File Per Paper, Flat Directory

**What alpha-hub does:** Annotations are stored as individual JSON files in
`~/.ahub/annotations/`, keyed by arXiv ID. Each file contains just `{id, note, updatedAt}`.
The `alpha get` command automatically surfaces any existing annotation alongside the
paper content.

**Lesson for bib:** This is essentially what bib already does — one Markdown file per
paper, keyed by citekey. The important pattern is the *automatic surfacing* behavior:
when an agent or script retrieves a paper, any prior notes should come along for free.
For bib, this could mean that any tool that looks up a citekey should also return the
"Notes and Excerpts" section from the corresponding Markdown file.

**Difference worth preserving:** alpha-hub's annotations are opaque JSON blobs with
a single `note` string. Bib's Markdown files are richer — they have structured sections
(BibTeX, abstract, notes), support math, and are human-readable in a browser. This is
a genuine advantage over alpha-hub's approach.

---

## 2. Structured Metadata in Frontmatter vs. Inline

**What alpha-hub does:** Paper metadata (title, authors, date, abstract, arXiv ID) comes
from the AlphaXiv API. The CLI displays it in a structured format but does not store it
locally — only annotations are persisted.

**What the alphaxiv-skill adds:** The `metadata` command returns structured fields
(title, arXiv ID, version, publication date, topics, authors, institutions, GitHub link)
and can output BibTeX via `--bibtex`. The `implementations` command links papers to
code repositories.

**Lesson for bib:** The proposed frontmatter redesign (citekey, title, authors, year,
publication, doi, url, pdf, tags) captures the right metadata. Two additions worth
considering from the alphaxiv-skill's data model:

- **`institutions`** — The alphaxiv-skill returns author affiliations. These are useful
  for understanding a paper's provenance and could be stored as an optional frontmatter
  field (e.g., `institutions: ["Harvard Kennedy School", "MIT Media Lab"]`).
- **`code_url`** — A dedicated field for associated code repositories, separate from
  the paper URL. The alphaxiv-skill's `implementations` command treats these as
  first-class metadata, and they are valuable for reproducibility.

---

## 3. Multiple Search Modes

**What alpha-hub does:** `alpha search` offers three modes: `semantic` (default,
meaning-based), `keyword` (exact term matching), and `agentic` (multi-turn,
broader retrieval). The Feynman researcher agent is instructed to start with broad
queries and progressively narrow.

**Lesson for bib:** Lunr.js provides keyword search over the rendered site. But for
an LLM agent working with the bib repo locally, a different search strategy makes
sense:

- **Citekey lookup** — exact match on filename (fast, deterministic).
- **Frontmatter search** — grep over YAML fields (author, year, tags, publication).
- **Full-text search** — grep over the body content (notes, abstracts, excerpts).
- **Semantic search** — would require an index; probably not worth building locally,
  but worth noting that alpha-hub delegates this to a server-side API.

The bib project could benefit from a small skill or script that wraps these search
modes and presents results in a consistent format. This would make it easier for
Claude to find relevant entries without reading every file.

---

## 4. Paper Q&A Without Full Context Ingestion

**What alpha-hub does:** `alpha ask <id> "question"` sends a question to AlphaXiv's
server, which runs RAG against the paper's PDF and returns a grounded answer. This
avoids dumping the full paper text into the LLM's context window.

**Lesson for bib:** For papers that Robert has already read and annotated, the bib
entry itself serves as a compressed summary — the "Notes and Excerpts" section is
a human-curated distillation. An agent looking up a citation can read the bib entry
(a few hundred lines) instead of the full paper (potentially thousands of lines).
This is a significant practical advantage of maintaining rich reading notes.

For papers not yet in bib, `alpha ask` remains useful as a way to interrogate a
paper before deciding whether to add it. A workflow like "alpha ask → decide if
relevant → create bib entry" could be formalized.

---

## 5. Provenance and Source Tracking

**What Feynman does:** Every research output includes a `.provenance.md` sidecar
file recording: date, number of research rounds, sources consulted vs. accepted
vs. rejected, verification status, and intermediate file references. The researcher
agent assigns each source a stable numeric ID and maintains an evidence table
with URL, key claim, type (primary/secondary/self-reported), and confidence level.

**Lesson for bib:** Bib entries currently store BibTeX (which encodes publication
venue) and a URL. But they do not systematically track:

- **How the paper was found** — was it from a citation chain, a search, a
  recommendation, a syllabus?
- **Relationship to other entries** — some entries have cross-references
  (e.g., `[nori2019interpretml](nori2019interpretml)`), but these are ad hoc.
- **Confidence or relevance assessment** — Feynman's evidence tables
  distinguish between high/medium/low confidence claims.

For a personal bibliography, formal provenance tracking would be overkill. But
two lightweight additions could be valuable:

- A `found_via` frontmatter field (e.g., `found_via: "cited in angrist1996iv"` or
  `found_via: "alpha search for economic complexity"`).
- Standardized cross-reference syntax in notes, so that links between entries
  are parseable (the current `[citekey](citekey)` convention works for Jekyll
  rendering but could also be extracted programmatically).

---

## 6. Collections as Curated Research Outputs

**What Feynman does:** The literature-review and source-comparison skills produce
structured output documents that synthesize multiple sources: consensus summaries,
comparison matrices, open questions. These are saved as standalone artifacts in
`outputs/`.

**Lesson for bib:** The proposed `collection` layout is the natural home for this
kind of synthesis. A collection page could be:

- **Manually curated** — a reading list on a topic, with annotations about how
  the papers relate to each other.
- **Agent-generated** — the output of a `/lit` or `/compare` workflow, saved as
  a collection page that links to individual bib entries.
- **Hybrid** — an agent drafts a collection, the user reviews and edits it.

The key design decision is whether collection pages should *reference* bib entries
(by citekey) or *duplicate* metadata. Referencing by citekey is more maintainable
and consistent with the single-source-of-truth principle.

---

## 7. BibTeX as an Interchange Format

**What the alphaxiv-skill does:** `metadata <id> --bibtex` outputs a BibTeX entry
for any arXiv paper. This is a one-command path from "I found a paper" to "I have
a citation I can paste."

**Lesson for bib:** Every bib entry already contains a BibTeX block. Two features
that could streamline the pipeline:

- **Import from BibTeX:** A script that takes a BibTeX entry (pasted or from a
  `.bib` file) and scaffolds a new Markdown file with the frontmatter fields
  populated and the BibTeX block pre-filled.
- **Export to BibTeX:** A script that reads all bib entries and concatenates their
  BibTeX blocks into a single `.bib` file for use in LaTeX/LyX. This already
  works via copy-paste, but automation would help when assembling a paper's
  bibliography.

---

## 8. The Annotation Learning Loop

**What alpha-hub does:** When `alpha get` retrieves a paper, it automatically appends
any stored annotation. This means that across sessions, the agent's understanding of
a paper accumulates. The Feynman researcher agent is explicitly instructed to annotate
papers it finds useful, creating a feedback loop where the corpus of annotations grows
over time.

**Lesson for bib:** Bib already has this property — if a Claude session reads a bib
entry, it gets the user's notes and excerpts. But the loop could be made more
intentional:

- After a research session, Claude could propose additions to existing bib entries
  (new notes, cross-references, updated tags).
- The `alpha annotate` command could be mirrored: a skill that appends a note to
  an existing bib entry's "Notes and Excerpts" section, timestamped.
- Over time, bib entries would grow richer as both human and agent reading
  accumulates — exactly the "learning loop" that alpha-hub aims for, but stored
  in a durable, version-controlled, human-readable format.

---

## 9. Source Quality Heuristics

**What Feynman does:** The researcher agent has explicit source quality tiers:

- **Prefer:** academic papers, official documentation, primary datasets, verified
  benchmarks, government filings, reputable journalism
- **Accept with caveats:** well-cited secondary sources, trade publications
- **Deprioritize:** SEO listicles, undated blog posts, content aggregators
- **Reject:** no-author/no-date sources, AI-generated content without primary backing

**Lesson for bib:** The `type` field in bib's proposed schema (paper, book, article,
report, dataset) captures some of this, but a lightweight quality or formality
indicator could be useful. For example, distinguishing between a peer-reviewed
journal article, a working paper, a conference proceedings paper, and a preprint
would help when assembling a bibliography for a submission. This could be handled
via tags (e.g., `tags: [peer-reviewed]`) rather than a separate field.

---

## 10. Integrity Rules for Agent-Assisted Curation

**What Feynman does:** The researcher and writer agents have explicit "integrity
commandments" — never fabricate a source, never claim a project exists without
checking, URL-or-it-didn't-happen, read-before-you-summarize, refuse fake certainty.

**Lesson for bib:** If Claude assists with creating or updating bib entries, similar
rules should apply:

- Never create a bib entry for a paper that has not been verified to exist (via
  `alpha get`, DOI lookup, or direct URL check).
- Never fabricate BibTeX fields. If a field is unknown, leave it blank rather
  than guessing.
- Never add content to "Notes and Excerpts" that was not actually read from the
  paper or explicitly stated by the user.
- Always include a URL or DOI so the entry can be verified later.

These rules could be codified in the bib project's CLAUDE.md as agent guidelines.

---

## Summary of Actionable Patterns

| Pattern | Source | Relevance to Bib | Effort |
|---------|--------|-------------------|--------|
| Auto-surface notes on lookup | alpha-hub annotations | Already works via file reads; formalize as a skill | Low |
| `code_url` frontmatter field | alphaxiv-skill `implementations` | Useful for reproducibility-focused papers | Low |
| `found_via` frontmatter field | Feynman provenance tracking | Lightweight citation chain tracking | Low |
| BibTeX import script | alphaxiv-skill `--bibtex` | Scaffold new entries from BibTeX | Medium |
| BibTeX export script | Bib's existing BibTeX blocks | Concatenate all entries into a `.bib` file | Medium |
| Agent-assisted annotation loop | alpha-hub learning loop | Claude proposes additions after research sessions | Medium |
| Collection pages from research outputs | Feynman lit-review/compare | Generate collection drafts from `/lit` or `/compare` | Medium |
| Integrity rules for agent curation | Feynman researcher commandments | Add to CLAUDE.md as agent guidelines | Low |
| Multi-mode local search skill | alpha-hub search modes | Citekey, frontmatter, full-text search wrapper | Medium |
| Source quality tagging | Feynman source quality tiers | Tags like `peer-reviewed`, `working-paper`, `preprint` | Low |
