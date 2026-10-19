# Workshop Labs

Step-by-step instructions for every hands-on part of the workshop. Each step shows the **VS Code** way first, then the same thing **in the terminal** for reference. You only need one of them.

> Haven't set up yet? Do [SETUP.md](SETUP.md) first. Want a one-page summary? See the [cheat sheet](https://texbonham.github.io/GithubWorkshop/cheatsheet.html).

**Words you'll see**

| Word | Meaning |
|---|---|
| **repository (repo)** | A project folder that Git tracks, including its full history |
| **commit** | A saved snapshot of your changes, with a short message |
| **branch** | A separate line of work; `main` is the official one |
| **push / pull** | Send your commits to GitHub / bring others' commits down |
| **pull request (PR)** | A request to merge your branch into `main`, with review and checks |
| **remote / `origin`** | The copy of the repo on GitHub |

Contents: [Lab 0](#lab-0-clone-and-tour-follow-along) · [Lab 1](#lab-1-sign-the-guestbook) · [Lab 2](#lab-2-resolve-a-merge-conflict) · [Demo: history and undo](#demo-history-and-undo-instructor) · [Lab 3](#lab-3-fix-a-bug)

---

## Lab 0: Clone and tour (follow-along)

**Goal:** get your own copy of this repo on your computer and open it in VS Code.

1. **Clone the repo.**
   - In VS Code: open the Command Palette (`Ctrl+Shift+P` on Windows, `Cmd+Shift+P` on macOS), type **Git: Clone**, press Enter, paste `https://github.com/TexBonham/GithubWorkshop`, and press Enter.
   - Or in the terminal: `git clone https://github.com/TexBonham/GithubWorkshop.git`
2. **Pick a folder** to put it in (your Desktop or Documents is fine). When VS Code asks "Would you like to open the cloned repository?", click **Open**.
   - Or in the terminal: `cd GithubWorkshop` then `code .`
3. **If a browser window asks you to sign in or authorize**, click **Allow** / **Authorize**. That's all the login you need.
4. **Take the tour.**
   - **Explorer** (top icon in the left bar): the files. Open `ATTENDEES.md` and find the line `<!-- ADD YOUR LINE DIRECTLY BELOW THIS MARKER -->`.
   - **Source Control** (the branch-shaped icon): shows files you've changed. Empty right now.
   - **Status bar** (bottom-left): the current branch name, `main`, and the sync arrows.
   - Or in the terminal: `git status` shows the branch and any changes.

**What you just learned:** `clone` downloads a repo and its whole history, and remembers GitHub as `origin`.

| Problem | Fix |
|---|---|
| "Git not found" / no Clone option | Git isn't installed, or VS Code was open during the install. Install Git ([SETUP.md](SETUP.md)), then fully quit and reopen VS Code. |
| "Repository not found" | Check the URL. Make sure you accepted the collaborator invite: <https://github.com/TexBonham/GithubWorkshop/invitations>. |
| Opened the wrong folder | **File → Open Folder…** and choose the `GithubWorkshop` folder. |

---

## Lab 1: Sign the guestbook

**Goal:** make a branch, change a file, commit, push, and open a pull request.

1. **Start on `main`, up to date.**
   - In VS Code: the status bar should say `main`. If not, click the branch name and pick `main`. Then in Source Control click **…** (More Actions) → **Pull**.
   - Or in the terminal: `git switch main` then `git pull`
2. **Create your branch** named `name/<your-github-username>`, for example `name/octocat`.
   - In VS Code: click the branch name in the status bar → **+ Create new branch…** → type `name/octocat` → Enter.
   - Or in the terminal: `git switch -c name/octocat`
3. **Add your line to `ATTENDEES.md`.** Put it on the line **directly below the marker**, not at the bottom of the file. Use exactly this format:

   ```
   - Your Name (@your-github-username) — your major
   ```

   Save the file (`Ctrl+S` / `Cmd+S`).
4. **Stage the change.**
   - In VS Code: in Source Control, hover over `ATTENDEES.md` and click **+** (Stage Changes).
   - Or in the terminal: `git add ATTENDEES.md`
5. **Commit with a good message.** Good messages say what you did, e.g. `Add Ana Ruiz to attendees`.
   - In VS Code: type the message in the box at the top of Source Control and click **Commit**.
   - Or in the terminal: `git commit -m "Add Ana Ruiz to attendees"`
6. **Publish (push) your branch to GitHub.**
   - In VS Code: click **Publish Branch**.
   - Or in the terminal: `git push -u origin name/octocat`
7. **Open a pull request.** Go to <https://github.com/TexBonham/GithubWorkshop>. A yellow banner says your branch had recent pushes: click **Compare & pull request**. Check it says `base: main` ← `compare: name/octocat`, then click **Create pull request**.
   - No banner? Click **Pull requests** → **New pull request**, set compare to your branch.
8. **Watch the "Workshop check".** At the bottom of the PR, a check called **Workshop check** runs. A green check mark means you're done. The instructor will merge PRs.

**What you just learned:** the everyday loop: branch → edit → stage → commit → push → pull request.

| Problem | Fix |
|---|---|
| Push says it's rejected / protected branch | You committed on `main`. `main` only accepts changes through PRs. Don't force anything: raise your hand and the instructor will help move your commit. |
| Workshop check is red | Click **Details** and read the message. Usually you changed a file other than `ATTENDEES.md`. Undo that change, commit, and push again. |
| "Please tell me who you are" when committing | Run the two `git config --global` lines from [SETUP.md](SETUP.md). |
| A browser sign-in pops up on push | Click **Allow** / **Authorize**. |
| Nothing to stage | You didn't save the file. Press `Ctrl+S` / `Cmd+S`. |

---

## Lab 2: Resolve a merge conflict

**Goal:** bring the latest `main` into your branch and fix the conflict.

**Why is there a conflict?** Everyone added their line in the **same spot**, right under the marker. Once some PRs are merged, `main` has other people's lines exactly where yours goes. Git can't know which line should come first, so it stops and asks you. A conflict isn't an error; it's a question.

Your PR page will say **"This branch has conflicts that must be resolved."**

1. **Make sure you're on your branch** (`name/<your-username>` in the status bar).
2. **Fetch the latest from GitHub.**
   - In VS Code: Source Control → **…** → **Fetch**.
   - Or in the terminal: `git fetch`
3. **Merge `origin/main` into your branch.**
   - In VS Code: Source Control → **…** → **Branch** → **Merge…** → choose `origin/main`. (Or Command Palette → **Git: Merge Branch…**.)
   - Or in the terminal: `git pull origin main` (fetches and merges in one step)
4. **Open `ATTENDEES.md`.** You'll see conflict markers:

   ```
   <<<<<<< HEAD
   - Your Name (@you) — your major
   =======
   - Someone Else (@them) — their major
   >>>>>>> origin/main
   ```

   *Current* (top) is your branch; *Incoming* (bottom) is what's on `main`.
5. **Resolve it: keep every line, remove nothing.**
   - In VS Code: click **Accept Both Changes** above the conflict. If you opened the **Merge Editor** instead, choose **Accept Combination** (or tick both sides), then **Complete Merge**.
   - Or by hand: delete only the three marker lines (`<<<<<<<`, `=======`, `>>>>>>>`) and keep all the names.
   - Check: every name is still there, and no `<<<<<<<` / `=======` / `>>>>>>>` lines are left. Save the file.
6. **Stage and commit the merge.**
   - In VS Code: click **+** on `ATTENDEES.md`, then **Commit** (the message is pre-filled, like `Merge remote-tracking branch 'origin/main' into name/octocat`).
   - Or in the terminal: `git add ATTENDEES.md` then `git commit` (saves the default message; in the editor that opens, just save and close)
7. **Push.**
   - In VS Code: **Sync Changes**.
   - Or in the terminal: `git push`
8. **Look at your PR.** It updates by itself. The conflict message disappears and the **Workshop check** runs again.

If more PRs get merged before yours, you may conflict again. That's normal: repeat from step 2.

**Fallback:** on your PR page, click **Resolve conflicts**. GitHub shows the same markers in a web editor. Delete only the marker lines, keep every name, click **Mark as resolved** → **Commit merge**.

**What you just learned:** a conflict happens when two branches change the same lines. You resolve it by editing the file to what it *should* be, then committing.

| Problem | Fix |
|---|---|
| No conflict happened | Either your PR was merged already, or nobody's had been yet. Help a neighbor. |
| `origin/main` isn't in the merge list | Do the **Fetch** step first. |
| I accidentally deleted someone's line | Add it back (copy it from `main` on GitHub), save, commit, push. |
| Check is red after the merge | Click **Details**. Most often a leftover `<<<<<<<` line or a changed file other than `ATTENDEES.md`. |
| Terminal opened a strange editor (Vim) on commit | Type `:wq` and press Enter to save and close. |

---

## Demo: history and undo (instructor)

Watch, no typing needed.

- **See history.**
  - In VS Code: Source Control → **Graph** shows every commit and branch. In Explorer, the **Timeline** section shows one file's history.
  - Or in the terminal: `git log --oneline --graph`
- **Undo a commit that's already pushed:** `git revert <sha>` (the `sha` is the commit ID from the log, e.g. `3f2a9c1`). It adds a **new** commit that undoes the old one, so history stays honest and nobody else's copy breaks.
- **Throw away edits you haven't committed:** VS Code **Discard Changes** (↶) / `git restore <file>`. This is permanent.
- **Unstage a file:** VS Code **−** / `git restore --staged <file>`.
- **`git reset` exists.** It rewrites history. Be careful, and never use it on a branch others are using.

**What you just learned:** committed work is almost never lost, and `revert` is the safe undo.

---

## Lab 3: Fix a bug

**Goal:** the full team workflow: claim an issue, branch, fix, open a PR that passes an automatic check, and review someone else's work.

The repo has 50 small bugs: Python (bugs 01–17), JavaScript (18–34), and C++ (35–50). Each one is a **one-line fix**. You don't need to know the language: read the summary and the hint.

> **Two different numbers!** The **bug number** is in the title, like `[Bug 07]`. The **issue number** is GitHub's `#` number, like `#23`. The branch uses the bug number; `Closes` uses the issue number.

1. **Pick an issue.** On GitHub, open the **Issues** tab. Click **Labels** and choose `workshop-bug`, and optionally a language (`python`, `javascript`, `cpp`). Pick one with **no assignee** (no avatar on the right).
2. **Assign yourself.** Open the issue. In the right sidebar, under **Assignees**, click **assign yourself**. Now nobody else will take it.
3. **Start from an up-to-date `main`.**
   - In VS Code: click the branch name → pick `main`. Then **…** → **Pull**.
   - Or in the terminal: `git switch main` then `git pull`
4. **Create the branch `fix/bug-NN`** with the two-digit bug number, exactly. Bug 7 → `fix/bug-07`. (A suffix is allowed: `fix/bug-07-ana`.)
   - In VS Code: branch name → **+ Create new branch…** → `fix/bug-07`.
   - Or in the terminal: `git switch -c fix/bug-07`
5. **Fix the bug.** The issue names the file, inside `exercises/<language>/bug-NN/`. Edit **only that one file**. Don't touch the test file or `bug.json`. Save.
6. **(Optional) Test it locally.**
   - In the terminal: `python scripts/run_bug_test.py bug-07` (on macOS you may need `python3`).
   - This only works if that language is installed on your computer (Python, Node.js, or a C++ compiler). Skip it if not: the GitHub check runs the same test for you.
7. **Commit** with a message like `Fix bug 07: use >= instead of > in the limit check` (say what you changed).
   - In VS Code: **+** to stage, type the message, **Commit**.
   - Or in the terminal: `git add exercises/<language>/bug-07/<file>` then `git commit -m "Fix bug 07: …"`
8. **Publish the branch.**
   - In VS Code: **Publish Branch**.
   - Or in the terminal: `git push -u origin fix/bug-07`
9. **Open a pull request** (**Compare & pull request**). In the description, write `Closes #<issue number>`, e.g. `Closes #23`. When the PR is merged, GitHub closes that issue automatically.
10. **Watch the Workshop check.** It runs the bug's tests.
    - **Red ✗:** click **Details** and read the message. It tells you whether the tests failed (fix isn't right yet) or you changed a file you shouldn't have. Fix it, commit, and push again. **The same PR updates automatically**; don't open a new one.
    - **Green ✓:** request a review. On the PR's right sidebar, click **Reviewers** and pick a classmate.
11. **Review a classmate's PR.** Open **Pull requests**, pick someone else's, and click **Files changed**. Hover a line and click **+** to leave a comment, or click **Review changes** → **Approve** (or **Comment**) → **Submit review**. Be kind and specific.
12. **The instructor merges** green PRs. Your issue closes itself.

**What you just learned:** issues track work, branches isolate it, checks catch mistakes automatically, and review gets a second pair of eyes before anything reaches `main`.

| Problem | Fix |
|---|---|
| Check fails because of the branch name | It must be `fix/bug-NN` with two digits and the bug number (not the issue number). Create a correctly named branch from your current one, publish it, and open a new PR (close the old one). Or ask the instructor. |
| Check says I changed files I shouldn't have | Only the one file named in the issue may change. Use **Discard Changes** on the others (or put back what you deleted), commit, push. |
| Check says tests failed | Read the failing test's message in **Details**. Re-read the hint. Change your line, commit, push. |
| My fix accidentally went on `main` or the wrong branch | Don't push. Raise your hand: the instructor will help. |
| Someone else already fixed my bug | Pick another unassigned issue. There are more bugs than people. |
| `run_bug_test.py` says the language isn't installed | That's fine. Rely on the GitHub check. |
| Can't approve a PR | You can't approve your own. Pick a classmate's. |

---

Done with everything? Try another bug in a language you've never used, or read this repo's [README](README.md) as an example of a good one.
