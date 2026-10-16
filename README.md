# BookVideo Agent Workflow

面向 YouTube 读书视频的可执行 Agent 工作流包。覆盖跨学科选书、来源核验、选题、研究、脚本、独立审稿、MoneyPrinterTurbo 制作、成片验收、封面与元数据、上传发布及数据复盘。

## 快速开始

1. 下载仓库 ZIP 或克隆仓库。
2. **先读 `START_HERE.md` 和 `AGENTS.md`**，再读 `docs/SOP.md`、`docs/QUALITY_GATES.md` 与 `docs/INTEGRATIONS.md`。
3. 按 `config/project.yaml` 配置频道定位、时长、制作工具和发布授权策略。
4. 在 `data/` 中维护三张 CSV 台账；不要清空历史记录。
5. 在仓库根目录运行结构校验：
   ```bash
   python scripts/validate_project.py --ledgers-only
   ```
6. 创建新视频项目：
   ```bash
   python scripts/new_project.py --id BV-20261016-001 --title "工作标题"
   python scripts/validate_project.py --project BV-20261016-001
   ```
7. 将 Agent 指向 `START_HERE.md`，要求其遵循 `AGENTS.md` 和每阶段对应的 `skills/*/SKILL.md`。

## 核心原则

- 先核验书籍与事实，再写稿；来源不足时标记待核验，不得编造。
- 书籍质量、视频潜力、当前制作优先级是三个不同判断。
- 所有关键阶段都要产出可追踪文件与结构化状态。
- 自动化失败最多重试两次；仍失败则停止并输出可诊断报告。
- 上传默认私密；公开发布必须有针对具体视频的真实人工授权记录。
- 不大段复制书籍原文；采用评论、分析、概述和必要的短引文，并核对适用的版权规则。
- 不把凭据写入仓库、日志或项目报告。

## 目录

- `START_HERE.md`：Agent 启动协议
- `AGENTS.md`：全局调度规则、状态机和不可违反的约束
- `docs/SOP.md`：端到端标准作业程序
- `docs/QUALITY_GATES.md`：书籍/选题/脚本/成片评分和硬性门禁
- `docs/INTEGRATIONS.md`：MoneyPrinterTurbo 与 YouTube 集成合同
- `skills/`：分阶段技能说明、输入输出合同和审查规则
- `config/project.yaml`：默认项目配置
- `data/`：书籍总库、视频项目台账、评选历史
- `templates/project/`：单期视频项目完整模板
- `scripts/new_project.py`：创建新视频项目骨架
- `scripts/validate_project.py`：校验台账与项目结构

## 集成边界

本仓库提供 Agent 工作流、提示词、状态规范和本地校验脚本。MoneyPrinterTurbo 的 CLI/API、模型服务、YouTube OAuth 凭据和频道权限因环境而异。启用真实制作或上传前，必须核验本机工具版本与实际接口并完成集成测试。默认不公开发布；没有真实授权记录时，Agent 必须停留在私密验收阶段。
