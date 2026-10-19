# scripts/ — contract

All Python 3 stdlib only; run from any cwd (paths resolve from the script's location). `check_pr.py` and `create_issues.py` import `run_bug_test` (never duplicate its logic).

## Dry-run convention (instructor scripts)

`create_issues.py` and `reset.py` are **dry run by default**; `--yes` executes. Every git/gh call goes through ONE helper (`Gh.run` / `Runner.run`) taking a `mutating` flag: mutating calls print `[dry run] <cmd>` and return `""` unless `--yes`; read-only queries (list/view/diff/status) always run. Executed mutating calls print `+ <cmd>`. Any new call MUST go through the helper with the right flag.

## `run_bug_test.py` — run/verify bug tests

| Flag / function | Does |
|---|---|
| `bug` (positional), `--solution`, `--verify-all` | test one bug / with answer key / every bug broken-fails + solution-passes |
| `normalize_id(raw)` | `"7"`, `"bug-7"` → `"bug-07"`; `None` if not numeric |
| `load_bug(bug_id)` | `bug.json` dict + `dir` (Path), or `None` |
| `all_bugs()` | every bug's meta, sorted by `number` |
| `test_bug(meta, with_solution)` | runs the test in the bug folder; 0 pass, 1 fail, 2 setup error |

## `ci/check_pr.py` — the PR check (CI rules table in root `CLAUDE.md`)

`python scripts/ci/check_pr.py --head-ref fix/bug-07 --base <sha|ref> --head <sha|ref>` (env fallbacks `HEAD_REF`, `BASE_SHA`, `HEAD_SHA`; optional `PR_BODY`, `GITHUB_STEP_SUMMARY`). Tests run on the **working tree**, so check out the PR code first. Exit 0 pass / 1 fail.

| Function | Does |
|---|---|
| `changed_files(base, head)` | `git diff --name-status --no-renames base...head` → `[(status, posix_path)]` (three-dot: main merged into the branch doesn't count) |
| `check_fix_branch(report, n, changes, body)` | bug exists → non-empty diff → only `exercises/<lang>/bug-NN/<file>` → `test_bug`; `::warning::` if body lacks `closes/fixes/resolves #N` |
| `check_other_branch(report, ref, changes)` | pass iff non-empty diff touching only `ATTENDEES.md` |
| `undo_steps(offending)` | terminal commands to revert files (`git checkout origin/main --` / `git rm` for added files) |
| `fail(report, headline, details)` | `::error::` + stdout + `## ❌` step summary |
| `Report` | stdout, `::error/warning/notice::` annotations, buffered summary → `$GITHUB_STEP_SUMMARY` |

Branch regex: `^fix/bug-(\d{1,2})(-[A-Za-z0-9._-]+)?$` (`fix/bug-1`, `fix/bug-07-alex` OK). Local case matrix lives in the scratchpad test script, not the repo.

## `create_issues.py` — one issue per bug

Flags: `--yes`, `--repo OWNER/NAME`, `--verbose` (print bodies). Idempotent by exact title.

| Function | Does |
|---|---|
| `Gh.run(args, mutating, show)` | the single gh helper (appends `--repo`) |
| `ensure_labels(gh)` | `gh label create --force` for `LABELS` (workshop-bug, python, javascript, cpp, easy, medium) |
| `existing_issues(gh)` | `workshop-bug` issues (all states) keyed by title |
| `issue_body(meta, number)` | summary, `<details>` hint, file path, branch, steps, test cmd; `Closes #N` line when number known |
| `create_issue(gh, meta)` | create → parse `/issues/N` from output → `set_closes_line` |
| `set_closes_line(gh, meta, n)` | rewrite body with `Closes #n`; also back-fills existing issues missing it |

## `reset.py` — post-workshop reset

Flags: `--yes`, `--repo OWNER/NAME`, `--skip-github` (local git steps only — for testing in a throwaway repo).

| Function | Does |
|---|---|
| `Runner.run/git/gh(cmd, mutating, check)` | the single helper; `check=False` returns `None` on failure |
| `require_tag(runner)` | `workshop-pristine` local, else fetch from origin, else exit 1 with create instructions |
| `prepare_main(runner)` | clean tree + on `main` + `git pull --ff-only` |
| `restore_exercises(runner, have_tag)` | preview diff, `git rm -r exercises` + `git checkout TAG -- exercises ATTENDEES.md`, commit if changed, push; prints manual steps if push rejected (exit 1) |
| `close_workshop_prs(runner)` | close open PRs with head `fix/*` / `name/*`, with a comment |
| `delete_workshop_branches(runner, repo)` | delete EVERY remote `fix/*` / `name/*` branch (incl. ones from merged PRs) via `gh api -X DELETE` |
| `reset_issues(runner)` | reopen closed `workshop-bug` issues, remove all assignees |
