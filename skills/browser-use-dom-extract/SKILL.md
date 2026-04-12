---
name: browser-use-dom-extract
description: Extract useful visible context from rendered pages after navigation and interaction.
---

Use this skill when the user wants readable page content rather than a screenshot.

Prefer `computer_use_extract` (mode `text` or `dom`) after deterministic navigation.

What to extract:
- page title
- major headings
- visible paragraphs
- list items
- result cards
- prices, labels, and short metadata
- visible links when they matter to the task

Goals:
- extract only what matters
- remove obvious page noise
- keep output readable
- save long results into a reusable artifact

Workflow:
1. Reach the correct page first.
2. Interact if needed: expand sections, scroll, switch tabs, wait for content.
3. Extract visible content relevant to the request.
4. Ignore obvious boilerplate when possible.
5. Return a concise inline answer or save a Markdown/text artifact if the output is long.

Output rules:
- if the result is short, summarize inline
- if the result is medium or long, save a Markdown or text file
- preserve important names, labels, links, and visible values
- preserve source URLs when useful
- when comparing multiple pages, normalize fields so they line up cleanly
- do not dump raw source unless specifically requested

Prefer:
- focused extraction
- clean and compact Markdown
- structured lists or simple key-value results

Avoid:
- giant unfiltered page dumps
- screenshot-only output when text is the real goal
- extracting before the relevant content is actually visible
