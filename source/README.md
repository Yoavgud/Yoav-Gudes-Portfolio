# Portfolio source files

This folder holds the **editable source** behind `index.html` one level up —
everything a Claude chat (this one or a new one) needs to make further edits
without starting from scratch.

## What's here

- `portfolio_template.html` — the real source file. Has `__IMG_...__` and
  `__RESUME_HW_B64__` / `__RESUME_SW_B64__` placeholder tokens instead of the
  giant inline base64 blobs. **Edit this file**, not `index.html` directly.
- `build.py` — reads `portfolio_template.html`, embeds every image in `imgs/`
  and both résumés in `resumes/` as base64 data, and writes `portfolio.html`
  (a fully self-contained file, same format as `index.html`).
- `imgs/` — every photo/screenshot used on the site, as plain `.jpg` files.
- `resumes/` — the two résumé PDFs that get embedded for the sidebar download
  buttons (Semiconductor/Hardware and AI/Software versions).

## How to make an edit (for a Claude session with this folder connected)

1. Edit `portfolio_template.html` directly (text changes), or add/replace a
   file in `imgs/` or `resumes/` and reference it in the template with a new
   `__IMG_SOMENAME__` / `__RESUME_..._B64__` token (add the token → filename
   mapping in `build.py`'s `tokens` / `pdf_tokens` dict too).
2. Run `python3 build.py` from this folder. It writes `portfolio.html` right
   here.
3. Copy `portfolio.html` → `../index.html` (one level up, into the repo root)
   and run `../publish.ps1` (or `git add -A && git commit -m "..." && git
   push` by hand) to push it live to GitHub Pages.
4. If you also want it live on the hosted Claude Artifact link
   (`https://claude.ai/artifact/2wWJNRNDoNwWo9G2AVKjqi`), that step needs to
   happen from inside a Claude chat using the Artifact tool — republish
   `portfolio.html` to that same URL.

## Verified

This source was reconstructed on 2026-10-22 by decompiling the live,
published `index.html` back into separate template + images + résumés, then
rebuilding and confirming the output is **byte-for-byte identical** to the
original. So this source is a complete, faithful, independent copy — it
doesn't depend on any one chat session or this container to keep working.
