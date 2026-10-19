"""Create one GitHub issue per workshop bug (plus the labels they use).

    python scripts/create_issues.py                 # DRY RUN: print every gh command, change nothing
    python scripts/create_issues.py --yes           # really create labels and issues
    python scripts/create_issues.py --repo OWNER/NAME --yes

Idempotent: issues whose title already exists (any state) are skipped; an existing issue
missing its "Closes #N" line gets it added. Read-only gh queries run even in a dry run.
Requires the GitHub CLI (gh), logged in with write access to the repo.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_bug_test  # noqa: E402

REPO = run_bug_test.REPO

LABELS = [
    ("workshop-bug", "d73a4a", "A bug to fix during the Git/GitHub workshop"),
    ("python", "3572A5", "Python exercise"),
    ("javascript", "f1e05a", "JavaScript exercise"),
    ("cpp", "f34b7d", "C++ exercise"),
    ("easy", "0e8a16", "Good first fix"),
    ("medium", "fbca04", "Needs a little more digging"),
]

ISSUE_URL = re.compile(r"/issues/(\d+)\s*$")


class Gh:
    def __init__(self, repo, execute, verbose):
        self.repo = repo
        self.execute = execute
        self.verbose = verbose

    def run(self, args, mutating, show=None):
        cmd = ["gh"] + args
        if self.repo:
            cmd += ["--repo", self.repo]
        printable = show
        if printable is None:
            printable = " ".join(quote(part) for part in cmd)
        if mutating and not self.execute:
            print("[dry run] " + printable)
            return ""
        if mutating:
            print("+ " + printable)
        result = subprocess.run(cmd, cwd=str(REPO), capture_output=True, text=True, encoding="utf-8")
        if result.returncode != 0:
            print(result.stderr.strip())
            raise SystemExit("gh command failed: " + printable)
        return result.stdout


def quote(part):
    if part == "" or re.search(r"[\s\"'#<>|&]", part):
        return '"' + part.replace('"', '\\"') + '"'
    return part


def issue_title(meta):
    return "[Bug {:02d}] {}".format(meta["number"], meta["title"])


def issue_labels(meta):
    return ["workshop-bug", meta["language"], meta["difficulty"]]


def file_path(meta):
    return Path(meta["dir"]).relative_to(REPO).as_posix() + "/" + meta["file"]


def closes_line(number):
    return "In your pull request description write: `Closes #{}`".format(number)


def issue_body(meta, number):
    branch = "fix/bug-{:02d}".format(meta["number"])
    path = file_path(meta)
    lines = [
        "## What's wrong",
        "",
        meta["summary"],
        "",
        "<details>",
        "<summary>Hint (click to open)</summary>",
        "",
        meta["hint"],
        "",
        "</details>",
        "",
        "## Where",
        "",
        "- File to edit: `{}` (change **only** this file)".format(path),
        "- Branch name: `{}`".format(branch),
        "",
        "## Steps",
        "",
        "1. **Assign yourself** to this issue (right side: Assignees > assign yourself) so nobody else picks it.",
        "2. In VS Code, make sure you're on `main` and pull, then create a branch named exactly `{}`.".format(branch),
        "3. Open `{}` and fix the one line that's wrong.".format(path),
        "4. Test it (optional, needs {}): `python scripts/run_bug_test.py {}`".format(language_name(meta), meta["id"]),
        "5. Commit, then **Publish Branch** / push.",
        "6. Open a pull request into `main`.",
    ]
    if number is None:
        lines.append("7. In your pull request description, write `Closes #` followed by this issue's number.")
    else:
        lines.append("7. " + closes_line(number))
    lines.append("8. Watch the **Workshop check** on your pull request turn green, then ask someone to review it.")
    return "\n".join(lines) + "\n"


def language_name(meta):
    names = {"python": "Python", "javascript": "Node.js", "cpp": "a C++ compiler"}
    return names.get(meta["language"], meta["language"])


def ensure_labels(gh):
    for name, color, description in LABELS:
        gh.run(["label", "create", name, "--color", color, "--description", description, "--force"], True)


def existing_issues(gh):
    output = gh.run(
        ["issue", "list", "--label", "workshop-bug", "--state", "all", "--limit", "500", "--json", "number,title,body"],
        False,
    )
    by_title = {}
    for issue in json.loads(output or "[]"):
        by_title[issue["title"]] = issue
    return by_title


def body_arg_display(cmd_args, body):
    shown = []
    for part in cmd_args:
        if part == body:
            shown.append("<body: {} lines>".format(body.count("\n")))
        else:
            shown.append(quote(part))
    return " ".join(["gh"] + shown)


def create_issue(gh, meta):
    title = issue_title(meta)
    body = issue_body(meta, None)
    args = ["issue", "create", "--title", title, "--body", body]
    for label in issue_labels(meta):
        args += ["--label", label]
    output = gh.run(args, True, show=body_arg_display(args, body))
    if gh.verbose:
        print(body)
    if not gh.execute:
        print("[dry run] gh issue edit <new number> --body <body with '{}'>".format(closes_line("<new number>")))
        return
    match = ISSUE_URL.search(output.strip())
    if match is None:
        raise SystemExit("Could not read the new issue number from gh output: " + output)
    set_closes_line(gh, meta, int(match.group(1)))


def set_closes_line(gh, meta, number):
    body = issue_body(meta, number)
    args = ["issue", "edit", str(number), "--body", body]
    gh.run(args, True, show=body_arg_display(args, body))


def main():
    sys.stdout.reconfigure(line_buffering=True, encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--yes", action="store_true", help="actually run the commands (default is a dry run)")
    parser.add_argument("--repo", help="OWNER/NAME (default: the repo gh detects from this folder)")
    parser.add_argument("--verbose", action="store_true", help="also print each issue body")
    args = parser.parse_args()

    gh = Gh(args.repo, args.yes, args.verbose)
    if not args.yes:
        print("DRY RUN - nothing will change. Re-run with --yes to do it for real.\n")

    bugs = run_bug_test.all_bugs()
    print("Found {} bugs.\n".format(len(bugs)))
    ensure_labels(gh)
    existing = existing_issues(gh)

    created = 0
    skipped = 0
    patched = 0
    for meta in bugs:
        title = issue_title(meta)
        issue = existing.get(title)
        if issue is None:
            create_issue(gh, meta)
            created += 1
            continue
        if closes_line(issue["number"]) not in (issue.get("body") or ""):
            print("#{} exists but lacks its Closes line - updating".format(issue["number"]))
            set_closes_line(gh, meta, issue["number"])
            patched += 1
            continue
        print("skip (exists as #{}): {}".format(issue["number"], title))
        skipped += 1

    verb = "Would create"
    if args.yes:
        verb = "Created"
    print("\n{} {} issue(s); {} already existed; {} existing issue(s) updated.".format(verb, created, skipped, patched))
    return 0


if __name__ == "__main__":
    sys.exit(main())
