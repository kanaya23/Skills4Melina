---
name: browser-use-artifacts
description: Create useful browser-derived artifacts such as screenshots, extracted notes, page context files, and normalized sendable outputs.
---

Use this skill whenever a browser task should leave behind a reusable output file.

Primary artifact path in MelinaClaw is the runtime artifact registry; create visual artifacts with `computer_use_screenshot`.

Artifact types:
- screenshot
- markdown notes
- text extraction
- page HTML snapshot
- downloaded file
- normalized upload-ready output

Preferred artifact order:
1. real requested file or asset
2. extracted structured notes
3. page context capture
4. final-page screenshot
5. intermediate screenshot only as a fallback

Workflow:
1. Decide which artifact best answers the task.
2. Save it under `workspace/Melina/out/` if possible.
3. If created elsewhere, copy it into `workspace/Melina/out/`.
4. Use a clear file name.
5. Verify the file exists before sending.

Good artifact choices:
- article -> markdown notes
- multi-result comparison -> markdown or text report
- requested visual state -> screenshot
- downloadable PDF/image -> original file copied into out dir
- long extraction -> text artifact instead of chat flood
- dynamic page context -> HTML snapshot plus extracted summary

Bad artifact choices:
- screenshot of search results when the user wants the actual file
- temp path sent directly to Discord
- unreadable filename
- disposable proof artifact when a reusable structured file would be better
