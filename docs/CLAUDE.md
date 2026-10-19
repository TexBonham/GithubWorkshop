# docs/ — slides and cheat sheet (GitHub Pages root)

Served from `/docs` on `main` at https://texbonham.github.io/GithubWorkshop/. No build step, no frameworks; edit the files directly.

## Files

| File | Role |
|---|---|
| `index.html` | The deck. Every slide is a `<section class="slide">` inside `<main class="deck">`, in agenda order. Ends with the HUD `<nav class="hud">` and the two scripts. |
| `css/slides.css` | Tokens on `:root` (light) + dark overrides (`prefers-color-scheme` guarded by `:root:not([data-theme="light"])`, and `:root[data-theme="dark"]`). Layout, slide variants, diagram, notes, HUD, overview grid, print. |
| `js/config.js` | `window.WORKSHOP_CONFIG` — instructor-editable values (below). Loaded before `slides.js`. |
| `js/slides.js` | Navigation, hash sync, notes/overview/fullscreen, clock, HUD, config links, QR. One IIFE. |
| `cheatsheet.html` | Standalone one-page (letter) cheat sheet with its own inline styles. Linked from the HUD and the wrap-up slide. |

## config.js keys

| Key | Default | Used for |
|---|---|---|
| `REPO_URL` | `https://github.com/TexBonham/GithubWorkshop` | every `<a data-repo-link>` (`data-repo-link="text"` also replaces link text) |
| `POLL_URL` | `https://github.com/TexBonham/GithubWorkshop/discussions` | last slide `#poll-link` + QR in `#poll-qr`. Instructor pastes the specific poll discussion URL. |

QR: `slides.js` injects `qrcodejs` 1.0.0 from cdnjs asynchronously; if it fails, the plain link (already in the HTML) still shows and `.qr:empty` hides the box.

## Slide markup conventions

| Thing | Markup |
|---|---|
| Section divider | `<section class="slide divider" data-section="N · Title" data-at="mm:ss">` — `data-section` sets the HUD label for it and every later slide; `data-at` = planned start time shown next to the clock |
| Lab slide | `class="slide lab"`, `.kicker` "Hands-on · Lab N · X min", short `<ol>`, `.labfoot` with link to the `LABS.md` anchor |
| Speaker notes | exactly one `<aside class="notes"><ul><li>[timing] …</li></ul></aside>` per slide (smoke check expects it) |
| Terminal equivalent | `<span class="cmd"><code>git …</code></span>` under the VS Code action (small, muted) |
| Two columns | `<div class="cols">` (`.three` for three); cards `<div class="card">` (`.good` / `.bad` accent) |
| Tables | `<div class="table-wrap"><table class="simple">` |
| Diagram | inline SVG, two variants `.flow-wide` (landscape ≥760px) and `.flow-tall` (portrait); classes `box`/`local`/`remote`/`label`/`sub`/`verb`/`arrow`/`back`/`zone` |

## Add / reorder a slide

1. Copy an existing `<section class="slide">…</section>` block (including its `<aside class="notes">`).
2. Paste it where it belongs; order in the file = order in the deck. Slide numbers (URL hash) are positional, so they shift.
3. New section? Add a `<!-- ===== Section N: Title ===== -->` marker and a divider slide with `data-section`/`data-at`, then update the index below.
4. Check: `node --check docs/js/slides.js` and open `index.html` in a browser (works from `file://`).

## Keyboard / input

| Input | Action |
|---|---|
| `→` `Space` `PageDown` / swipe left / click right half | next |
| `←` `PageUp` / swipe right / click left half | previous |
| `Home` / `End` | first / last |
| `N` | toggle speaker notes panel |
| `F` | fullscreen |
| `O` (or `Esc` to leave) | overview grid; click a slide to jump |
| `T` | reset the elapsed clock |
| URL `#N` | slide N (1-based); kept in sync, survives reload |

Clicks on links, buttons, `pre`, notes, HUD, and QR don't navigate; neither does a click while text is selected.

## index.html section index (line numbers)

| Line | Marker | Slides |
|---:|---|---:|
| 14 | Section 0: Welcome | 2 |
| 53 | Section 1: What Git and GitHub are | 6 |
| 161 | Section 2: Getting started | 4 |
| 223 | Section 3: Fundamentals (diagram, init/clone, loop, Lab 0) | 5 |
| 368 | Section 4: Branches and pull requests (Lab 1) | 4 |
| 438 | Section 5: Merge conflicts (Lab 2) | 3 |
| 495 | Section 6: History and undo (demo) | 3 |
| 544 | Section 7: Collaboration (issues, review, fork note, Lab 3) | 4 |
| 617 | Section 8: Engineering projects | 6 |
| 735 | Section 9: Wrap-up (recap, poll) | 2 |

Total 39 slides. Read a section with `Read(docs/index.html, offset=<line>, limit=80)`.
