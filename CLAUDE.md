# GithubWorkshop — maintainer reference

Materials for a ~72-minute intro Git/GitHub workshop for undergrads (many brand new). Taught through **VS Code**, attendees work **solo** in this one shared repo (`TexBonham/GithubWorkshop`, public). Slides are static HTML on GitHub Pages; hands-on labs run in this repo.

## Key constants

| Constant | Value |
|---|---|
| Repo | `TexBonham/GithubWorkshop` (public, default branch `main`) |
| Expected attendees / bugs prepared | ~30 / **50** |
| Bug id format | `bug-NN` (two digits, `bug-01`..`bug-50`) |
| Bug number ranges | Python `01–17`, JavaScript `18–34`, C++ `35–50` |
| Fix branch name | `fix/bug-NN` (optional suffix: `fix/bug-07-alex`) |
| Lab 1 branch name | `name/<github-username>` |
| Required status check | job id `workshop-check`, name **`Workshop check`** (static — branch protection matches it) |
| Pristine tag (reset source) | `workshop-pristine` |
| Issue title | `[Bug NN] <bug.json title>` |
| Issue labels | `workshop-bug` + language (`python`/`javascript`/`cpp`) + difficulty (`easy`/`medium`) |
| Test timeout | 30 s per test run |
| Toolchains (CI) | Python 3 `unittest`, Node `node:test`, `g++ -std=c++17` + `<cassert>` — no third-party deps anywhere |

## Bug folder contract (summary — full detail in `exercises/CLAUDE.md`)

`exercises/<language>/bug-NN/` contains exactly three files:

| File | Role | Attendee may edit? |
|---|---|:-:|
| `bug.json` | metadata (id, number, language, title, difficulty, file, test, summary, hint) | no |
| `<file>` (e.g. `average.py`) | broken code — **one-line fix** | **yes, only this** |
| `<test>` (e.g. `test_average.py`) | tests; fail when broken, pass when fixed | no |

Answer keys: `instructor/solutions/bug-NN/<file>` — **gitignored, never committed.**

## CI rules (`scripts/ci/check_pr.py`, run by `.github/workflows/check-fixes.yml` on PRs to `main`)

| PR head branch | Allowed changed files (`git diff base...head`) | Then |
|---|---|---|
| `fix/bug-NN[-suffix]` | only `exercises/*/bug-NN/<file>` | run that bug's test; pass ⇔ tests pass |
| anything else, diff touches only `ATTENDEES.md` | `ATTENDEES.md` | pass (Lab 1 / Lab 2) |
| anything else | — | fail with a friendly explanation (instructor bypasses as admin) |

Failure messages are written for beginners and go to the job log **and** `$GITHUB_STEP_SUMMARY`.

## Where to find X

| Task | Files, in order |
|---|---|
| Add / change a bug | `exercises/<lang>/bug-NN/*` → `instructor/solutions/bug-NN/` → `python scripts/run_bug_test.py --verify-all` |
| Run one bug's test locally | `python scripts/run_bug_test.py bug-07` (`--solution` to test the answer key) |
| C++ locally on this Windows box | `source instructor/cxx-env.sh` first (points clang++ at MSVC headers) |
| Change what CI allows | `scripts/ci/check_pr.py` → `.github/workflows/check-fixes.yml` → table above |
| Create the 50 issues | `python scripts/create_issues.py` (idempotent) |
| Reset after a workshop | `python scripts/reset.py` (dry run) → `python scripts/reset.py --yes` |
| Slides / cheat sheet | `docs/index.html`, `docs/css/`, `docs/js/`, `docs/cheatsheet.html` |
| Poll link (last slide) | `docs/js/config.js` |
| Attendee setup / instructor checklist | `SETUP.md` |
| Step-by-step labs | `LABS.md` |

## Agenda (slides follow this)

| Min | Section | Format |
|---|---|---|
| 0–10 | 1–2: What Git/GitHub are, why version control | slides |
| 10–15 | Clone in VS Code, tour | follow-along |
| 15–30 | Lab 1: branch `name/<you>`, add name to `ATTENDEES.md`, commit, push, PR | hands-on |
| 30–40 | Lab 2: your PR conflicts → pull `main`, resolve in VS Code merge editor, push | hands-on |
| 40–45 | History & `git revert` | instructor demo |
| 45–60 | Lab 3: assign yourself a `[Bug NN]` issue, branch `fix/bug-NN`, fix, PR, watch check, review | hands-on |
| 60–70 | Section 6: READMEs, organizing projects, `.gitignore`, senior design tips | slides |
| 70–72 | Interest poll: long-term group resume-project workshop (biweekly/monthly) | GitHub Discussions poll + QR |

## Code conventions

- Curly braces on all control flow; no `var` in JS; no ternary (`?:`, nor Python `x if c else y`).
- Comments only where the WHY is non-obvious.
- Scripts are Python 3 stdlib only (instructor runs Windows; CI runs Ubuntu).

## Session Cost Log

| Date | Task | Mode | Tokens (est.) | Notes |
|------|------|------|:-------------:|-------|
| 2026-10-19 | Planning (topics, agenda, design decisions) | inline | ~15K | |
| 2026-10-19 | Foundations: CLAUDE.md, .gitignore, runner, 3 exemplar bugs | inline | ~20K | C++ local toolchain needed MSVC env (`instructor/cxx-env.sh`) |
| 2026-10-19 | Python bugs 02–17 | general-purpose (sonnet) | 58K | One-time content generation; 6 calls — size is file output, not re-scanning |
| 2026-10-19 | JavaScript bugs 19–34 | general-purpose (sonnet) | 58K | Same as above |
| 2026-10-19 | C++ bugs 36–50 | general-purpose (sonnet) | 61K | Same as above |
| 2026-10-19 | CI check, issue/reset scripts, templates | general-purpose | 87K | 21-case check_pr matrix + reset tests in scratchpad repo |
| 2026-10-19 | Slides, cheat sheet, LABS/SETUP/README | general-purpose | 109K | Largest output set (39 slides + notes) |
| 2026-10-19 | Integration review: replaced 3 duplicate bugs (05, 25, 44), verify-all, workflow hardening | inline | ~15K | Bug agents were siloed per language → cross-language idea overlap; next time give each agent the others' topic list |
