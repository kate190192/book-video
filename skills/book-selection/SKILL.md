# Skill: Book Selection, Verification and Deduplication

## Hard gates
入选前必须确认：作品身份可识别；作者与出版/版本信息有可靠依据；存在实质内容；关键主张可通过书籍资料或独立来源核验；没有无法解决的重大风险；符合频道定位。硬门禁不通过时，无论评分多少都不得进入优先队列。

## Score (100)
- 思想/知识贡献：25
- 证据与论证质量：20
- 原创性与独特性：15
- 长期价值与现实意义：15
- 视频解读潜力：15
- 资料可获得性：5
- 受众适配度：5

90–100 优先候选；80–89 推荐；70–79 观察；低于 70 不进入优先队列。每项必须给出理由与来源，评分不得仅由模型印象产生。

## Deduplication
1. ISBN 精确匹配（若有）。
2. 原版书名 + 作者匹配。
3. 中文译名、不同译本、再版和修订版归入同一 `edition_group`，保留版本信息。
4. 对近似书名、同一作者的相关作品、合集/节选进行人工判断。
5. 检查历史视频标题、中心问题和角度。一本书可多次使用，但必须提出实质不同的解释问题并通过选题审查。
6. 发现重复时填 `duplicate_of`，不删除历史记录。

## Status values
`DISCOVERED`, `NEEDS_VERIFICATION`, `QUALIFIED`, `SHORTLISTED`, `QUEUED`, `IN_PRODUCTION`, `PUBLISHED`, `REJECTED`, `ARCHIVED`.

## Required output
`02_book_review/book_review.md` includes identity evidence, score per dimension, total, hard-gate results, duplication result, strengths, limitations, proposed video questions, decision and sources. Update `books.csv` and append a row to `book_decisions.csv`.

## Do not
Do not treat popularity as proof of quality. Do not invent citation details. If source coverage is incomplete, use `NEEDS_VERIFICATION`; if the library/ledger is unavailable, disclose that deduplication is partial. 