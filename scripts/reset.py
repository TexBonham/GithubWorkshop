"""Reset the repo after a workshop so it is ready for the next one.

    python scripts/reset.py                 # DRY RUN: show what would happen, change nothing
    python scripts/reset.py --yes           # really do it
    python scripts/reset.py --yes --skip-github   # git steps only (used for local testing)

Steps:
  1. require the tag workshop-pristine, a clean working tree on main, then git pull --ff-only
  2. restore exercises/ and ATTENDEES.md exactly to the tag, commit if changed, push to main
  3. close open PRs from fix/* and name/* branches (with a comment), delete every remote fix/* and name/* branch
  4. reopen every workshop-bug issue and remove its assignees
Read-only git/gh queries run even in a dry run. Requires gh logged in as a repo admin.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TAG = "workshop-pristine"
RESTORE_PATHS = ["exercises", "ATTENDEES.md"]
WORKSHOP_PREFIXES = ("fix/", "name/")
COMMIT_MESSAGE = "Reset workshop exercises to workshop-pristine"
CLOSE_COMMENT = "Closing: the workshop has been reset for the next session. Thanks for taking part!"


class Runner:
    def __init__(self, execute, repo):
        self.execute = execute
        self.repo = repo

    def run(self, cmd, mutating, check=True):
        printable = " ".join(quote(part) for part in cmd)
        if mutating and not self.execute:
            print("[dry run] " + printable)
            return ""
        if mutating:
            print("+ " + printable)
        result = subprocess.run(cmd, cwd=str(REPO), capture_output=True, text=True, encoding="utf-8")
        if result.returncode != 0:
            if not check:
                if result.stderr.strip():
                    print(result.stderr.strip())
                return None
            print(result.stdout.strip())
            print(result.stderr.strip())
            raise SystemExit("Command failed: " + printable)
        return result.stdout

    def git(self, args, mutating, check=True):
        return self.run(["git"] + args, mutating, check)

    def gh(self, args, mutating, check=True):
        cmd = ["gh"] + args
        if self.repo and args[0] != "api":
            cmd += ["--repo", self.repo]
        return self.run(cmd, mutating, check)


def quote(part):
    if part == "" or re.search(r"[\s\"'#<>|&]", part):
        return '"' + part.replace('"', '\\"') + '"'
    return part


def require_tag(runner):
    if runner.git(["rev-parse", "-q", "--verify", "refs/tags/" + TAG], False, check=False) is not None:
        return True
    remote = runner.git(["ls-remote", "--tags", "origin", "refs/tags/" + TAG], False, check=False)
    if remote:
        print("Tag {} exists on origin but not locally - fetching it.".format(TAG))
        runner.git(["fetch", "origin", "tag", TAG], True)
        return runner.execute
    print("ERROR: the tag '{}' does not exist (locally or on origin).".format(TAG))
    print("It marks the clean state of the exercises that reset restores. Create it once,")
    print("on main, when the exercises are exactly how attendees should first see them:")
    print("")
    print("    git tag {} && git push origin {}".format(TAG, TAG))
    raise SystemExit(1)


def prepare_main(runner):
    dirty = runner.git(["status", "--porcelain"], False)
    if dirty.strip():
        print(dirty)
        raise SystemExit("ERROR: working tree has uncommitted changes (above). Commit or stash them first.")
    branch = runner.git(["rev-parse", "--abbrev-ref", "HEAD"], False).strip()
    if branch != "main":
        raise SystemExit("ERROR: you are on '{}'. Run `git checkout main` first.".format(branch))
    runner.git(["pull", "--ff-only"], True)


def restore_exercises(runner, have_tag):
    if have_tag:
        preview = runner.git(["diff", "--stat", TAG, "--"] + RESTORE_PATHS, False)
        if preview.strip():
            print("Differences from {} that will be undone:".format(TAG))
            print(preview.rstrip())
        else:
            print("exercises/ and ATTENDEES.md already match {}.".format(TAG))
    runner.git(["rm", "-r", "-q", "--ignore-unmatch", "exercises"], True)
    runner.git(["checkout", TAG, "--"] + RESTORE_PATHS, True)
    if not runner.execute:
        print("[dry run] git commit -m \"{}\"   (only if anything changed)".format(COMMIT_MESSAGE))
        print("[dry run] git push origin main")
        return "dry run"
    if not runner.git(["status", "--porcelain"], False).strip():
        print("Nothing to commit - already pristine.")
        return "unchanged"
    runner.git(["commit", "-q", "-m", COMMIT_MESSAGE], True)
    if runner.git(["push", "origin", "main"], True, check=False) is None:
        print("")
        print("PUSH REJECTED. The reset commit is on your local main but not on GitHub.")
        print("Most likely branch protection blocks direct pushes. Either:")
        print("  - Settings > Branches > edit the main rule > allow administrators to bypass, then `git push origin main`; or")
        print("  - git checkout -b reset-workshop && git push -u origin reset-workshop, open a PR, and merge it as admin.")
        return "push failed"
    return "pushed"


def repo_name(runner):
    if runner.repo:
        return runner.repo
    return runner.gh(["repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner"], False).strip()


def close_workshop_prs(runner):
    output = runner.gh(["pr", "list", "--state", "open", "--limit", "500", "--json", "number,headRefName"], False)
    closed = 0
    for pr in json.loads(output or "[]"):
        if pr["headRefName"].startswith(WORKSHOP_PREFIXES):
            runner.gh(["pr", "close", str(pr["number"]), "--comment", CLOSE_COMMENT], True)
            closed += 1
    return closed


def delete_workshop_branches(runner, name):
    output = runner.gh(["api", "--paginate", "repos/{}/branches".format(name), "--jq", ".[].name"], False)
    deleted = 0
    for branch in output.split():
        if branch.startswith(WORKSHOP_PREFIXES):
            runner.gh(["api", "-X", "DELETE", "repos/{}/git/refs/heads/{}".format(name, branch)], True)
            deleted += 1
    return deleted


def reset_issues(runner):
    output = runner.gh(
        ["issue", "list", "--label", "workshop-bug", "--state", "all", "--limit", "500", "--json", "number,state,assignees"],
        False,
    )
    reopened = 0
    unassigned = 0
    issues = json.loads(output or "[]")
    for issue in issues:
        number = str(issue["number"])
        if issue["state"] != "OPEN":
            runner.gh(["issue", "reopen", number], True)
            reopened += 1
        logins = [person["login"] for person in issue["assignees"]]
        if logins:
            runner.gh(["issue", "edit", number, "--remove-assignee", ",".join(logins)], True)
            unassigned += 1
    return len(issues), reopened, unassigned


def main():
    sys.stdout.reconfigure(line_buffering=True, encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--yes", action="store_true", help="actually run the commands (default is a dry run)")
    parser.add_argument("--repo", help="OWNER/NAME for gh (default: the repo gh detects from this folder)")
    parser.add_argument("--skip-github", action="store_true", help="only do the local git steps (for testing)")
    args = parser.parse_args()

    runner = Runner(args.yes, args.repo)
    if not args.yes:
        print("DRY RUN - nothing will change. Re-run with --yes to do it for real.\n")

    print("== 1. Check tag, working tree, and main")
    have_tag = require_tag(runner)
    prepare_main(runner)

    print("\n== 2. Restore exercises/ and ATTENDEES.md to {}".format(TAG))
    restore = restore_exercises(runner, have_tag)

    summary = ["exercises/ATTENDEES.md: {}".format(restore)]
    if args.skip_github:
        print("\n(--skip-github: skipping pull requests, branches, and issues)")
    else:
        print("\n== 3. Close workshop pull requests and delete their branches")
        name = repo_name(runner)
        closed = close_workshop_prs(runner)
        deleted = delete_workshop_branches(runner, name)
        print("\n== 4. Reopen and unassign workshop-bug issues")
        total, reopened, unassigned = reset_issues(runner)
        summary.append("pull requests closed: {}".format(closed))
        summary.append("remote branches deleted: {}".format(deleted))
        summary.append("workshop-bug issues: {} total, {} reopened, {} unassigned".format(total, reopened, unassigned))

    heading = "\nSummary (dry run - counts are what WOULD change):"
    if args.yes:
        heading = "\nSummary:"
    print(heading)
    for line in summary:
        print("  " + line)
    if restore == "push failed":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
