"""Run the test for one workshop bug, or verify every bug against its answer key.

    python scripts/run_bug_test.py bug-07            # test the code as it is in the repo
    python scripts/run_bug_test.py 7 --solution      # test with instructor/solutions/bug-07 applied
    python scripts/run_bug_test.py --verify-all      # every bug: broken must FAIL, solution must PASS

Exit codes: 0 = tests passed (or verification clean), 1 = tests failed, 2 = bad input.
C++ uses $CXX if set, otherwise g++, otherwise clang++.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EXERCISES = REPO / "exercises"
SOLUTIONS = REPO / "instructor" / "solutions"
TIMEOUT_SECONDS = 30


def normalize_id(raw):
    text = raw.strip().lower()
    if text.startswith("bug-"):
        text = text[4:]
    if not text.isdigit():
        return None
    return "bug-{:02d}".format(int(text))


def load_bug(bug_id):
    matches = list(EXERCISES.glob("*/{}/bug.json".format(bug_id)))
    if len(matches) != 1:
        return None
    meta = json.loads(matches[0].read_text(encoding="utf-8"))
    meta["dir"] = matches[0].parent
    return meta


def all_bugs():
    bugs = []
    for path in EXERCISES.glob("*/bug-*/bug.json"):
        meta = json.loads(path.read_text(encoding="utf-8"))
        meta["dir"] = path.parent
        bugs.append(meta)
    bugs.sort(key=lambda meta: meta["number"])
    return bugs


def find_cxx():
    if os.environ.get("CXX"):
        return os.environ["CXX"]
    for name in ("g++", "clang++"):
        if shutil.which(name):
            return name
    return None


def run(cmd, cwd):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    try:
        result = subprocess.run(cmd, cwd=str(cwd), env=env, timeout=TIMEOUT_SECONDS)
    except subprocess.TimeoutExpired:
        print("\nTest timed out after {} seconds (is there an infinite loop?)".format(TIMEOUT_SECONDS))
        return 1
    return result.returncode


def run_tests(meta, work_dir):
    language = meta["language"]
    if language == "python":
        module = Path(meta["test"]).stem
        return run([sys.executable, "-m", "unittest", "-v", module], work_dir)
    if language == "javascript":
        return run(["node", "--test", meta["test"]], work_dir)
    if language == "cpp":
        cxx = find_cxx()
        if cxx is None:
            print("No C++ compiler found (set CXX, or install g++/clang++)")
            return 2
        with tempfile.TemporaryDirectory() as build:
            binary = str(Path(build) / "test_bin")
            if os.name == "nt":
                binary += ".exe"
            compiled = run([cxx, "-std=c++17", "-Wall", "-o", binary, meta["test"]], work_dir)
            if compiled != 0:
                print("\nCompile failed - fix the compiler error above first.")
                return 1
            return run([binary], work_dir)
    print("Unknown language in bug.json: {}".format(language))
    return 2


def test_bug(meta, with_solution):
    if not with_solution:
        return run_tests(meta, meta["dir"])
    answer = SOLUTIONS / meta["id"] / meta["file"]
    if not answer.is_file():
        print("Missing answer key: {}".format(answer))
        return 2
    with tempfile.TemporaryDirectory() as scratch:
        work_dir = Path(scratch) / meta["id"]
        shutil.copytree(meta["dir"], work_dir)
        shutil.copyfile(answer, work_dir / meta["file"])
        return run_tests(meta, work_dir)


def verify_all():
    problems = []
    bugs = all_bugs()
    for meta in bugs:
        print("\n===== {} ({}) broken - expecting FAIL =====".format(meta["id"], meta["language"]))
        if test_bug(meta, False) == 0:
            problems.append("{}: broken code PASSES its test".format(meta["id"]))
        print("\n===== {} ({}) solution - expecting PASS =====".format(meta["id"], meta["language"]))
        if test_bug(meta, True) != 0:
            problems.append("{}: solution does NOT pass its test".format(meta["id"]))
    print("\nVerified {} bugs.".format(len(bugs)))
    if problems:
        print("PROBLEMS:")
        for line in problems:
            print("  " + line)
        return 1
    print("All bugs fail when broken and pass when fixed.")
    return 0


def main():
    sys.stdout.reconfigure(line_buffering=True)
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("bug", nargs="?", help="bug id, e.g. bug-07 or 7")
    parser.add_argument("--solution", action="store_true", help="apply the instructor answer key first")
    parser.add_argument("--verify-all", action="store_true", help="check every bug fails broken and passes fixed")
    args = parser.parse_args()

    if args.verify_all:
        return verify_all()
    if args.bug is None:
        parser.print_help()
        return 2
    bug_id = normalize_id(args.bug)
    if bug_id is None:
        print("Not a bug id: {}".format(args.bug))
        return 2
    meta = load_bug(bug_id)
    if meta is None:
        print("No bug folder found for {}".format(bug_id))
        return 2
    return test_bug(meta, args.solution)


if __name__ == "__main__":
    sys.exit(main())
