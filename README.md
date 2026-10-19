# Git & GitHub Workshop

[![Slides](https://img.shields.io/badge/slides-GitHub%20Pages-2f6fde)](https://texbonham.github.io/GithubWorkshop/)
[![Workshop check](https://github.com/TexBonham/GithubWorkshop/actions/workflows/check-fixes.yml/badge.svg)](https://github.com/TexBonham/GithubWorkshop/actions/workflows/check-fixes.yml)

Welcome! This repository is the classroom for a 72-minute, hands-on introduction to Git and GitHub for undergraduates. No experience needed: you'll work in VS Code, make real commits, open real pull requests, fix a merge conflict, and fix a small bug that an automated check verifies. Everything happens right here, in this shared repo.

## Start here

| | |
|---|---|
| **1. [SETUP.md](SETUP.md)** | **Do this before the workshop!** Accounts, installing Git and VS Code, signing in. |
| **2. [Slides](https://texbonham.github.io/GithubWorkshop/)** | The presentation. Use the arrow keys, or swipe on a phone. |
| **3. [LABS.md](LABS.md)** | Step-by-step instructions for every hands-on lab. |
| **4. [Cheat sheet](https://texbonham.github.io/GithubWorkshop/cheatsheet.html)** | One printable page: VS Code buttons next to Git commands, plus "I'm stuck" fixes. |

## Agenda

| Minutes | Topic | Format |
|---:|---|---|
| 0–10 | What Git and GitHub are, and why version control matters | slides |
| 10–15 | Clone this repo in VS Code and take a tour | follow-along |
| 15–30 | **Lab 1:** branch, add your name to `ATTENDEES.md`, commit, push, pull request | hands-on |
| 30–40 | **Lab 2:** your PR has a merge conflict; resolve it | hands-on |
| 40–45 | Viewing history and undoing with `git revert` | demo |
| 45–60 | **Lab 3:** claim a bug issue, fix it, pass the check, review a classmate | hands-on |
| 60–70 | Engineering projects: READMEs, organizing files, `.gitignore`, team habits | slides |
| 70–72 | Interest poll for a long-term project workshop | poll |

## What's in this repo

| Path | What it is |
|---|---|
| [`ATTENDEES.md`](ATTENDEES.md) | The guestbook you edit in Labs 1 and 2 |
| [`exercises/`](exercises/) | 50 small bugs (Python, JavaScript, C++), one folder each, used in Lab 3 |
| [`scripts/`](scripts/) | Helper scripts: run a bug's tests locally, the automated PR check, instructor tools |
| [`.github/`](.github/) | The GitHub Actions workflow that runs the **Workshop check** on every pull request |
| [`docs/`](docs/) | The slides and cheat sheet, published with GitHub Pages |
| [`LABS.md`](LABS.md), [`SETUP.md`](SETUP.md) | Lab guide and setup checklist |

## Found a bug?

That's the point! The code in `exercises/` is broken **on purpose**. Each bug has an issue labeled `workshop-bug`. See [Lab 3](LABS.md#lab-3-fix-a-bug) to claim one and fix it.

For anything else (a typo in the slides, a confusing step), please [open an issue](https://github.com/TexBonham/GithubWorkshop/issues/new).

## This README is an example

Notice how this file is built: a title, a one-paragraph summary, links to what matters most, tables for structured info, and a short map of the project. Your own project READMEs (class projects, senior design, portfolio) can follow the same shape. It's written in [Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
