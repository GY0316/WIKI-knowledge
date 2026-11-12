# WIKI-knowledge

基于 [Karpathy LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 的个人**知识库**。配合 Obsidian 浏览、Claude Code / Codex 维护。

这是「知识库」单库，只放可公开/分享的学习内容。个人日程、日记等私密内容请放在另一个独立的私密仓库。

## 结构

```
raw/        原始资料（AI 只读；ingest 后移到 09-archive/）
  01-articles/  02-papers/  03-transcripts/  04-meeting_notes/  09-archive/  assets/
wiki/       AI 维护的知识层
  concepts/  entities/  sources/  syntheses/
  index.md  全库目录    log.md  操作日志
templates/  页面模板（source / concept / entity / synthesis）
CLAUDE.md   Claude Code 规则    AGENTS.md  Codex/OpenCode 规则（内容相同）
```

## 用法

在仓库目录打开 Claude Code 或 Codex，用自然语言或简写操作：

- `ingest 这份资料`（或给出 raw/ 里的文件）— 把资料编译进 wiki
- `query：我对注意力机制了解什么？` — 从 wiki 检索并带引用回答
- `lint` — 检查死链、孤儿页、索引缺失、认知冲突

规则细节见 `CLAUDE.md`。

### Skills 与脚本

`.claude/skills/` 下有 `ingest`、`query`、`lint`、`evolve` 四个 skill，对应上面的操作加一个学习回顾：

- `evolve` — 盘点覆盖度与薄弱点，更新 `wiki/gaps.md`（学习缺口清单），建议下一步读什么

学习闭环：query / lint / evolve 发现缺口 → 登记到 `gaps.md` → 你找到资料放进 `raw/` → ingest 回答缺口并移到「已解决」。

脚本：

```bash
python3 scripts/lint.py          # 死链、孤儿页、索引缺失、frontmatter、待 ingest 资料
scripts/sync_rules.sh            # CLAUDE.md -> AGENTS.md
scripts/sync_rules.sh --check    # 仅检查两份规则是否一致
```

### 可选：安装成熟的 skill

```bash
npx add-skill Astro-Han/karpathy-llm-wiki
```

## Obsidian 设置建议

1. 用 Obsidian「打开文件夹作为仓库」选中本目录。
2. 图谱视图里过滤掉索引和日志，避免它们成为「引力中心」：
   在图谱的 filter 搜索框填 `-path:index -path:log`。
3. 附件路径（设置 → 文件与链接 → 附件默认位置）指到 `raw/assets/`。

## 示例

仓库里带了一组 `示例-` 前缀的文件（Transformer / 注意力机制 / Google Brain），演示完整的 ingest 链路。熟悉后可直接删除它们。

## 备份

仓库已连到 GitHub。建议在 Obsidian 安装社区插件 **Obsidian Git**，设置定时自动提交推送。不要在本库存放密码、API key 等敏感信息（GitHub 私有库非端到端加密）。
