# Local PDF linking from GitHub Pages

## Problem

The bib site is served from `https://rmwinslow.com/bib/` via GitHub Pages. The user has PDFs synced via Google Drive across three computers and wants bibliography entries to link to the corresponding local PDF file. However, browsers block `file:///` navigation from `https://` origins — this is a hardcoded security policy in Chromium (and all modern browsers), not a configurable setting.

We confirmed this on 2026-03-23 by pushing a test page (`test_file_links.html`) with hardcoded `file:///` links. Edge blocked every link with "Not allowed to load local resource" errors in the console.

## Approaches considered

### 1. `file:///` links (rejected)

Browsers block `file:///` links from `https://` origins. There is no Chrome/Edge policy or registry key that whitelists specific origins for `file://` access. The blocking is hardcoded in Chromium's `ShouldBlockRequestForNavigation` security check.

### 2. Localhost detection via JavaScript (considered, not ideal)

The layout renders clickable PDF links only when the site is being served from `localhost` (i.e., via `jekyll serve`). On GitHub Pages, the link is hidden or shown as plain text.

- Pros: No per-machine setup; works cleanly on local dev server.
- Cons: Only works when running Jekyll locally; doesn't help when browsing the live site. The live site is the primary use case.

### 3. Browser extension (considered, not recommended)

Install an extension like "Local Explorer" or "Enable Local File Links" on each machine, whitelist `rmwinslow.com`.

- Pros: `file:///` links work as-is with no changes to the site.
- Cons: Depends on a third-party extension that could be discontinued, removed from the extension store, or broken by a browser update. Directly at odds with the project's goal of resilience to breaking software updates. Need to find and trust an extension with broad filesystem permissions.

### 4. Custom protocol handler (recommended)

Register a custom URL scheme (e.g., `openpdf://`) in the Windows registry on each machine. The site generates `openpdf://` links instead of `file:///`. When clicked, the browser hands off to a small PowerShell script that opens the file.

#### How it works

**One-time setup per machine:** Import a `.reg` file that registers the protocol handler.

```
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Classes\openpdf]
@="URL:Open Local PDF"
"URL Protocol"=""

[HKEY_CURRENT_USER\Software\Classes\openpdf\shell\open\command]
@="powershell -NoProfile -Command \"$u='%1'; $p=$u -replace '^openpdf:///',''; $p=[uri]::UnescapeDataString($p); Start-Process $p\""
```

**In the bib layout:** Links are generated as `openpdf:///G:/My Drive/Zotero/papers/lou2013.pdf` using the entry's `pdf` frontmatter field and a configurable base path.

**User experience:** First click on a given site prompts "Allow this site to open the openpdf handler?" — the user checks "Always allow," and it never asks again for rmwinslow.com. Subsequent clicks open the PDF directly in the default viewer.

#### Pros

- No browser extension needed — nothing to break or get delisted.
- Works in any browser (Edge, Chrome, Firefox).
- Fully self-controlled; the `.reg` file can live in the repo for easy setup on new machines.
- Resilient to browser updates (custom protocol handlers are a stable OS-level feature).
- Opens PDFs in whatever the default viewer is (Zotero, Acrobat, SumatraPDF, etc.).

#### Cons

- Requires running a `.reg` file once per machine (three machines total).
- The browser shows a one-time confirmation prompt per site.
- The URL scheme is non-standard (but that's the point — standard `file://` is blocked).
- Windows-specific as written; would need equivalent setup for macOS/Linux (but all three machines are Windows).

#### Frontmatter integration

Each entry would store a relative PDF path:

```yaml
pdf: "papers/lou2013accurate.pdf"   # relative to a per-machine base path
```

The base path (e.g., `G:/My Drive/Zotero/`) would be stored either:
- In `_config.yml` (if the same across machines — unlikely)
- In a gitignored `_config.local.yml`
- In `localStorage` (set once per browser)
- Or hardcoded in the layout if all three machines share the same Google Drive path structure

The layout would concatenate the base path and the entry's `pdf` field to generate the full `openpdf:///` URL.

### 5. Copy-to-clipboard fallback

If the protocol handler approach proves too cumbersome, a simpler fallback is to render the local PDF path as visible text with a "copy to clipboard" button. The user pastes the path into Explorer. This always works with no setup but is less convenient than a clickable link.

## Status

This document records our research as of 2026-03-23. The custom protocol handler (option 4) is the leading approach but has not yet been implemented. The test page `test_file_links.html` remains in the repo for reference and can be removed when no longer needed.
