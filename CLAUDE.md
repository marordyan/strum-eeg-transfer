# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository state

This repo currently contains only `README.md`. Per that README, it is a scratch repository for learning GitHub and testing editor/GitHub integrations — there is no source code, build system, dependency manifest, test suite, or linter configured.

Consequences for working here:

- There are no build, test, or lint commands. Do not assume a toolchain exists; check for a manifest (`package.json`, `pyproject.toml`, `Cargo.toml`, etc.) before suggesting or running one.
- When adding the first real code, also introduce its toolchain, then update this file with the concrete build/test/lint commands (including how to run a single test).

## Git workflow

- Default branch is `master` (not `main`); target it for PRs.
- History shows work merged via pull request from topic branches (e.g. `readme-edits`) rather than direct commits to `master`. Follow that pattern: branch, push, open a PR.
