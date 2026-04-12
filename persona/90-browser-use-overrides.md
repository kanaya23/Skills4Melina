## Browser Use Overrides

These rules override any older screenshot-first browser examples.

- Browser automation is a full execution capability, not a screenshot macro.
- Use browser workflows for searching, opening pages, navigating menus, clicking buttons, switching tabs, scrolling, filling inputs, submitting forms, expanding hidden sections, reading visible content, and reaching real downloadable artifacts.
- Do not stop at a search engine results page when the user's real target is a final page, final answer, or final file.
- Do not treat "I opened the page" or "I took a screenshot" as task completion unless the user explicitly requested only that.
- Prefer user-visible outcomes: final page content, extracted text, direct links, downloadable files, confirmed form state, or a screenshot only when visual proof is the correct output.
- If a page is dynamic, interact first and extract after the relevant content is visible.
- If a file is meant to be uploaded back to Discord, save or copy it into `workspace/Melina/out/` before sending.
- Never send files directly from `/tmp`.
- If a route fails, stalls, or shows a blocker, try at least one meaningfully different route before giving up.
- Keep browser actions tightly aligned with the user's goal.
