#!/usr/bin/env python3
"""Validate required ledgers and a project workspace without external dependencies."""
from __future__ import annotations
import argparse, csv, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_LEDGER_COLUMNS = {
    "books.csv": ["book_id", "title_original", "author", "quality_score", "evidence_status", "selection_status"],
    "video_projects.csv": ["project_id", "book_id", "working_title", "central_question", "status"],
    "book_decisions.csv": ["decision_id", "book_id", "decision_date", "decision_type", "total_score", "decision"],
}
REQUIRED_PROJECT_FILES = [
    "project_state.json", "01_book_discovery/candidates.md", "02_book_review/book_review.md",
    "03_topic/topic_brief.md", "04_research/evidence_ledger.md", "04_research/research_summary.md",
    "05_script/script.md", "05_script/scene_plan.json", "05_script/citation_map.md",
    "06_editorial/review_report.md", "07_production/production_manifest.json",
    "08_video_qa/qa_report.md", "09_metadata/title_options.md", "09_metadata/thumbnail_brief.md",
    "09_metadata/video_description.md", "09_metadata/metadata.json",
    "09_publish/private_verification.md", "10_analytics/analytics_review.md",
]

def validate_csv(path: Path, required: list[str]) -> list[str]:
    errors = []
    if not path.exists():
        return [f"Missing ledger: {path.relative_to(ROOT)}"]
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            actual = reader.fieldnames or []
            missing = [c for c in required if c not in actual]
            if missing: errors.append(f"{path.name}: missing columns: {', '.join(missing)}")
            rows = list(reader)
            key = actual[0] if actual else None
            if key:
                seen = set()
                for line_no, row in enumerate(rows, start=2):
                    value = (row.get(key) or "").strip()
                    if value and value in seen: errors.append(f"{path.name}:{line_no}: duplicate {key}={value}")
                    if value: seen.add(value)
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"{path.name}: cannot parse CSV: {exc}")
    return errors

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", help="Project ID or path under projects/")
    parser.add_argument("--ledgers-only", action="store_true", help="Validate ledgers only")
    args = parser.parse_args()
    errors = []
    for name, columns in REQUIRED_LEDGER_COLUMNS.items():
        errors.extend(validate_csv(ROOT / "data" / name, columns))
    if args.project and not args.ledgers_only:
        candidate = Path(args.project)
        project_path = candidate if candidate.is_absolute() else ROOT / "projects" / candidate
        if not project_path.is_dir(): errors.append(f"Project directory not found: {project_path}")
        else:
            for rel in REQUIRED_PROJECT_FILES:
                if not (project_path / rel).is_file(): errors.append(f"Missing project artifact: {rel}")
            for rel in ["project_state.json", "05_script/scene_plan.json", "07_production/production_manifest.json", "09_metadata/metadata.json"]:
                path = project_path / rel
                if path.is_file():
                    try: json.loads(path.read_text(encoding="utf-8"))
                    except (OSError, json.JSONDecodeError) as exc: errors.append(f"Invalid JSON {rel}: {exc}")
    if errors:
        print("VALIDATION: FAIL")
        for error in errors: print(f"- {error}")
        return 1
    print("VALIDATION: PASS")
    print("Note: structural validation does not verify facts, media quality, tool availability, or publication authorization.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
