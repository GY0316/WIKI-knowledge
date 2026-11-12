---
name: lint
description: 知识库体检。先跑 scripts/lint.py 做机械检查并自动修复死链和索引缺失，再做语义检查（矛盾、过时、概念缺页）交用户定夺。用户说「lint」或定期维护时使用。
---

# lint

## 步骤

1. 运行 `python3 scripts/lint.py`，得到死链、孤儿页、索引缺失、frontmatter 问题、sources 路径失效、待 ingest 列表。
2. 能自动修的直接修：
   - 索引缺失：补进 `wiki/index.md`（一句话摘要取自页面）。
   - 死链：目标明显是改名或拼写错误时改链接；否则列给用户。
3. 语义检查（脚本做不到，由你读页面判断）：
   - 认知冲突：页面间互相矛盾的说法。
   - 过时说法：被较新来源推翻的旧结论。
   - 概念缺页：多个页面提到、但无独立页面的概念。把它们登记到 `wiki/gaps.md`。
4. 运行 `scripts/sync_rules.sh --check`，确认 `CLAUDE.md` 与 `AGENTS.md` 一致。
5. 追加 `wiki/log.md`：`## [YYYY-MM-DD] lint | 摘要`。
6. 报告：已修复的、需用户判断的（附页面与原文片段）、孤儿页与待 ingest 资料。

只修机械问题。矛盾和过时的取舍交给用户，不擅自改写结论。
