from pathlib import Path
from datetime import datetime
import argparse
import re

OUT_DIR = Path("workspace/Melina/out")


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9._-]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("._-")
    return text or "report"


def save_report(title: str, body: str) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = OUT_DIR / f"{ts}_{slugify(title)}.md"
    path.write_text(body, encoding="utf-8")
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--body", required=True)
    args = parser.parse_args()

    out = save_report(args.title, args.body)
    print(str(out))
