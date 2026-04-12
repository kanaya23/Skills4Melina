from pathlib import Path
from datetime import datetime
import argparse

DEFAULT_BASE = Path("workspace/Melina")
DEFAULT_JOURNAL_DIR = "Journal"


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def build_entry(ts: datetime, summary: str, actions: str, observations: str, blockers: str, next_steps: str) -> str:
    lines = [
        f"## {ts.strftime('%H:%M:%S')}",
        "",
        f"**Summary:** {summary.strip() or 'No major update.'}",
        f"**Key actions:** {actions.strip() or 'None noted.'}",
        f"**Observations:** {observations.strip() or 'None noted.'}",
        f"**Blockers:** {blockers.strip() or 'None noted.'}",
        f"**Next steps:** {next_steps.strip() or 'None noted.'}",
        "",
    ]
    return "\n".join(lines)


def write_daily_journal(
    base_dir: Path,
    summary: str,
    actions: str,
    observations: str,
    blockers: str,
    next_steps: str,
) -> Path:
    now = datetime.now()
    journal_dir = base_dir / DEFAULT_JOURNAL_DIR
    ensure_dir(journal_dir)

    day_file = journal_dir / f"{now.strftime('%Y-%m-%d')}.md"

    if not day_file.exists():
        day_file.write_text(
            "\n".join(
                [
                    f"# Journal — {now.strftime('%Y-%m-%d')}",
                    "",
                ]
            ),
            encoding="utf-8",
        )

    entry = build_entry(now, summary, actions, observations, blockers, next_steps)

    with day_file.open("a", encoding="utf-8") as f:
        if day_file.stat().st_size > 0:
            f.write("\n")
        f.write(entry)

    return day_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", default=str(DEFAULT_BASE))
    parser.add_argument("--summary", default="Routine daily journal entry.")
    parser.add_argument("--actions", default="")
    parser.add_argument("--observations", default="")
    parser.add_argument("--blockers", default="")
    parser.add_argument("--next-steps", default="")
    args = parser.parse_args()

    out = write_daily_journal(
        base_dir=Path(args.base_dir),
        summary=args.summary,
        actions=args.actions,
        observations=args.observations,
        blockers=args.blockers,
        next_steps=args.next_steps,
    )
    print(str(out))
