# Skill: Video Quality Assurance

Review the rendered video independently of the production Agent.

## Automated checks where supported
- file exists, size > 0, duration within configured bounds;
- expected video and audio streams exist;
- resolution/aspect ratio and frame rate;
- audio peak/clipping and silence detection;
- subtitle file parses and timestamps are monotonic;
- no missing required deliverables.

Use available local tools only after confirming they are installed. If ffprobe/ffmpeg is absent, report that automated media checks were not run; do not claim success.

## Semantic and playback checks
Sample the beginning, each major section, transitions, and end; use full playback or visual/audio review when feasible. Check narration clarity, subtitle timing and spelling, visual relevance, text legibility, scene order, continuity, pacing, black frames, frozen frames, missing scenes, music balance and abrupt ending. Cross-check all factual captions and displayed numbers against the evidence ledger.

## Copyright and safety
Check visual/music asset provenance and license status. Do not assume online availability means reuse permission. Confirm required disclosure and attribution.

## Output
`08_video_qa/qa_report.md` with timecodes, severity, evidence, fixes and retest results. Score >=90 and no hard-stop issue to pass. Failed videos return to production. 