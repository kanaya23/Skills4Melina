---
name: browser-use-forms
description: Use browser automation to fill inputs, submit forms, handle multi-step UI flows, and confirm outcomes.
---

Use this skill for:
- search boxes
- login pages when credentials/session are available
- forms
- filters
- settings changes
- multi-step site actions

Use typed actions for forms: `computer_use_click`, `computer_use_type`, `computer_use_keypress`, `computer_use_wait`.

Form interaction rules:
- Understand the target action before typing.
- Fill only the fields needed for the task.
- Confirm the effect of submission instead of assuming success.
- If there is validation feedback, read and react to it.
- Avoid duplicate submissions caused by impatience.

Workflow:
1. Reach the correct form or input.
2. Identify the required fields and controls.
3. Fill them carefully.
4. Submit once.
5. Wait for resulting state change, success indicator, redirect, or explicit error.
6. Continue only if the post-submit page still requires action.

Good completion criteria:
- Success message visible
- Redirect to expected page
- Changed state visible
- Submitted resource appears in the UI
- Clear error captured if submission failed

Bad completion criteria:
- "I typed into the field"
- "I clicked submit" with no confirmation
- Screenshot of an unfinished form
