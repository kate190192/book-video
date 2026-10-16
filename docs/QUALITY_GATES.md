# Quality Gates and Scoring

## Hard-stop rules

以下任一项成立即失败，不可被总分抵消：
- 书籍身份、作者或出版信息存在重大疑点且未标注；
- 核心事实无可靠来源或存在已知错误；
- 伪造引用、页码、研究、奖项、销量或专家观点；
- 核心论证不成立，或把争议观点冒充共识；
- 严重版权/隐私风险未解决；
- 成片缺失关键段落、音轨损坏、字幕严重错位或输出文件不可播放；
- 未授权即公开发布；
- 发布动作结果不确定却重复上传。

## Book score (100)

| Dimension | Points | Review question |
|---|---:|---|
| Knowledge/idea contribution | 25 | 是否提供有解释力的概念、机制、框架或证据？ |
| Evidence and argument quality | 20 | 论证是否可靠，证据是否与结论相称？ |
| Originality/distinctiveness | 15 | 是否带来独特视角或有效综合？ |
| Long-term/relevance value | 15 | 是否有长期价值或现实解释力？ |
| Video interpretation potential | 15 | 能否形成明确问题、叙事张力和清晰解释？ |
| Source availability | 5 | 能否获得足够可靠的核验资料？ |
| Audience fit | 5 | 是否符合频道定位与受众理解水平？ |

Bands: 90–100 priority candidate; 80–89 recommended; 70–79 watchlist; below 70 do not prioritize. Score is a structured editorial judgment, not a universal measure of academic merit. Apply discipline-appropriate evidence standards.

## Topic score (100)

Importance 20; audience relevance 15; clarity of mechanism/claim 20; evidence support 20; narrative tension 15; channel differentiation 10.
- 75+: research
- 65–74: revise and rescore
- below 65: reject or archive

## Script score (100)

Argument and accuracy 25; structure 20; evidence and source traceability 20; audience comprehension 15; voice and originality 10; pacing and production readiness 10.
- 85+ with no hard-stop issue: pass
- 75–84: revise
- below 75: major rewrite
- Any hard-stop issue: fail regardless of score

## Video QA score (100)

| Dimension | Points |
|---|---:|
| Audio clarity, levels, no clipping | 20 |
| Visual relevance and legibility | 20 |
| Subtitle accuracy and timing | 15 |
| Narrative continuity and pacing | 15 |
| Technical integrity and export | 15 |
| Factual/copyright review | 15 |

Pass: 90+ and no hard-stop issue. 80–89 requires targeted fixes and recheck. Below 80 requires rework. Factual/copyright issues are hard stops regardless of score.

## Required evidence per gate

Each report must include:
- gate name and project ID;
- artifact paths and versions reviewed;
- score by dimension and rationale;
- hard-stop checklist;
- result: PASS / REVISE / BLOCKED / FAIL;
- reviewer role and timestamp;
- unresolved issues and next action.

## Retry policy

Maximum two retries per automated stage after the initial attempt. A retry must be based on a specific diagnosis. If still failing, stop, preserve logs, set state to BLOCKED and report the missing dependency or decision. Never retry publishing blindly. 