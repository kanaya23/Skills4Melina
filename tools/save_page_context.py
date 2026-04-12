from pathlib import Path
from datetime import datetime
import argparse
import json
import re

from playwright.sync_api import sync_playwright

OUT_DIR = Path("workspace/Melina/out")


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9._-]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("._-")
    return text or "page"


def auto_scroll(page, step=1200, pause_ms=350, max_rounds=20):
    last_height = 0
    stable_rounds = 0

    for _ in range(max_rounds):
        page.evaluate(f"window.scrollBy(0, {step})")
        page.wait_for_timeout(pause_ms)
        height = page.evaluate("document.body.scrollHeight")

        if height == last_height:
            stable_rounds += 1
        else:
            stable_rounds = 0
            last_height = height

        if stable_rounds >= 2:
            break


def save_page_context(url: str, slug: str, wait_ms: int, do_scroll: bool, headless: bool):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    stem = f"{ts}_{slugify(slug)}"

    html_path = OUT_DIR / f"{stem}.html"
    png_path = OUT_DIR / f"{stem}.png"
    meta_path = OUT_DIR / f"{stem}.json"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page(viewport={"width": 1440, "height": 2200})
        page.goto(url, wait_until="domcontentloaded", timeout=90000)
        page.wait_for_timeout(wait_ms)

        if do_scroll:
            auto_scroll(page)

        page.wait_for_timeout(800)

        html = page.content()
        html_path.write_text(html, encoding="utf-8")
        page.screenshot(path=str(png_path), full_page=True)

        meta = {
            "requested_url": url,
            "final_url": page.url,
            "title": page.title(),
            "html_path": str(html_path),
            "screenshot_path": str(png_path),
        }
        meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
        browser.close()

    return html_path, png_path, meta_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--slug", default="page_context")
    parser.add_argument("--wait-ms", type=int, default=2500)
    parser.add_argument("--scroll", action="store_true")
    parser.add_argument("--headless", action="store_true")
    args = parser.parse_args()

    html_path, png_path, meta_path = save_page_context(
        url=args.url,
        slug=args.slug,
        wait_ms=args.wait_ms,
        do_scroll=args.scroll,
        headless=args.headless,
    )

    print(str(html_path))
    print(str(png_path))
    print(str(meta_path))
