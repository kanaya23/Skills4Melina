---
name: browser-use-downloads
description: Reach real downloadable files or final media targets through browser interaction and prepare them for reuse or Discord sending.
---

Use this skill when the user wants:
- an image
- a PDF
- a downloadable file
- a document
- a real media asset
- a site-generated export

Goal:
- Reach the actual downloadable artifact or final content page, not just a search result or thumbnail page.

In MelinaClaw, finish download flows with a recorded artifact and expose it through `/api/files`.

Workflow:
1. Discover the target page or result.
2. Open the result and verify it is the intended target.
3. If the site provides a direct download or openable asset, use that path.
4. If the file lands in a temporary or browser-default directory, move or copy it into `workspace/Melina/out/`.
5. Verify the file exists and has a reasonable filename and extension.
6. Send or reference the normalized output file.

Rules:
- Prefer the original file over screenshots of the page containing it.
- Prefer the final content page over a generic search page.
- If multiple candidate files exist, pick the one best matching the request.
- If the file cannot be directly downloaded, provide the best alternative: final page link, extracted info, or screenshot depending on what remains possible.
