---
name: file-normalize
description: Normalize files for safe Discord sending by copying outputs into the agent out directory with clean names and preserved extensions.
---

Use this skill whenever a file was created in a temporary location, has a messy name, needs to be staged for sending, or should be made consistent before upload.

Goals:
- Ensure sendable artifacts live under `workspace/Melina/out/`.
- Avoid sending files directly from `/tmp`.
- Preserve the original extension unless conversion is explicitly required.
- Use clear, predictable filenames.
- Confirm the final file exists before attempting to send it.

Workflow:
1. Identify the source file.
2. If it is outside `workspace/Melina/out/`, copy it into `workspace/Melina/out/`.
3. Normalize the filename, keeping the extension.
4. Verify the copied file exists and is readable.
5. Send the normalized file path, not the original temporary path.

When available, use helper scripts from `workspace/Melina/tools/`, especially `make_sendable.py`.

Examples:
- `/tmp/jane_doe_search.png` -> `workspace/Melina/out/jane_doe_search.png`
- `/tmp/result.jpeg` -> `workspace/Melina/out/result.jpeg`

Never:
- Send directly from `/tmp`.
- Rename files to extensionless names.
- Overwrite unrelated files without intent.
