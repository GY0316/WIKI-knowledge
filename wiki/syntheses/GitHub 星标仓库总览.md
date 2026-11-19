---
title: GitHub 星标仓库总览
type: synthesis
date: 2026-11-14
tags: [github-stars, 资源盘点, agent, agent-skills, 学习资源]
sources:
  - raw/01-articles/github-stars-2026-11-15.json
---

# GitHub 星标仓库总览（2026-11）

## 一句话结论

共 96 个公开星标仓库。按形态看，**工具（25）与教程（22）合计 47 个，占了近一半**，纯框架只有 8 个——这份星标更像“工具箱 + 工具书”，而不是一套造轮子的技术栈。按主题看，与 AI agent / AI 编程直接相关的 G1–G4 合计 28 个（29%），是单一方向里最集中的一块；其次是中文后端与面试资料（G6+G9 合计 23 个）。

## 数据与方法

- 数据源：GitHub 公开 API `GET /users/GY0316/starred`，抓取时间 2026-11-14，快照存于 `raw/01-articles/github-stars-2026-11-15.json`，字段与口径见 [[GitHub 星标快照 2026-11]]。
- 口径：仅包含**公开**星标仓库；GitHub 私有星标、以及用户在网页端自建的 star 列表（Lists）不在 API 返回里，因此本表不含“用户自己的分组标签”。
- 分类方式：先按**主题**分 14 组（组内按星数降序），再给每个仓库两个维度的标签——领域标签（如 `#agent`）与形态标签（框架/Skill/工具/库/模板/教程/清单/论文/资源站）。
- “定位”一列是根据仓库名、描述与 topics 写的一句话判断，不是仓库的官方介绍；描述缺失的仓库已单独标注。

## 按项目形态分布

| 形态 | 数量 | 代表仓库 |
| --- | --- | --- |
| 工具 | 25 | farion1231/cc-switch、Graphify-Labs/graphify、stablyai/orca |
| 教程 | 22 | codecrafters-io/build-your-own-x、donnemartin/system-design-primer、nilbuild/developer-roadmap |
| Skill | 12 | mattpocock/skills、multica-ai/andrej-karpathy-skills、anthropics/skills |
| 清单 | 11 | Shubhamsaboo/awesome-llm-apps、ripienaar/free-for-dev、punkpeye/awesome-mcp-servers |
| 框架 | 8 | earendil-works/pi、D4Vinci/Scrapling、FoundationAgents/OpenManus |
| 库 | 8 | juliangarnier/anime、DavidHDev/react-bits、greensock/GSAP |
| 模板 | 6 | fastapi/full-stack-fastapi-template、lin-xin/vue-manage-system、jekip/naive-ui-admin |
| 论文 | 3 | Robbyant/lingbot-map、Yangfan-Jiang/Federated-Learning-with-Differential-Privacy、synxlin/deep-gradient-compression |
| 资源站 | 1 | GitHubDaily/GitHubDaily |

## 分类清单

### G1 智能体框架与运行时（7）

> 从“能对话”走向“能自己干活”：多 agent 编排、个人助理、agent 原生 CLI 都在这一组。

| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |
| --- | --- | --- | --- | --- | --- |
| [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 125,155 | 工具 | 用自有订阅批量跑 Claude Code/Codex，桌面+移动+远程运行时 | `#agent` `#orchestration` |
| [earendil-works/pi](https://github.com/earendil-works/pi) | TypeScript | 122,051 | 框架 | 把统一 LLM API、agent loop、TUI 打包成一套工具包 | `#agent` `#cli` |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Python | 59,265 | 工具 | 多 agent + RAG 的终身个性化 AI 导师 | `#agent` `#education` |
| [FoundationAgents/OpenManus](https://github.com/FoundationAgents/OpenManus) | Python | 58,967 | 框架 | 开源通用 agent 框架，Manus 思路的公开实现 | `#agent` `#opensource` |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Python | 58,736 | 工具 | 让所有软件变成 agent 可直接调用的 CLI | `#agent` `#cli` |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | Python | 50,089 | 框架 | 轻量自托管个人助理，接 Telegram/Discord 等聊天入口 | `#agent` `#personal-assistant` |
| [deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype) | TypeScript | 23,163 | 框架 | 更自主的多 agent 系统原型，看它怎么定义 agent 的自治边界 | `#agent` `#multi-agent` |

### G2 Agent Skills 与提示工程（11）

> 本组几乎全是 skill 资产而非程序，共同点是“把某个领域的经验写成 agent 能执行的规范”。

| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |
| --- | --- | --- | --- | --- | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 324,564 | Skill | 一线工程师 .agents 目录里的实战 skills | `#agent-skills` `#engineering` |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | — | 233,188 | Skill | 单个 CLAUDE.md 修正 Claude Code 的常见坏习惯（源自 Karpathy 的观察） | `#agent-skills` `#prompt` |
| [anthropics/skills](https://github.com/anthropics/skills) | Python | 194,690 | Skill | Anthropic 官方 Agent Skills 公共仓库，学习 skill 写法的基准 | `#agent-skills` `#official` |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 190,998 | Skill | 让 agent 像最懒的资深工程师那样写“最少但够用”的代码（YAGNI） | `#agent-skills` `#prompt` |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 117,626 | Skill | 面向 AI 编程 agent 的生产级工程 skills | `#agent-skills` `#engineering` |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | JavaScript | 115,729 | Skill | 给编程 agent 审美：艺术指导 + 参考图 + 浏览器自检，专治“AI 味页面” | `#agent-skills` `#design` |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | JavaScript | 96,488 | Skill | 把想法、计划或代码库直接转成可交互架构图 | `#agent-skills` `#diagram` |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 67,196 | Skill | 45 种图表类型的编辑级图表设计 skill（HTML+SVG，不用 Mermaid） | `#agent-skills` `#diagram` |
| [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | HTML | 29,797 | Skill | 生成 HTML 幻灯片的 skill，杂志风/瑞士排版 + WebGL 放映 | `#agent-skills` `#ppt` |
| [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | — | 18,463 | Skill | GSAP 官方 skills，教 agent 正确使用动画库与插件 | `#agent-skills` `#animation` |
| [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | Python | 12,869 | Skill | 把书、长视频、播客蒸馏成可执行 Agent Skills | `#agent-skills` `#knowledge-distillation` |

### G3 AI 编程工具链与模型网关（6）

> 围绕 Claude Code / Codex 等引擎做客户端、配置切换与供应商聚合，是“多引擎并存”现状的产物。

| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |
| --- | --- | --- | --- | --- | --- |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Rust | 154,473 | 工具 | Claude Code / Codex / OpenCode 等多引擎配置与供应商一键切换 | `#ai-coding` `#provider-management` |
| [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | TypeScript | 87,523 | 工具 | 单端点聚合 375 家供应商的 MIT 网关，带回退与 token 压缩 | `#gateway` `#llm` |
| [warpdotdev/warp](https://github.com/warpdotdev/warp) | Rust | 66,012 | 工具 | 从终端长出来的 agentic 开发环境 | `#terminal` `#ai-coding` |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Python | 33,657 | 工具 | Claude Code 组件（agents/commands/skills/hooks/MCP）注册表与 CLI | `#ai-coding` `#registry` |
| [zhukunpenglinyutong/desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) | TypeScript | 4,598 | 工具 | 多引擎 AI 编程桌面客户端（Tauri） | `#ai-coding` `#desktop` |
| [ZyphrZero/kiro.rs](https://github.com/ZyphrZero/kiro.rs) | Rust | 569 | 工具 | Rust 实现的 Kiro 客户端 | `#ai-coding` `#client` |

### G4 代码智能与知识库（4）

> 用图谱或 wiki 结构替代“每次重新检索”，和本知识库是同一思路的不同实现。

| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |
| --- | --- | --- | --- | --- | --- |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Python | 147,870 | 工具 | 代码库+文档+SQL+PDF 建成可查询知识图谱，本地 AST 解析、无向量库 | `#knowledge-graph` `#code-intelligence` |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | TypeScript | 77,626 | 工具 | 随代码变更自动同步的预索引代码图谱，省 token、全程本地 | `#knowledge-graph` `#code-intelligence` |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | TypeScript | 48,546 | 工具 | 零服务端的代码智能引擎 | `#code-intelligence` `#tool` |
| [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | TypeScript | 21,664 | 工具 | LLM 增量维护持久 wiki 的桌面应用——本知识库的同类实现 | `#llm-wiki` `#knowledge-management` |

### G5 MCP、检索与数据采集（4）

> 给 agent 接外部世界的手：MCP 框架、搜索/抓取、以及 MCP 服务清单。

| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |
| --- | --- | --- | --- | --- | --- |
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | Python | 103,008 | 框架 | 从单请求到全站爬取的抓取框架，自带 MCP 与反爬处理 | `#scraping` `#tool` |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | — | 97,712 | 清单 | MCP server 大全，选型第一站 | `#mcp` `#awesome-list` |
| [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | Python | 28,466 | 框架 | Pythonic 的 MCP server/client 框架 | `#mcp` `#python` |
| [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | TypeScript | 5,544 | 工具 | 本地优先的 web 搜索/抓取/研究 MCP，无需 API Key | `#mcp` `#search` |

### G6 学习路线、课程与面试（12）

> 数量最多的一组，说明星标里有相当比例是“打算学”而不是“正在用”。

| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |
| --- | --- | --- | --- | --- | --- |
| [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Markdown | 562,567 | 教程 | 通过复刻技术来学编程的教程总集 | `#learning` `#awesome-list` |
| [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | Python | 377,882 | 教程 | 大规模系统设计学习与面试指南 | `#learning` `#system-design` |
| [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | TypeScript | 372,023 | 教程 | roadmap.sh 交互式开发者路线图 | `#learning` `#roadmap` |
| [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) | JavaScript | 186,516 | 教程 | 技术面试基础知识：操作系统、网络、系统设计、Leetcode | `#interview` `#cs-fundamentals` |
| [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | Python | 87,002 | 教程 | 《从零开始构建智能体》原理与实践教程 | `#learning` `#agent` |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Python | 78,957 | 教程 | 从零学 AI 工程：LLM、agent、CV、RL 一条线 | `#learning` `#ai-engineering` |
| [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) | Jupyter Notebook | 60,180 | 教程 | 《动手学大模型》系列编程实践 | `#learning` `#llm` |
| [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | Python | 58,064 | 教程 | 《深入理解 AI Agent》全书正文 + PDF + 分章代码 | `#learning` `#agent` `#book` |
| [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | Python | 23,167 | 教程 | Vibe Coding 中文资料（仓库无描述，按名称与主题归类，待核实） | `#vibe-coding` `#learning` |
| [SSHeRun/CS-Xmind-Note](https://github.com/SSHeRun/CS-Xmind-Note) | — | 10,855 | 教程 | 408 四门专业课思维导图与笔记 | `#learning` `#cs-fundamentals` |
| [xiaomabenten/system_architect](https://github.com/xiaomabenten/system_architect) | — | 4,677 | 教程 | 软考高级「系统架构设计师」备考资源 + 刷题软件 | `#exam` `#architecture` |
| [csguide-dabai/interview-guide](https://github.com/csguide-dabai/interview-guide) | — | 1,509 | 教程 | 后端校招八股文重点总结 | `#interview` `#backend` |

### G7 前端、UI 与动效可视化（8）

> 动效库与中后台模板占主导，可直接复用于交付物（PPT/网页/看板）。

| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |
| --- | --- | --- | --- | --- | --- |
| [juliangarnier/anime](https://github.com/juliangarnier/anime) | JavaScript | 74,691 | 库 | 轻量 JavaScript 动画引擎 | `#animation` `#frontend` |
| [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | JavaScript | 51,966 | 库 | 最大的动效/交互 React 组件库 | `#react` `#ui` `#animation` |
| [justjavac/wechat-miniapp-radar](https://github.com/justjavac/wechat-miniapp-radar) | TypeScript | 51,158 | 工具 | 小程序选型、趋势追踪与迁移诊断 | `#miniapp` `#tool` |
| [greensock/GSAP](https://github.com/greensock/GSAP) | JavaScript | 30,653 | 库 | 现代 Web 动画库的标杆 | `#animation` `#frontend` |
| [lin-xin/vue-manage-system](https://github.com/lin-xin/vue-manage-system) | Vue | 19,583 | 模板 | Vue3 + Element Plus 后台管理系统 | `#vue` `#admin` |
| [jekip/naive-ui-admin](https://github.com/jekip/naive-ui-admin) | Vue | 5,937 | 模板 | Vue3 + Naive UI 企业级中后台方案，含按钮级权限 | `#vue` `#admin` |
| [zclzone/vue-naive-admin](https://github.com/zclzone/vue-naive-admin) | Vue | 3,986 | 模板 | 轻量 Vue3 + Pinia + UnoCSS 后台模板 | `#vue` `#admin` |
| [TailAdmin/tailadmin-free-tailwind-dashboard-template](https://github.com/TailAdmin/tailadmin-free-tailwind-dashboard-template) | HTML | 2,392 | 模板 | Tailwind 后台仪表盘模板，组件齐全 | `#tailwind` `#template` |

### G8 全栈脚手架与后端模板（2）

> 开箱即用的工程骨架，价值在于目录分层与鉴权/测试的默认配置。

| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |
| --- | --- | --- | --- | --- | --- |
| [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) | TypeScript | 46,250 | 模板 | FastAPI + React + SQLModel + Docker 官方全栈模板 | `#fastapi` `#fullstack` |
| [JiayuXu0/FastAPI-Template](https://github.com/JiayuXu0/FastAPI-Template) | Python | 535 | 模板 | 分层清晰的企业级 FastAPI 后端模板 | `#fastapi` `#backend` |

### G9 Java / Spring 生态与实践（11）

> 中文 Java 学习生态的头部项目集中地：7 个教程、3 个工具库、1 个清单，教程大多已停止更新。

| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |
| --- | --- | --- | --- | --- | --- |
| [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide) | JavaScript | 159,561 | 教程 | Java 后端面试与知识体系大全 | `#java` `#interview` |
| [doocs/advanced-java](https://github.com/doocs/advanced-java) | Java | 79,176 | 教程 | Java 工程师进阶：高并发、分布式、微服务、海量数据 | `#java` `#architecture` |
| [xkcoding/spring-boot-demo](https://github.com/xkcoding/spring-boot-demo) | Java | 34,035 | 教程 | Spring Boot 实战 demo 大全 | `#spring` `#demo` |
| [wuyouzhuguli/SpringAll](https://github.com/wuyouzhuguli/SpringAll) | Java | 28,920 | 教程 | Spring Boot / Cloud / Security 循序渐进示例集 | `#spring` `#learning` |
| [yudaocode/SpringBoot-Labs](https://github.com/yudaocode/SpringBoot-Labs) | Java | 20,113 | 教程 | 六大专栏：Spring Boot/Cloud/Alibaba/Dubbo/MQ/分布式事务 | `#spring` `#distributed` |
| [itwanger/toBeBetterJavaer](https://github.com/itwanger/toBeBetterJavaer) | Java | 17,846 | 教程 | 通俗风格的 Java 学习指南：并发、JVM、企业开发 | `#java` `#learning` |
| [justauth/JustAuth](https://github.com/justauth/JustAuth) | Java | 17,541 | 库 | 小而全的第三方登录组件，覆盖几十家平台 | `#java` `#auth` |
| [baomidou/dynamic-datasource](https://github.com/baomidou/dynamic-datasource) | Java | 5,190 | 库 | Spring Boot 多数据源、读写分离、分布式事务 | `#spring` `#database` |
| [lets-mica/mica](https://github.com/lets-mica/mica) | Java | 2,230 | 库 | Spring Cloud 微服务核心工具集 | `#spring` `#toolkit` |
| [RudeCrab/rude-java](https://github.com/RudeCrab/rude-java) | Java | 1,413 | 教程 | SSM/Spring Security/MinIO/Vue 多框架项目实践 | `#java` `#demo` |
| [hello-go-maker/Java-project](https://github.com/hello-go-maker/Java-project) | — | 599 | 清单 | Java 实战项目推荐合集（电商/支付/后台/论坛） | `#java` `#awesome-list` |

### G10 视觉、3D、语音与图像（5）

> 多模态方向的少量但高价值项目，含 3D 重建与零样本 TTS。

| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |
| --- | --- | --- | --- | --- | --- |
| [lucidrains/vit-pytorch](https://github.com/lucidrains/vit-pytorch) | Python | 25,571 | 库 | Vision Transformer 的极简 PyTorch 实现 | `#cv` `#transformer` |
| [index-tts/index-tts](https://github.com/index-tts/index-tts) | Python | 25,096 | 库 | 工业级零样本可控 TTS，支持跨语种与音色克隆 | `#tts` `#audio` |
| [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | Python | 21,386 | Skill | 把参考图重建成可动画的 Three.js 程序（token 高效的图生 3D） | `#3d` `#threejs` `#agent-skills` |
| [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | Python | 18,635 | 论文 | 流式 3D 重建的几何上下文 Transformer（ECCV 2026 候选） | `#3d` `#academic` |
| [aoguai/LiYing](https://github.com/aoguai/LiYing) | Python | 4,056 | 工具 | 照相馆证件照后期全流程自动化（换底/裁剪/排版/压缩） | `#image` `#automation` |

### G11 学术论文、算法与安全（6）

> 论文复现与领域清单，适合当研究入口而非直接落地。

| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |
| --- | --- | --- | --- | --- | --- |
| [ctf-wiki/ctf-wiki](https://github.com/ctf-wiki/ctf-wiki) | Python | 9,763 | 教程 | CTF 知识 wiki：crypto/pwn/re/web/misc | `#security` `#wiki` |
| [youngfish42/Awesome-FL](https://github.com/youngfish42/Awesome-FL) | Python | 2,019 | 清单 | 联邦学习论文/框架/数据集全景清单，持续更新 | `#academic` `#federated-learning` |
| [the-web3/cryptography](https://github.com/the-web3/cryptography) | — | 691 | 教程 | 人人能懂的密码学教程 | `#cryptography` `#learning` |
| [hzysvilla/Academic_Smart_Contract_Papers](https://github.com/hzysvilla/Academic_Smart_Contract_Papers) | — | 647 | 清单 | 智能合约学术论文清单 | `#academic` `#blockchain` |
| [Yangfan-Jiang/Federated-Learning-with-Differential-Privacy](https://github.com/Yangfan-Jiang/Federated-Learning-with-Differential-Privacy) | Python | 323 | 论文 | 差分隐私联邦学习的 PyTorch 实现 | `#academic` `#privacy` |
| [synxlin/deep-gradient-compression](https://github.com/synxlin/deep-gradient-compression) | Python | 228 | 论文 | ICLR'18 深度梯度压缩：分布式训练省通信带宽 | `#academic` `#distributed-training` |

### G12 金融投研、量化与加密资产（4）

> 两类东西：系统化交易的资料库，和用 agent 做投研的框架。

| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |
| --- | --- | --- | --- | --- | --- |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | Python | 38,252 | 框架 | 个人交易 agent，带回测与多 agent 协作 | `#finance` `#agent` |
| [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | HTML | 17,136 | 框架 | 巴菲特/芒格/段永平/李录四大师方法论 + 多 agent 价值投资研究 | `#finance` `#agent` |
| [paperswithbacktest/awesome-systematic-trading](https://github.com/paperswithbacktest/awesome-systematic-trading) | Python | 15,363 | 清单 | 系统化交易库、策略、书与教程清单 | `#quant` `#awesome-list` |
| [Tangent-Wei/crypto_info](https://github.com/Tangent-Wei/crypto_info) | — | 2,890 | 清单 | 币圈工具与资料大全（交易所在内，偏引流性质） | `#crypto` `#awesome-list` |

### G13 资源清单、独立开发者与内容生态（8）

> “清单的清单”，用来发现新项目，本身不含技术实现。

| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |
| --- | --- | --- | --- | --- | --- |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Python | 144,653 | 清单 | 100+ AI agent / skill / RAG 应用合集 | `#awesome-list` `#agent` |
| [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | HTML | 142,864 | 清单 | 有免费额度的 SaaS/PaaS/IaaS 清单 | `#awesome-list` `#devops` |
| [1c7/chinese-independent-developer](https://github.com/1c7/chinese-independent-developer) | — | 62,111 | 清单 | 中国独立开发者项目列表 | `#indie` `#content` |
| [GitHubDaily/GitHubDaily](https://github.com/GitHubDaily/GitHubDaily) | — | 48,454 | 资源站 | 高质量开源项目日更推荐 | `#awesome-list` `#content` |
| [timqian/chinese-independent-blogs](https://github.com/timqian/chinese-independent-blogs) | JavaScript | 24,471 | 清单 | 中文独立博客列表 | `#indie` `#blog` |
| [easychen/opc-methodology](https://github.com/easychen/opc-methodology) | PHP | 17,072 | 教程 | 《一人企业方法论》第二版 | `#indie` `#book` |
| [dhamaniasad/awesome-postgres](https://github.com/dhamaniasad/awesome-postgres) | — | 12,186 | 清单 | PostgreSQL 生态资源清单 | `#database` `#awesome-list` |
| [vikiboss/60s](https://github.com/vikiboss/60s) | TypeScript | 5,925 | 工具 | 免费聚合 API：热搜、金价油价、天气、翻译、壁纸 | `#api` `#tool` |

### G14 桌面工具、Office 与系统增强（6）

> 提升单人效率的成品工具，其中 OfficeCLI 是少见的“给 agent 用的 Office”。

| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |
| --- | --- | --- | --- | --- | --- |
| [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | TypeScript | 98,369 | 工具 | 开源 CapCut 替代，浏览器内视频剪辑 | `#video` `#tool` |
| [CorentinTh/it-tools](https://github.com/CorentinTh/it-tools) | Vue | 41,268 | 工具 | 开发者在线小工具集合，UX 出色 | `#tool` `#developer-tools` |
| [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | C# | 33,297 | 工具 | 给 agent 用的 Office 套件 CLI：读写 Word/Excel/PPT，免装 Office | `#office` `#cli` `#agent` |
| [DevToys-app/DevToys](https://github.com/DevToys-app/DevToys) | C# | 32,276 | 工具 | 开发者瑞士军刀，跨平台桌面工具箱 | `#tool` `#desktop` |
| [Ebullioscopic/Atoll](https://github.com/Ebullioscopic/Atoll) | Swift | 5,267 | 工具 | macOS 上的灵动岛 | `#macos` `#desktop` |
| [ailyProject/aily-blockly](https://github.com/ailyProject/aily-blockly) | TypeScript | 3,874 | 工具 | 硬件开发 AI IDE：Arduino / ESP32 / STM32 / MicroPython | `#iot` `#ide` |

### G15 网络与自托管运维（2）

> 把服务跑在自己的机器上：DDNS、部署平台这类“装了就一直后台运行”的小工具。

| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |
| --- | --- | --- | --- | --- | --- |
| [jeessy2/ddns-go](https://github.com/jeessy2/ddns-go) | Go | 17,556 | 工具 | 单文件 DDNS 客户端：把动态公网 IP 自动更新到阿里云/腾讯云/Cloudflare 等解析 | `#ddns` `#network` `#self-hosted` |
| [oblien/openship](https://github.com/oblien/openship) | TypeScript | 15,321 | 工具 | 自托管部署平台 | `#devops` `#self-hosted` |

## 横向观察

- **语言分布**：Python 28，TypeScript 16，未标注 13，JavaScript 10，Java 9，HTML 5。空语言多为纯 Markdown/提示词类仓库，代码不是主体。
- **星数梯队**：10 万+ 18 个，5 万–10 万 20 个，1 万–5 万 34 个，1 万以下 24 个。星数在这里只反映流行度，不代表可维护性。
- **活跃度（最后推送年份）**：2026 年 83 个，2025 年 3 个，2024 年 6 个，2023 年 2 个，2022 年 1 个，2021 年 1 个。可据此判断哪些项目已停止更新、哪些仍在快速迭代。
- **同一主题的重复度偏高**：Java 教程（JavaGuide / advanced-java / toBeBetterJavaer / CS-Notes）与 Spring 示例（SpringAll / spring-boot-demo / SpringBoot-Labs / rude-java）内容高度重叠；前端中后台模板有 4 个同质项目。后续若要深入，每组只需保留 1–2 个继续读。
- **skill 类项目几乎都不靠代码取胜**：这一批（`#agent-skills`）主体是 Markdown 写的规范 + 少量脚本，说明 agent 能力的瓶颈正在从“能不能实现”转向“领域知识和验收标准写得够不够清楚”。

## 与本知识库的关系

星标里有一批项目和本库（Karpathy LLM Wiki 模式）在做同一件事——**把资料沉淀成可复用的结构化知识，而不是每次重新检索**：

- [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki)：同一模式的桌面实现，可直接对照它的页面组织与增量策略。
- [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) 与 [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)：用图谱替代向量库的路线——本库 AGENTS.md 明确“不做向量检索”，这两者提供了另一种“确定性 + 可解释边”的参照。
- [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill)：把书/长视频/播客蒸馏成 skill，与 ingest 的产出目标（可复用的知识页）相近，可借鉴它的蒸馏模板。
- [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)、[anthropics/skills](https://github.com/anthropics/skills)：本仓库 `CLAUDE.md/AGENTS.md` 的写法可直接对标这两处。
- [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)、[datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents)：后续 ingest agent 主题时的首选读物（成体系、有代码）。

## 尚存的缺口 / 待研究

- [ ] 星标里 `#agent-skills` 的 12 个 skill，实际质量差异很大（星数≠可用），需要挑 3 个真跑一遍再评。
- [ ] `2025Emma/vibe-coding-cn` 无仓库描述，定位待核实。
- [ ] GitHub 网页端自建的 star 列表（Lists）未纳入，若用户有分组习惯，可导出后合并进本表。
- [ ] 私有星标不可见，本表可能少于真实星标总数。
- [ ] 下一步候选：按组各 ingest 1 个代表仓库（先 G4 知识库组与 G2 skill 组），生成实体页与概念页。
