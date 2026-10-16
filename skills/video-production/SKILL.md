# Skill: MoneyPrinterTurbo Production

## Preflight
- Confirm editorial approval.
- Validate script and scene plan.
- Confirm local MoneyPrinterTurbo version and supported interface from installed docs/source.
- Confirm required model services, configuration and credentials are available without exposing secrets.
- Confirm output directory, disk space, voice/language, aspect ratio and subtitle settings.
- Save exact tool/version/interface information to production manifest.

## Execution
1. Convert neutral script/scene plan to the exact input schema supported by the installed version.
2. Run a small smoke test if this environment has not been validated.
3. Execute full render using only verified commands/API/UI actions.
4. Capture stdout/stderr or UI evidence, exit status, runtime and output paths.
5. Verify that output files exist and are non-empty; do not treat that as full QA.
6. On failure, diagnose root cause, make a targeted change and retry. Maximum two retries after initial attempt.
7. If still failing, set `BLOCKED`, preserve logs and provide a concrete remediation report.

## Scene logic
Visuals must follow narration order. Text, diagrams and formulas appear when introduced and remain long enough to read. Do not insert arbitrary unrelated footage. If an image/video asset cannot be licensed or sourced safely, replace it or block the render.

## Outputs
`07_production/production_manifest.json`, final video, logs and any conversion artifacts. Never invent a CLI flag or API endpoint. 