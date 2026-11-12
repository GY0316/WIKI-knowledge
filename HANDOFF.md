# 交接文档:个人知识库 + 生活库搭建

日期:2026-11-12。用于从对话模式切换到 code 模式后继续修改内容。

## 1. 目标

为用户 mi 搭建一套 AI 协作的个人笔记系统,用于:

- 学习技术架构、社会知识等内容,并沉淀与 AI 的讨论结论。
- 记录日常、日程、计划,并做周复盘。

用户主要在电脑上使用,只有自己一人,使用 Claude Code 和 Codex 作为 AI。

## 2. 已定决策与理由

| 决策 | 理由 |
|---|---|
| 工具选 Obsidian,不选飞书/Notion | 笔记是本地 Markdown 文件,AI agent 直接读写,无需 API 和联网 |
| 备份用 Git + GitHub 私有仓库,暂不买 Obsidian Sync | 可按批次审查和回退 AI 的改动;用户主要在电脑上使用 |
| 采用 Karpathy LLM Wiki 三层结构(raw / wiki / schema) | 有成熟社区实践,适合学习型知识沉淀 |
| 分成两个独立仓库 | 用户确认两类内容隐私差别很大,且接受切换成本 |
| 不使用 nashsu/llm_wiki 作主力 | 自带聊天 agent 与 Claude/Codex 功能重叠,按 token 另外计费,不含日程与日记 |
| 两库之间只走「搬运草稿」流程 | 保证生活库内容不会被动进入知识库,搬什么由用户逐条确认 |

参考仓库:Astro-Han/karpathy-llm-wiki(skills 和设计边界)、jason-effi-lab/karpathy-llm-wiki-vault(中文目录结构)、SamurAIGPT/llm-wiki-agent(软链接方案、图谱过滤)、nvk/llm-wiki(Ideas 到 Projects 的流转思路)。其中 nvk 的 README 只读了开头的总览,后面的命令细节没有读完。

## 3. 当前状态

### WIKI-knowledge(知识库)

- 本地路径:`~/Projects/WIKI-knowledge`
- 远程:`GY0316/WIKI-knowledge`。**远程地址曾是 HTTPS**,需要改成 `git@github.com:GY0316/WIKI-knowledge.git`。用户可能已改,先用 `git remote -v` 确认。
- 文件已全部写入。是否已提交、推送,未经确认。用 `git log` 和 `git status` 核实。
- 内容:
  - `CLAUDE.md` 和 `AGENTS.md`:内容相同的中文规则,含 ingest / query / lint 工作流、读写权限、「刻意不做的事」。
  - `raw/`:`01-articles`、`02-papers`、`03-transcripts`、`04-meeting_notes`、`09-archive`、`assets`。
  - `wiki/`:`concepts`、`entities`、`sources`、`syntheses`,加 `index.md` 和 `log.md`。
  - `templates/`:source、concept、entity、synthesis 四个模板。
  - 示例链路(文件名带「示例-」前缀或为其衍生页):`raw/02-papers/示例-attention-is-all-you-need.md`、`wiki/sources/示例-Attention Is All You Need.md`、`wiki/concepts/注意力机制.md`、`wiki/entities/Google Brain.md`。
  - `README.md`、`.gitignore`。

### WIKI-life(生活库)

- 本地路径:`~/Projects/WIKI-life`
- 远程:`git@github.com:GY0316/WIKI-life.git`(已是 SSH)。仓库为空,没有任何提交。
- 文件已全部写入,**未提交、未推送**。
- 内容:
  - `CLAUDE.md` 和 `AGENTS.md`:内容相同,含隐私红线、整理 Inbox、日记、周复盘、搬运草稿、项目归档流程。
  - 目录:`00-Inbox`、`10-日记/2026`、`20-计划/周计划`、`20-计划/月度与年度`、`30-项目`、`90-归档`。
  - `templates/`:日记、周复盘、项目、月度目标。
  - `10-日记/2026/示例-2026-11-12.md`(虚构示例)、`README.md`、`.gitignore`(额外排除 `.env`、`*.key`、`*.pem`)。

## 4. 待办

1. 确认 `WIKI-life` 在 GitHub 上的可见性为 **Private**(仓库 Settings 最下方 Danger Zone)。
2. 核实并完成两个仓库的提交与推送。`WIKI-life` 首次推送用 `git push -u origin main`。
3. 在 Obsidian 中分别用「打开文件夹作为仓库」打开两个目录。
   - 知识库:图谱 filter 填 `-path:index -path:log`,附件路径设为 `raw/assets/`。
   - 生活库:Daily notes 和 Templates 插件的模板目录设为 `templates/`。
4. 可选:安装 Obsidian Git 插件做定时提交。
5. 可选:`npx add-skill Astro-Han/karpathy-llm-wiki`,装成熟的 ingest / query / lint skill。
6. 用户熟悉流程后,删除所有「示例-」文件及其衍生页,并同步清理 `index.md` 和 `log.md` 中的示例条目。
7. 已向用户提议、尚未创建:每周日晚上自动 lint 并提示可 ingest 内容的定时任务。用户没有回应,不要擅自创建。

## 5. 环境与踩坑记录

- **Git 认证**:用户的 GitHub 使用专用密钥 `~/.ssh/id_ed25519_github`,已在 `~/.ssh/config` 为 `github.com` 配置 `IdentityFile` 和 `IdentitiesOnly yes`。`ssh -T git@github.com` 已验证通过。用户另有一把默认密钥给 GitLab 用,不能覆盖。
- **HTTPS 地址不会使用 SSH 密钥**,GitHub 也不接受密码。所有远程必须是 `git@github.com:` 形式。用户已两次在这里失败。
- **对话模式的沙箱对 `.git` 没有写权限**,残留了 `index.lock` 和若干 `tmp_obj_*` 文件,无法删除。所有 git 提交和推送都要在用户本机终端或 code 模式执行。如发现 `.git/index.lock`,确认没有 git 进程在运行后删除。
- 沙箱里的 `mnt` 路径是 `/sessions/.../mnt/WIKI-knowledge` 和 `.../WIKI-life`,仅在 bash 里有效;文件工具使用 `/Users/mi/Projects/...`。

## 6. 约定与注意事项

- 所有页面用简体中文,日期用 `YYYY-MM-DD`。
- **`CLAUDE.md` 和 `AGENTS.md` 是手工复制的两份**,修改其中一个必须同步另一个,两个仓库各一对。可考虑加一个同步脚本或改用符号链接,但要权衡符号链接在 Windows 和部分 git 工具上的兼容性。
- 文件名即双链名。部分文件名含空格,例如 `Google Brain.md`、`示例-Attention Is All You Need.md`,处理路径时要加引号。
- Obsidian 双链不跨 vault,两个库之间禁止互建 `[[双链]]`。
- 规则文件里写的 `[[页面名]]` 是代码块内的格式说明,不是真链接,lint 时应忽略。
- 知识库只放可公开或可分享的内容。生活库内容不得直接写入知识库,只能经「搬运草稿」由用户逐条确认。
- 不要在任何库里存放密码、API key、证件号等凭据。
- 本交接文档位于知识库根目录,含有生活库的结构概述但没有私密内容。若不想提交它,加入 `.gitignore` 或移走。

## 7. 在 code 模式中可以改进的方向

以下是建议,没有经过用户确认,动手前先问用户。

- 把 ingest / query / lint 做成 `.claude/skills/` 下的正式 skill(参考 jason-effi-lab 的写法),并加 `/ingest`、`/query`、`/lint` 命令。
- 写一个 lint 脚本:检查死链、孤儿页、`index.md` 缺失条目,忽略代码块里的双链。
- 写一个脚本同步 `CLAUDE.md` 到 `AGENTS.md`。
- 生活库加一个按日期查找逾期任务的小脚本(任务格式为 `- [ ] 事项 📅 YYYY-MM-DD`,可直接用 grep)。
