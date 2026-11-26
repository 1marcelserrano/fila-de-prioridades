# Contributing to fila-de-prioridades

Thanks for considering a contribution.

## What to edit

Single source of truth: `skills/fila-de-prioridades/SKILL.md`. All behavior changes go there first. The root `README.md` is the product front door and updates after the skill body stabilizes.

## How to test locally

1. Clone the repo.
2. Copy `skills/fila-de-prioridades/` into your Claude skills directory:
   - macOS/Linux: `~/.claude/skills/`
3. Restart Claude or open a new chat.
4. Trigger the skill with one of the phrases from the README.

## PR guidelines

- **Conventional Commits** — `feat:`, `fix:`, `docs:`, `refactor:`
- **One concern per PR** — a docs fix and a behavior change go separately
- **Show before/after** for any SKILL.md body change — one sentence on why the new wording is better
- **Keep the README install table accurate** — a broken install command costs real users

## Issues

Bug or behavior gap? Use the issue templates in `.github/ISSUE_TEMPLATE/`. Be specific about input, expected output, and actual output.

## License

By contributing you agree your contributions are licensed under MIT.
