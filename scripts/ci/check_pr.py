"""Workshop pull request check (run by .github/workflows/check-fixes.yml).

    python scripts/ci/check_pr.py --head-ref fix/bug-07 --base <sha-or-ref> --head <sha-or-ref>

Rules (see the CI rules table in the root CLAUDE.md):
  fix/bug-NN[-suffix]  -> may change ONLY exercises/<lang>/bug-NN/<file>; then that bug's test must pass
  any other branch     -> may change ONLY ATTENDEES.md
The bug test runs against the working tree, so check out the PR code first.
Env fallbacks: HEAD_REF, BASE_SHA, HEAD_SHA, PR_BODY, GITHUB_STEP_SUMMARY.
Exit codes: 0 = pass, 1 = fail.
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import run_bug_test  # noqa: E402

REPO = run_bug_test.REPO
FIX_BRANCH = re.compile(r"^fix/bug-(\d{1,2})(-[A-Za-z0-9._-]+)?$")
CLOSING_KEYWORD = re.compile(r"\b(close[sd]?|fix(e[sd])?|resolve[sd]?)\s+#\d+", re.IGNORECASE)
ATTENDEES = "ATTENDEES.md"


class Report:
    def __init__(self):
        self.lines = []

    def say(self, text=""):
        print(text)

    def error(self, text):
        print("::error::" + text.replace("\n", "%0A"))

    def warning(self, text):
        print("::warning::" + text.replace("\n", "%0A"))

    def notice(self, text):
        print("::notice::" + text.replace("\n", "%0A"))

    def summary(self, text=""):
        self.lines.append(text)

    def write_summary(self):
        path = os.environ.get("GITHUB_STEP_SUMMARY")
        if not path:
            return
        with open(path, "a", encoding="utf-8") as handle:
            handle.write("\n".join(self.lines) + "\n")


def changed_files(base, head):
    cmd = ["git", "diff", "--name-status", "--no-renames", "{}...{}".format(base, head)]
    result = subprocess.run(cmd, cwd=str(REPO), capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        print(result.stderr)
        raise SystemExit("Could not compute the changed files with: " + " ".join(cmd))
    changes = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        status, path = line.split("\t", 1)
        changes.append((status[0], path.replace("\\", "/")))
    return changes


def undo_steps(offending):
    lines = [
        "How to undo it in VS Code: open the terminal (Terminal > New Terminal) and run:",
        "",
        "```",
        "git fetch origin",
    ]
    for status, path in offending:
        if status == "A":
            lines.append('git rm "{}"'.format(path))
        else:
            lines.append('git checkout origin/main -- "{}"'.format(path))
    lines.append('git commit -m "Undo changes to files I should not have touched"')
    lines.append("git push")
    lines.append("```")
    lines.append("")
    lines.append("The check re-runs by itself after you push.")
    return lines


def fail(report, headline, details):
    report.error(headline)
    report.say("")
    report.say("FAILED: " + headline)
    for line in details:
        report.say("  " + line)
    report.summary("## ❌ " + headline)
    report.summary("")
    for line in details:
        report.summary(line)
    return 1


def check_fix_branch(report, number_text, changes, pr_body):
    bug_id = run_bug_test.normalize_id(number_text)
    label = "Bug {}".format(bug_id[4:])
    meta = run_bug_test.load_bug(bug_id)
    if meta is None:
        return fail(report, "There is no {} in this workshop".format(label), [
            "Your branch name points at `{}`, but no folder `exercises/*/{}` exists.".format(bug_id, bug_id),
            "",
            "Check the number in your issue title (`[Bug NN] ...`) and name your branch `fix/bug-NN` to match.",
            "To rename a branch in VS Code: Command Palette (Ctrl+Shift+P) > **Git: Rename Branch...**, then push and open a new pull request.",
        ])

    allowed = Path(meta["dir"]).relative_to(REPO).as_posix() + "/" + meta["file"]
    if not changes:
        return fail(report, "{}: you haven't committed a change yet".format(label), [
            "This pull request has no changed files compared to `main`.",
            "",
            "Edit `{}`, then in VS Code's Source Control panel: type a message, click **Commit**, then **Sync Changes** (push).".format(allowed),
        ])

    offending = [(status, path) for status, path in changes if path != allowed]
    if offending:
        details = [
            "A fix pull request may change **only one file**: `{}`.".format(allowed),
            "",
            "These files should not be in this pull request:",
            "",
        ]
        for status, path in offending:
            details.append("- `{}`".format(path))
        details.append("")
        details.extend(undo_steps(offending))
        return fail(report, "{}: this pull request changes files it shouldn't".format(label), details)

    report.say("Only {} changed - running the {} tests for {}...".format(allowed, meta["language"], bug_id))
    report.say("")
    sys.stdout.flush()
    result = run_bug_test.test_bug(meta, False)
    sys.stdout.flush()
    report.say("")

    if pr_body is not None and not CLOSING_KEYWORD.search(pr_body):
        report.warning(
            "Your pull request description has no 'Closes #<issue number>' line, "
            "so the issue won't close automatically when this merges. Edit the description to add it."
        )

    if result != 0:
        return fail(report, "{} isn't fixed yet".format(label), [
            "The tests for `{}` are still failing.".format(bug_id),
            "",
            "What to do next:",
            "1. Click **Details** next to the check, expand the **Check this pull request** step, and read the test output - it says which case failed and what it expected.",
            "2. Re-read the hint in your issue.",
            "3. Change `{}`, commit, and push. This check re-runs automatically.".format(allowed),
            "",
            "Tip: run it yourself first with `python scripts/run_bug_test.py {}`.".format(bug_id),
        ])

    headline = "{} fixed — nice work!".format(label)
    report.notice(headline)
    report.say("PASSED: " + headline)
    report.summary("## ✅ " + headline)
    report.summary("")
    report.summary("All tests for `{}` pass. Next: ask a neighbor (or the instructor) to review your pull request.".format(bug_id))
    return 0


def check_other_branch(report, head_ref, changes):
    if changes and all(path == ATTENDEES for _, path in changes):
        headline = "Only ATTENDEES.md changed — looks good!"
        report.notice(headline)
        report.say("PASSED: " + headline)
        report.summary("## ✅ " + headline)
        report.summary("")
        report.summary("Branch `{}` changes only `ATTENDEES.md`, which is exactly what Lab 1 / Lab 2 asks for.".format(head_ref))
        return 0

    details = [
        "Branch `{}` isn't a bug-fix branch, so it may change only `ATTENDEES.md`.".format(head_ref),
        "",
        "- **Fixing a bug (Lab 3)?** Name the branch `fix/bug-NN` (e.g. `fix/bug-07`) and change only that bug's one file.",
        "- **Adding your name (Lab 1 / Lab 2)?** Use a `name/<your-github-username>` branch and change only `ATTENDEES.md`.",
    ]
    if head_ref.startswith("fix/"):
        details.append("")
        details.append("Your branch starts with `fix/` but doesn't match `fix/bug-NN` exactly (e.g. `fix/bug-07`).")
    details.append("")
    details.append("Wrong branch name? In VS Code: Command Palette (Ctrl+Shift+P) > **Git: Rename Branch...**, push, then open a new pull request from the renamed branch.")
    if not changes:
        details.append("")
        details.append("This pull request has no changed files compared to `main` yet.")
    else:
        others = [(status, path) for status, path in changes if path != ATTENDEES]
        details.append("")
        details.append("Files that shouldn't be here:")
        details.append("")
        for status, path in others:
            details.append("- `{}`".format(path))
        details.append("")
        details.extend(undo_steps(others))
    return fail(report, "This pull request doesn't follow the workshop rules", details)


def main():
    sys.stdout.reconfigure(line_buffering=True, encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--head-ref", default=os.environ.get("HEAD_REF"), help="PR head branch name")
    parser.add_argument("--base", default=os.environ.get("BASE_SHA"), help="base commit (sha or ref)")
    parser.add_argument("--head", default=os.environ.get("HEAD_SHA"), help="head commit (sha or ref)")
    args = parser.parse_args()
    if not args.head_ref or not args.base or not args.head:
        parser.print_help()
        return 1

    pr_body = os.environ.get("PR_BODY")
    report = Report()
    changes = changed_files(args.base, args.head)
    report.say("Branch: {}".format(args.head_ref))
    report.say("Changed files ({}):".format(len(changes)))
    for status, path in changes:
        report.say("  {} {}".format(status, path))
    report.say("")

    match = FIX_BRANCH.match(args.head_ref)
    if match:
        result = check_fix_branch(report, match.group(1), changes, pr_body)
    else:
        result = check_other_branch(report, args.head_ref, changes)
    report.write_summary()
    return result


if __name__ == "__main__":
    sys.exit(main())
