## DOM Extraction Rules

- When a page contains the answer in visible text, prefer extracting the relevant DOM content over taking a screenshot.
- Extract only what is needed for the task: titles, headings, paragraphs, lists, prices, labels, links, and small metadata.
- Avoid dumping whole pages when a focused extract is enough.
- Remove obvious noise such as cookie banners, navigation chrome, footer clutter, and repeated boilerplate where possible.
- If the extracted result is long, save it as a Markdown or text artifact under `workspace/Melina/out/`.
- If the page is dynamic, scroll or interact first, then extract after the relevant content is visible.
