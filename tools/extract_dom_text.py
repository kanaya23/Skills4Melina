from pathlib import Path
import argparse
import json
import re
from bs4 import BeautifulSoup

OUT_DIR = Path("workspace/Melina/out")


def clean_text(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_from_html(html: str, max_items: int = 200) -> dict:
    soup = BeautifulSoup(html, "lxml")

    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()

    title = clean_text(soup.title.get_text(" ", strip=True)) if soup.title else ""

    headings = []
    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = clean_text(tag.get_text(" ", strip=True))
        if text:
            headings.append(text)

    paragraphs = []
    for tag in soup.find_all(["p", "li"]):
        text = clean_text(tag.get_text(" ", strip=True))
        if text and len(text) >= 20:
            paragraphs.append(text)

    links = []
    for a in soup.find_all("a", href=True):
        text = clean_text(a.get_text(" ", strip=True))
        href = clean_text(a["href"])
        if text or href:
            links.append({"text": text, "href": href})

    return {
        "title": title,
        "headings": headings[:max_items],
        "paragraphs": paragraphs[:max_items],
        "links": links[:max_items],
    }


def to_markdown(data: dict) -> str:
    lines = []

    if data.get("title"):
        lines += [f"# {data['title']}", ""]

    if data.get("headings"):
        lines += ["## Headings", ""]
        lines += [f"- {x}" for x in data["headings"]]
        lines += [""]

    if data.get("paragraphs"):
        lines += ["## Content", ""]
        lines += [f"- {x}" for x in data["paragraphs"]]
        lines += [""]

    if data.get("links"):
        lines += ["## Links", ""]
        lines += [f"- {(x.get('text') or '(no text)')} -> {x.get('href') or ''}" for x in data["links"]]
        lines += [""]

    return "\n".join(lines).strip() + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to saved HTML file")
    parser.add_argument("--format", choices=["json", "md"], default="md")
    parser.add_argument("--output", default="", help="Optional explicit output path")
    parser.add_argument("--max-items", type=int, default=200)
    args = parser.parse_args()

    html_path = Path(args.input)
    if not html_path.exists():
        raise FileNotFoundError(f"Missing input: {html_path}")

    html = html_path.read_text(encoding="utf-8", errors="replace")
    data = extract_from_html(html, max_items=args.max_items)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.output:
        out_path = Path(args.output)
    else:
        out_path = OUT_DIR / f"{html_path.stem}_dom_extract.{args.format}"

    if args.format == "json":
        out_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    else:
        out_path.write_text(to_markdown(data), encoding="utf-8")

    print(str(out_path))


if __name__ == "__main__":
    main()
