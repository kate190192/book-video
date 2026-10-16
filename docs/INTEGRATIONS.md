# Integration Contracts

This document intentionally separates workflow logic from environment-specific tools.

## MoneyPrinterTurbo

Before enabling production, the Agent must inspect the locally installed MoneyPrinterTurbo version and its official README/configuration, then record:
- repository/version or commit;
- supported invocation method (CLI, Python API, web service, or UI automation);
- exact input schema and required fields;
- exact output directory and output file naming;
- required model/API keys and where they are stored;
- supported subtitle, TTS, image/video, resolution, aspect-ratio and language options;
- known limitations and error codes.

Do not infer flags or endpoints from examples for a different version. Keep secrets in environment variables or a local secret manager, never in this repository.

### Neutral handoff format

The workflow produces:
- `script.md`: final narration script;
- `scene_plan.json`: scene-level narration and visual intent;
- `production_request.json`: normalized request generated from config;
- `production_manifest.json`: actual tool version, command/method, input hash, outputs, logs and status.

Example `scene_plan.json` structure:
```json
{
  "project_id": "BV-YYYYMMDD-001",
  "language": "zh-CN",
  "scenes": [
    {
      "scene_id": "S01",
      "narration": "这一段旁白。",
      "visual_intent": "表现本段概念的示意画面",
      "on_screen_text": [],
      "source_ids": ["SRC-001"],
      "estimated_seconds": 12
    }
  ]
}
```

Each scene must preserve narration order. On-screen text, formulas and diagrams must be legible and appear in the order required by the explanation. Avoid unrelated stock footage used merely to fill time.

## YouTube upload

Use the official YouTube Data API or an explicitly authorized upload tool. Before upload verify:
- target channel identity;
- authenticated account has permission;
- video file exists and is playable;
- title, description, thumbnail, privacy status and made-for-kids setting are explicitly set;
- all required disclosures and licensing checks are complete.

Initial visibility must be `private`. Save remote video ID immediately after a successful response. If the response times out, query the channel for the upload before retrying.

Publishing authorization must be a structured record such as:
```json
{
  "approved": true,
  "approved_by": "human operator identifier",
  "approved_at": "ISO-8601 timestamp",
  "approved_visibility": "public",
  "video_id": "remote-video-id"
}
```
This is a schema example only; never fabricate an approval record. Public release must be blocked unless an actual authorized operator supplied approval.

## Environment variables

Use a local `.env` file that is excluded from version control, or a secret manager. Suggested names are placeholders and do not imply automatic support:
- `YOUTUBE_CLIENT_ID`
- `YOUTUBE_CLIENT_SECRET`
- `YOUTUBE_REFRESH_TOKEN`
- tool-specific model API keys

Never print secret values to logs. 