---
name: browser-use-search
description: Use search engines and on-site search boxes to discover the right target page, then move from discovery to completion.
---

Use this skill when the user does not provide a direct URL or when the site has an internal search flow.

For MelinaClaw execution, search routing must still flow through `computer_use_open_url` and typed interaction tools.

Goals:
- turn vague user intent into the right target page
- avoid getting stuck at result pages
- choose the most relevant result efficiently

Workflow:
1. Decide whether to use a web search engine, the site's own search box, or both.
2. Search with concise, specific phrasing.
3. Review visible titles, snippets, domains, and page cues.
4. Open the best candidate.
5. Verify that it matches the requested entity or content.
6. Continue to the final page or artifact instead of stopping at discovery.

Search rules:
- prefer official or directly relevant domains first
- when looking for a file, prefer the file page or direct asset over a thumbnail page
- when looking for a profile, prefer the actual profile page over index or category pages
- when looking for documentation, prefer the exact doc page over generic homepages
- refine the query if the first result set is noisy

Completion rule:
- a search task is not complete when results are merely visible; it is complete when the target has been reached or the useful findings have been extracted cleanly
