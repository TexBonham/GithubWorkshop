# Setup

- **Part A** is for **attendees**. Please do it **before** the workshop (about 20 minutes).
- **Part B** is the **instructor** checklist.

---

## Part A: Attendee pre-workshop checklist

Tick each box as you go. Linux users: the steps are the same idea with your package manager; you'll manage.

### Everyone (any computer)

- [ ] **Create a GitHub account** at <https://github.com/signup>. Pick a username you'd be happy to show an employer.
- [ ] **Students: apply for the free [GitHub Student Developer Pack](https://education.github.com/pack)** with your school email. Approval can take a few days, so do it early.
- [ ] **Accept the collaborator invite.** You'll get an email from GitHub inviting you to `TexBonham/GithubWorkshop`. Click **Accept**, or go to <https://github.com/TexBonham/GithubWorkshop/invitations> while signed in. Without this you can't push branches during the labs.

### Windows

- [ ] **Install Git** from <https://git-scm.com/download/win>. Run the installer and keep **all the default options** (just click Next). This also installs *Git Credential Manager*, which handles signing in for you.
- [ ] **Install VS Code** from <https://code.visualstudio.com/>. Defaults are fine. Ticking "Add to PATH" is helpful.
- [ ] **Open a terminal**: in VS Code, **Terminal → New Terminal**. Check Git works:

  ```
  git --version
  ```

  You should see something like `git version 2.x`. If it says "not recognized", quit VS Code completely and reopen it.

### macOS

- [ ] **Install Git.** Open **Terminal** (Applications → Utilities) and run:

  ```
  xcode-select --install
  ```

  Click **Install** in the pop-up. (Alternative: the installer at <https://git-scm.com/download/mac>.)
- [ ] **Install VS Code** from <https://code.visualstudio.com/>. Drag it into your **Applications** folder.
- [ ] **Check Git works**: in VS Code, **Terminal → New Terminal**, then:

  ```
  git --version
  ```

### Everyone: configure Git and sign in

- [ ] **Tell Git your name and email** (once per computer). In the VS Code terminal:

  ```
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"
  ```

  Use the email on your GitHub account, **or** GitHub's private *noreply* address if you'd rather keep your email hidden: on GitHub go to **Settings → Emails**; it looks like `12345678+username@users.noreply.github.com`.
  Check with `git config --global --list`.
- [ ] **Sign in to GitHub in VS Code.** Click the **Accounts** icon (the person at the bottom of the left bar) → **Sign in with GitHub** (it may say "Backup and Sync Settings" or similar; any GitHub sign-in option works). A browser opens: click **Allow** / **Authorize**. No SSH keys or tokens are needed.
- [ ] **Test it by cloning the workshop repo.** Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) → **Git: Clone** → paste `https://github.com/TexBonham/GithubWorkshop` → choose a folder → **Open**. If you see the files, you're ready. (If a browser asks you to authorize Git Credential Manager, click **Allow**.)

**Stuck?** Come 10 minutes early and we'll fix it together. Don't worry about understanding anything yet; that's what the workshop is for.

---

## Part B: Instructor checklist

Do these in order. Settings pages are under the repo's **Settings** tab (admin only).

### About a week before

- [ ] **Add collaborators.** Settings → **Collaborators** → **Add people** → each attendee's GitHub username (about 30), role **Write**. Invites expire after 7 days, so send them roughly a week ahead and re-send for anyone who hasn't accepted. Point attendees to Part A.
- [ ] **Turn on GitHub Pages.** Settings → **Pages** → Source: **Deploy from a branch** → Branch: `main`, folder: `/docs` → **Save**. After a minute the slides are live at <https://texbonham.github.io/GithubWorkshop/>.
- [ ] **Turn on Discussions and create the poll.** Settings → **General** → Features → tick **Discussions**. Then **Discussions** tab → **New discussion** → category **Polls** → ask about interest in a long-term (biweekly / monthly) group workshop building a large-scale resume project, with options such as *Biweekly*, *Monthly*, *Interested but not sure of schedule*, *Not right now*. Copy the discussion's URL into `POLL_URL` in [`docs/js/config.js`](docs/js/config.js) and commit. The last slide turns it into a QR code.
- [ ] **Protect `main` with a ruleset.** Settings → **Rules** → **Rulesets** → **New ruleset** → **New branch ruleset**:
  - Name: `protect main`; Enforcement status: **Active**.
  - **Bypass list** → Add bypass → **Repository admin** (so you can merge and fix things).
  - **Target branches** → Add target → **Include default branch** (`main`).
  - Rules:
    - **Restrict deletions** (on).
    - **Require a pull request before merging** → Required approvals: **0** (so attendees are never blocked waiting for a review).
    - **Require status checks to pass** → Add checks → `Workshop check` (source: GitHub Actions). If it doesn't appear in the search, open one test PR first so the check has run once, then come back.
    - **Block force pushes** (on).
  - **Create**.

### After all materials are committed

- [ ] **Tag the pristine state** that `reset.py` restores to:

  ```
  git tag workshop-pristine
  git push origin workshop-pristine
  ```

- [ ] **Create the 50 bug issues.** Dry run first, then for real (it's idempotent, so re-running is safe):

  ```
  python scripts/create_issues.py
  python scripts/create_issues.py --yes
  ```

- [ ] **Dry-run every lab with a test account** (a second GitHub account added as a collaborator): Lab 0 clone, Lab 1 PR goes green, merge a different PR so Lab 2 really conflicts and resolves, Lab 3 with a wrong fix (red), then the right fix (green), and a review. Check the slides on a phone too.
- [ ] Print copies of the [cheat sheet](https://texbonham.github.io/GithubWorkshop/cheatsheet.html) (optional).

### On the day

- Open the slides, press **F** for fullscreen, **N** for speaker notes (timing cues are in the notes), **T** to reset the clock when you start.
- Lab 1: wait ~8 minutes before merging any PRs, then merge green ones in small batches; this is what creates the Lab 2 conflicts.
- Keep merging green PRs through Labs 2 and 3.

### After the workshop

- [ ] **Reset the repo** for next time. Dry run first:

  ```
  python scripts/reset.py
  python scripts/reset.py --yes
  ```
