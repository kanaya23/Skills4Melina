---
name: computer-use-core
description: Typed computer-use contract for MelinaClaw browser operation.
---

Use this skill whenever a task requires operating a website through deterministic typed actions.

Canonical action order:
1. `computer_use_start`
2. `computer_use_open_url`
3. interaction loop (`computer_use_click`, `computer_use_double_click`, `computer_use_type`, `computer_use_keypress`, `computer_use_scroll`, `computer_use_wait`)
4. read/extract (`computer_use_extract`, `computer_use_inspect_viewport`, `computer_use_list_windows`, `computer_use_focus`)
5. artifact (`computer_use_screenshot`)
6. cleanup (`computer_use_close`)

Rules:
- Do not use `sh_exec` for browser automation.
- Every long workflow must produce at least one explicit state update.
- Save outputs as artifacts; do not rely on transient console output.
- Prefer linear, inspectable step progression over implicit jumps.

