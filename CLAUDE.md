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
| `assets/social-preview.html` and `.png` | Social preview of the repo (1280x640, rendered at 2x). Rebuilt from the HTML with Chrome headless. |
| `assets/social-preview-upload.jpg` | Same card as JPEG under 1 MB, for the manual upload in Settings, Social preview (GitHub's limit). |
| `page/index.html` | Copy of the published presentation page, with `exemplo-matriz.png` beside it. |
| `fila-de-prioridades.skill` | Zip of `skills/fila-de-prioridades`, for installing without a terminal. Rebuild after any change to the skill. |

## What NOT to edit

Nothing in this repo is auto-generated. Every file is hand-maintained. Keep the SKILL.md frontmatter (`name`, `description`) intact — `npx skills` and the Claude plugin loader both parse it.

## Voice

README and SKILL.md stay terse and direct. No marketing fluff. The Before/After table ships the value in 5 seconds of scan.

## License

MIT. Contributions welcome. See CONTRIBUTING.md.
