---
name: browser-use-navigation
description: Navigate websites reliably through search, result selection, page traversal, tabs, scrolling, and alternate routes.
---

Use this skill when the main challenge is getting from the starting page to the real target.

Use typed tools only: `computer_use_open_url`, `computer_use_click`, `computer_use_scroll`, `computer_use_focus`, `computer_use_list_windows`.

Use cases:
- search engine to target page
- home page to deep content page
- listing page to item detail page
- result grid to real media page
- multi-step navigation through tabs, menus, and expanders

Goals:
- reach the intended destination efficiently
- avoid getting stuck on intermediates
- choose the correct result among similar options
- keep navigation understandable and deliberate

Navigation workflow:
1. Start with the most direct known URL or search query.
2. Identify likely target links by visible title, snippet, domain, or surrounding context.
3. Open the best candidate and verify it matches the request.
4. Continue deeper if the target is not yet reached.
5. Scroll and expand only when that reveals relevant navigation or content.
6. If a route fails, choose a different route rather than repeating the same click.

Selection rules:
- prefer the official or most directly relevant source
- prefer titles that closely match the requested entity
- prefer final content pages over category or index pages
- prefer openable detail pages over thumbnails or snippets
- when multiple candidates are plausible, verify before committing

Tab and window rules:
- if a click opens a new tab, continue on the tab containing the target
- do not lose track of the source page if it remains useful
- close or ignore irrelevant tabs when they distract from the task

Stop conditions:
- the correct final page is open
- the requested artifact is reached
- the answer is fully extractable from the current page
- a meaningful blocker remains after trying another route

Avoid:
- repeated blind retries
- stopping at a search result screenshot
- opening many irrelevant pages without validating them
