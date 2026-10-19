# exercises/ — bug folder contract

One folder per bug: `exercises/<language>/bug-NN/`. Exemplars to copy the shape of: `python/bug-01`, `javascript/bug-18`, `cpp/bug-35`.

## Files

| File | Python | JavaScript | C++ |
|---|---|---|---|
| broken file (`file`) | `<name>.py` | `<name>.js` (CommonJS, `module.exports = { fn }`) | `<name>.cpp` (no `main`) |
| test (`test`) | `test_<name>.py`, `unittest`, `from <name> import fn` | `<name>.test.js`, `node:test` + `node:assert/strict`, `require("./<name>")` | `test_<name>.cpp`, `#include "<name>.cpp"`, `<cassert>`, `main()` returns 0 |
| how it runs (cwd = bug folder) | `python -m unittest -v test_<name>` | `node --test <name>.test.js` | `g++ -std=c++17 -Wall -o bin test_<name>.cpp && ./bin` |

## `bug.json`

```json
{
  "id": "bug-07", "number": 7, "language": "python|javascript|cpp",
  "title": "Short plain-English symptom (becomes issue title)",
  "difficulty": "easy|medium",
  "file": "average.py", "test": "test_average.py",
  "summary": "What the function SHOULD do + a concrete example that currently fails. Markdown ok.",
  "hint": "One nudge toward the line, without giving the answer."
}
```

## Rules for every bug

- The fix is a **single line** change, findable by someone who doesn't know the language.
- Test fails deterministically on the broken code, passes on the solution. Verify with `python scripts/run_bug_test.py --verify-all`.
- Broken file contains no hint comments; the bug must look like an honest mistake.
- Folder is self-contained: test imports only the sibling broken file; stdlib only.
- Answer key: full corrected copy of `<file>` at `instructor/solutions/bug-NN/<file>` (gitignored).
- Each bug uses a distinct function/idea — no two bugs alike across the whole set.
- Mix: ~70% `easy`, ~30% `medium`; at most 3 syntax/compile-error bugs per language, the rest logic bugs (off-by-one, wrong operator, wrong comparison, wrong variable, wrong initial value, missed edge case, wrong return).
