# Skill: Upload, Publish and Learn

## Preflight
Confirm final video passed QA; metadata and thumbnail files exist; channel/account identity is correct; privacy setting is explicitly private; credentials are available via secure local configuration; upload mechanism is documented and authorized.

## Upload state machine
`READY_TO_UPLOAD → UPLOADING → UPLOADED_PRIVATE → PROCESSING → PRIVATE_VERIFIED → WAITING_FOR_APPROVAL → PUBLISHED`

On upload success, immediately persist the remote video ID and response metadata. If timeout/connection loss occurs, query the channel/account for the possible upload before any retry. Never duplicate an uncertain upload.

## Private verification
Check platform processing status, video playback, title, description, thumbnail, subtitles, audience setting and visibility. Save verification evidence in `09_publish/private_verification.md`.

## Approval
Public release requires a real human approval record containing approver, timestamp, video ID and approved visibility. An example schema in `docs/INTEGRATIONS.md` is not an approval. If approval is absent, remain private and report the pending decision. Do not infer consent from silence or a generic “continue” if it does not clearly authorize public release of the identified video.

## After publication
Save URL, publication time and settings. At the configured observation intervals, collect only metrics actually available to the authenticated account. Produce `10_analytics/analytics_review.md` covering click-through rate, retention, average view duration, traffic sources, audience response and lessons, with limitations noted.

## Outputs
Upload manifest, private verification, approval record reference, publication record and analytics review. Do not commit credentials, tokens or private audience data. 