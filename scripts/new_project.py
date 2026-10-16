#!/usr/bin/env python3
"""Create a video project workspace by copying the project template."""
from __future__ import annotations
import argparse
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "project"
PROJECTS = ROOT / "projects"

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", dest="project_id", help="Project ID, e.g. BV-20261016-001")
    parser.add_argument("--title", default="", help="Working title")
    args = parser.parse_args()

    PROJECTS.mkdir(parents=True, exist_ok=True)
    if args.project_id:
        project_id = args.project_id
    else:
        day_prefix = f"BV-{datetime.now().strftime('%Y%m%d')}-"
        existing = [p.name for p in PROJECTS.iterdir() if p.is_dir() and p.name.startswith(day_prefix)]
        numbers = []
        for name in existing:
            match = re.fullmatch(re.escape(day_prefix) + r"(\d{3,})", name)
            if match:
                numbers.append(int(match.group(1)))
        project_id = f"{day_prefix}{max(numbers, default=0) + 1:03d}"

    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{2,80}", project_id):
        parser.error("Project ID may contain only letters, numbers, dot, underscore and hyphen.")
    destination = PROJECTS / project_id
    if destination.exists():
        parser.error(f"Project already exists: {destination}")
    if not TEMPLATE.is_dir():
        parser.error(f"Template directory missing: {TEMPLATE}")

    shutil.copytree(TEMPLATE, destination)
    state_path = destination / "project_state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).isoformat()
    state.update({
        "project_id": project_id,
        "created_at": now,
        "updated_at": now,
        "status": "DISCOVER",
        "current_stage": "DISCOVER",
        "next_action": "Run book discovery and verify candidates."
    })
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.title:
        (destination / "PROJECT_TITLE.txt").write_text(args.title.strip() + "\n", encoding="utf-8")
    print(f"Created project: {destination.relative_to(ROOT)}")
    print("Next: read START_HERE.md and execute skills/book-discovery/SKILL.md")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
