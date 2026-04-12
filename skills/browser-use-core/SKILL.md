---
name: browser-use-core
description: Full browser automation for navigation, interaction, visible-page reading, extraction, and artifact completion.
---

Use this skill whenever the user needs a real browser session rather than a simple HTTP fetch or shell command.

MelinaClaw action contract:
- start with `computer_use_start`
- perform browser work only via `computer_use_*` typed actions
- never route browser automation through `sh_exec`

Browser-use is for:
- searching when direct URLs are unknown
- opening and navigating sites
- clicking links, buttons, tabs, menus, accordions, and result cards
- typing into search boxes and forms
- scrolling and waiting for lazy-loaded content
- reading visible rendered content
- following multi-step flows
- reaching downloadable files or final media assets
- taking screenshots when screenshots are actually the right output
- confirming a real end state

Core principles:
- Complete the user's actual browser task, not just the first visible action.
- Operate on user-visible page state whenever possible.
- Prefer resilient, readable interaction over brittle assumptions.
- Treat screenshots as one output type, not the default output type.
- Keep focus on the final destination: answer, page, artifact, or confirmed submitted state.

When to use:
- The user asks to browse, search, inspect, open, retrieve, click through, or get something from a website.
- The target page is dynamic or interactive.
- Static fetching is insufficient because rendering or interaction is needed.

When not to stop:
- after opening a search engine
- after the first screenshot
- after landing on a generic homepage if the target is deeper
- after reading only a snippet if the real page can be opened
- after one failed action if another route is available

Default workflow:
1. Preflight
   - Ensure browser/display is available.
   - Clarify the target if needed.
   - Prefer the direct URL when known.

2. Reach the target
   - Search only when needed.
   - Open the most relevant page.
   - Move off result pages toward the final destination.

3. Interact
   - Click, scroll, type, filter, expand, and wait as required.
   - Follow the page structure logically.
   - Switch tabs/windows when the site opens them.

4. Evaluate state
   - Ask: am I on the final page yet?
   - If not, identify the missing step or blocker.

5. Acquire output
   - Extract the relevant information, confirm the state change, or obtain the final artifact.
   - If the result is long, save it to a file under `workspace/Melina/out/`.

6. Normalize output
   - Save or copy final files into `workspace/Melina/out/`.
   - Use normalized names.
   - Verify the file exists before sending.

Good outputs:
- final page answer
- extracted structured notes
- real file or media asset
- confirmed form result
- screenshot only when visually required

Bad outputs:
- screenshot of a search page when the answer is on the result page
- "I opened the website" with no completion
- unfinished navigation
- raw temp file paths sent directly to Discord
