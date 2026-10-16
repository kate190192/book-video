# Start Here: Agent Launch Protocol

This file is the shortest operational entry point for an Agent that has just downloaded the repository.

## Before doing any work

1. Read `AGENTS.md`.
2. Read `docs/SOP.md`, `docs/QUALITY_GATES.md`, and `docs/INTEGRATIONS.md`.
3. Read the relevant skill file before executing each stage.
4. Inspect `config/project.yaml` and the three CSV files under `data/`.
5. Check which tools and integrations are actually available. Do not assume web research, image generation, MoneyPrinterTurbo, media inspection, or YouTube upload is available unless it can be verified in the current runtime.

## Default task

If the user says “开始选书” or asks to build a new episode:
1. Run book discovery and create at least 20 raw candidates as a research target, not a quota for accepted books.
2. Verify bibliographic identity and evidence; score and deduplicate candidates against the existing ledger.
3. Present a ranked shortlist with sources, score rationale, uncertainties and rejected-candidate reasons.
4. Do not start production until a specific book and angle pass the book and topic gates.

If the user names a book:
1. Verify the book identity and relevant edition.
2. Check for duplicates in `data/books.csv` and `data/video_projects.csv`.
3. If a new project is approved, create its workspace:
   `python scripts/new_project.py --id BV-YYYYMMDD-001 --title "工作标题"`
4. Run stages in order, update `project_state.json`, and validate artifacts before each transition.

## Stage discipline

- One stage at a time; no skipping gates.
- Save findings to the specified artifact files, not only to chat.
- Use actual source URLs and distinguish verified facts from hypotheses.
- If an integration is unavailable, finish independent work and mark the dependent stage `BLOCKED_INTEGRATION`.
- Do not upload publicly without a real approval record for the specific video.
- Never claim tests passed unless they were actually executed.

## End-of-task report

Report:
- completed stages and artifact paths;
- gate scores and hard-stop checks;
- tests actually run and results;
- blockers or decisions needed from the user;
- exact next action.
