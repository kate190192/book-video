# BookVideo Agent Workflow

面向 YouTube 读书视频的可执行 Agent 工作流包。覆盖跨学科选书、来源核验、选题、研究、脚本、独立审稿、MoneyPrinterTurbo 制作、成片验收、封面与元数据、上传发布及数据复盘。

## 快速开始

1. 下载或克隆本仓库。
2. 先阅读 `AGENTS.md`，再阅读 `docs/SOP.md`。
3. 按 `config/project.yaml` 配置频道定位、时长、语言、制作工具路径和发布授权规则。
4. 在 `data/` 中维护书籍总库、视频项目台账与评选历史。
5. 对新任务执行：`python scripts/validate_project.py --help`，按脚本说明校验台账与项目文件。
6. 每个视频项目从 `templates/project/` 复制模板到 `projects/<project_id>/`，不得直接覆盖模板。
7. 先完成一个项目的端到端试运行，再开启批量自动化。

## 核心原则

- 先核验书籍与事实，再写稿；来源不充分时标记待核验，不得编造。
- 书籍质量、视频潜力、当前制作优先级是三个不同判断。
- 所有关键阶段都要产出可追踪文件与结构化状态。
- 自动化失败最多重试两次；仍失败则停止并输出可诊断报告。
- 上传默认私密；公开发布必须有明确的人类授权记录。
- 不把书籍原文大段复制进脚本；采用评论、分析、概述和必要的短引文，并核对适用的版权规则。
- 本仓库不包含 YouTube 凭据，不会自动绕过平台授权或工具限制。

## 目录

- `AGENTS.md`：所有 Agent 的总规则与调度入口
- `docs/SOP.md`：端到端标准作业程序
- `docs/QUALITY_GATES.md`：硬性门禁和评分规则
- `docs/INTEGRATIONS.md`：MoneyPrinterTurbo、YouTube 上传适配约定
- `skills/`：分阶段技能合同与提示词
- `config/project.yaml`：项目默认配置
- `data/`：三张 CSV 台账
- `templates/`：项目文件模板
- `scripts/validate_project.py`：台账与项目结构校验
- `scripts/new_project.py`：创建新视频项目骨架

## 当前边界

该包提供 Agent 可执行的流程、提示词、状态规范和本地校验工具。MoneyPrinterTurbo 的具体 CLI/API、模型服务、YouTube OAuth 凭据和频道权限因环境而异，必须在本地配置并通过集成测试后才能启用真实制作或上传。