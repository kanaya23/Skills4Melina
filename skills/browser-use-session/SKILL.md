---
name: browser-use-session
description: Manage full browser sessions including preflight, page transitions, retries, waiting, and multi-step task completion.
---

Use this skill when the browser task is longer than a single page load or requires multiple interactions.

Session lifecycle should map to typed calls: `computer_use_start` -> interaction -> `computer_use_close`.

What this skill is for:
- Multi-step browsing
- Search -> open result -> inspect -> continue
- Login or session-aware tasks when credentials/session are available
- Pages with lazy loading, tabs, expanders, or dynamic sections
- Workflows that require retries, backtracking, or alternate routes

Session principles:
- Keep a clear goal for the session.
- Track where you are in the flow: source page, intermediate page, target page, artifact page.
- Do not repeatedly perform the same failing action without changing strategy.
- Wait intelligently for dynamic content instead of assuming failure too early.
- If a flow opens a new tab or window, continue on the correct destination rather than getting stranded.

Standard session workflow:
1. Preflight
   - Ensure browser/display is available.
   - Prefer a direct URL if known.
   - If the user gave a site and target, use both.

2. Establish starting point
   - Open the most direct page available.
   - If discovery is needed, search first, then move off the search page.

3. Navigate deliberately
   - Use clicks, typing, scrolling, filtering, and tab switching as needed.
   - Expand collapsed sections or load more content when relevant.
   - Wait for the page state to settle before evaluating results.

4. Evaluate progress
   - Ask: am I at the final target yet?
   - If not, identify the blocker: wrong page, challenge page, missing selector, loading issue, session issue.

5. Retry with a changed strategy
   - Use a different selector path, alternate source, different search phrasing, or alternate route.
   - Avoid blind repetition.

6. Complete the task
   - Extract the needed data, confirm the form result, or download the requested file.
   - Normalize output under `workspace/Melina/out/` when applicable.

7. Report minimally but usefully
   - Return the final result, or a concise blocker if the task cannot proceed.

Rules:
- A browser session is complete only when the user’s actual intent is satisfied, not when the first screenshot exists.
- Use screenshots for confirmation or fallback, not as the default completion criterion.
- When the page is interactive, prefer meaningful interaction over static capture.
