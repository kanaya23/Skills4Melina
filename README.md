# Skills4Melina

Repo-backed skills, persona fragments, helper tools, and dependency lists for Melina.

## Purpose
This repo is the external source of truth for:
- `skills/` → skill folders and `SKILL.md` files
- `tools/` → helper scripts callable by the agent
- `persona/` → appended persona fragments
- `requirements/apt.txt` → system packages
- `requirements/pip.txt` → Python packages

## Expected notebook flow
Cell 1.5 should:
1. Clone/update this repo.
2. Sync `skills/`, `tools/`, and `persona/`.
3. Install packages from `requirements/apt.txt` if present.
4. Install packages from `requirements/pip.txt` if present.
5. Write `workspace/Melina/persona_repo_append.md`.

Cell 2 should:
- Boot Freeclaw.
- Pull config and optional memory only.
- Not be responsible for skill definitions or dependency expansion.

## Rules
- Final files meant for Discord upload must be saved under `workspace/Melina/out/`.
- Do not send files directly from `/tmp`.
- Prefer actual extracted/downloaded artifacts over screenshots of intermediary pages.
