from pathlib import Path
import shutil
import re
import sys

AGENT_OUT = Path("workspace/Melina/out")


def slugify_filename(name: str) -> str:
    p = Path(name)
    stem = p.stem.strip().lower()
    suffix = p.suffix

    stem = re.sub(r"[^a-z0-9._-]+", "_", stem)
    stem = re.sub(r"_+", "_", stem).strip("._-")
    if not stem:
        stem = "file"

    return f"{stem}{suffix}"


def make_sendable(src_path: str, out_name: str | None = None) -> str:
    src = Path(src_path)
    if not src.exists():
        raise FileNotFoundError(f"Missing file: {src}")

    AGENT_OUT.mkdir(parents=True, exist_ok=True)

    final_name = out_name.strip() if out_name else slugify_filename(src.name)
    dst = AGENT_OUT / final_name

    if src.resolve() == dst.resolve():
        return str(dst)

    shutil.copy2(src, dst)
    return str(dst)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: python make_sendable.py <src> [out_name]")

    src = sys.argv[1]
    out_name = sys.argv[2] if len(sys.argv) > 2 else None
    print(make_sendable(src, out_name))
