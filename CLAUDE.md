# CLAUDE.md — fila-de-prioridades

## What this repo is

A single Claude skill distributed as a public GitHub repo. The single source of truth is `skills/fila-de-prioridades/SKILL.md`. Every behavioral change starts there.

## What to edit

| File | What it controls |
|------|------------------|
| `skills/fila-de-prioridades/SKILL.md` | Skill behavior — triggers, workflow, output format. The body the agent loads. |
| `skills/fila-de-prioridades/README.md` | Per-skill technical notes (install, files). |
| `README.md` (root) | Product front door. Optimize for non-technical readers. The Before/After table is the pitch. |
| `CONTRIBUTING.md` | How to contribute. |

## What NOT to edit

Nothing in this repo is auto-generated. Every file is hand-maintained. Keep the SKILL.md frontmatter (`name`, `description`) intact — `npx skills` and the Claude plugin loader both parse it.

## Voice

README and SKILL.md stay terse and direct. No marketing fluff. The Before/After table ships the value in 5 seconds of scan.

## License

MIT. Contributions welcome. See CONTRIBUTING.md.
