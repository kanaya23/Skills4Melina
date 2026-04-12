from pathlib import Path
from datetime import datetime
import argparse
import re

DEFAULT_OUT = Path("workspace/Melina/out")


def slugify(name: str) -> str:
    name = name.strip().lower()
    name = re.sub(r"[^a-z0-9._-]+", "_", name)
    name = re.sub(r"_+", "_", name).strip("._-")
    return name or "artifact"


def save_text_artifact(title: str, content: str, suffix: str = ".md") -> Path:
    DEFAULT_OUT.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{ts}_{slugify(title)}{suffix}"
    path = DEFAULT_OUT / filename
    path.write_text(content, encoding="utf-8")
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--content", required=True)
    parser.add_argument("--suffix", default=".md")
    args = parser.parse_args()

    out = save_text_artifact(args.title, args.content, args.suffix)
    print(str(out))
