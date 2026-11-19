#!/usr/bin/env python3
"""把 GitHub 星标快照（raw/01-articles/github-stars-*.json）生成 wiki 分类总览页。

用法：
    python scripts/github_stars_to_wiki.py [快照json路径]

脚本只负责“数据搬运 + 分类排序 + 统计”，分类判断（组别/标签/一句话定位）写在下方 MAPPING 里，
人工维护。新增星标仓库后运行一次即可刷新页面；MAPPING 里没覆盖的仓库会在终端报错。
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_JSON = ROOT / "raw" / "01-articles" / "github-stars-2026-11-15.json"
OUT = ROOT / "wiki" / "syntheses" / "GitHub 星标仓库总览.md"

# 分类组（顺序即页面顺序）
GROUPS = [
    ("G1", "智能体框架与运行时", "从“能对话”走向“能自己干活”：多 agent 编排、个人助理、agent 原生 CLI 都在这一组。"),
    ("G2", "Agent Skills 与提示工程", "本组几乎全是 skill 资产而非程序，共同点是“把某个领域的经验写成 agent 能执行的规范”。"),
    ("G3", "AI 编程工具链与模型网关", "围绕 Claude Code / Codex 等引擎做客户端、配置切换与供应商聚合，是“多引擎并存”现状的产物。"),
    ("G4", "代码智能与知识库", "用图谱或 wiki 结构替代“每次重新检索”，和本知识库是同一思路的不同实现。"),
    ("G5", "MCP、检索与数据采集", "给 agent 接外部世界的手：MCP 框架、搜索/抓取、以及 MCP 服务清单。"),
    ("G6", "学习路线、课程与面试", "数量最多的一组，说明星标里有相当比例是“打算学”而不是“正在用”。"),
    ("G7", "前端、UI 与动效可视化", "动效库与中后台模板占主导，可直接复用于交付物（PPT/网页/看板）。"),
    ("G8", "全栈脚手架与后端模板", "开箱即用的工程骨架，价值在于目录分层与鉴权/测试的默认配置。"),
    ("G9", "Java / Spring 生态与实践", "中文 Java 学习生态的头部项目集中地：7 个教程、3 个工具库、1 个清单，教程大多已停止更新。"),
    ("G10", "视觉、3D、语音与图像", "多模态方向的少量但高价值项目，含 3D 重建与零样本 TTS。"),
    ("G11", "学术论文、算法与安全", "论文复现与领域清单，适合当研究入口而非直接落地。"),
    ("G12", "金融投研、量化与加密资产", "两类东西：系统化交易的资料库，和用 agent 做投研的框架。"),
    ("G13", "资源清单、独立开发者与内容生态", "“清单的清单”，用来发现新项目，本身不含技术实现。"),
    ("G14", "桌面工具、Office 与系统增强", "提升单人效率的成品工具，其中 OfficeCLI 是少见的“给 agent 用的 Office”。"),
    ("G15", "网络与自托管运维", "把服务跑在自己的机器上：DDNS、部署平台这类“装了就一直后台运行”的小工具。"),
]

# (仓库全名, 组, 形态, 标签[], 一句话定位)
MAPPING = [
    # G1 智能体框架与运行时
    ("deepseek-ai/dsh-superagent-prototype", "G1", "框架", ["agent", "multi-agent"], "更自主的多 agent 系统原型，看它怎么定义 agent 的自治边界"),
    ("earendil-works/pi", "G1", "框架", ["agent", "cli"], "把统一 LLM API、agent loop、TUI 打包成一套工具包"),
    ("stablyai/orca", "G1", "工具", ["agent", "orchestration"], "用自有订阅批量跑 Claude Code/Codex，桌面+移动+远程运行时"),
    ("FoundationAgents/OpenManus", "G1", "框架", ["agent", "opensource"], "开源通用 agent 框架，Manus 思路的公开实现"),
    ("HKUDS/nanobot", "G1", "框架", ["agent", "personal-assistant"], "轻量自托管个人助理，接 Telegram/Discord 等聊天入口"),
    ("HKUDS/DeepTutor", "G1", "工具", ["agent", "education"], "多 agent + RAG 的终身个性化 AI 导师"),
    ("HKUDS/CLI-Anything", "G1", "工具", ["agent", "cli"], "让所有软件变成 agent 可直接调用的 CLI"),
    # G2 Agent Skills 与提示工程
    ("multica-ai/andrej-karpathy-skills", "G2", "Skill", ["agent-skills", "prompt"], "单个 CLAUDE.md 修正 Claude Code 的常见坏习惯（源自 Karpathy 的观察）"),
    ("anthropics/skills", "G2", "Skill", ["agent-skills", "official"], "Anthropic 官方 Agent Skills 公共仓库，学习 skill 写法的基准"),
    ("mattpocock/skills", "G2", "Skill", ["agent-skills", "engineering"], "一线工程师 .agents 目录里的实战 skills"),
    ("addyosmani/agent-skills", "G2", "Skill", ["agent-skills", "engineering"], "面向 AI 编程 agent 的生产级工程 skills"),
    ("DietrichGebert/ponytail", "G2", "Skill", ["agent-skills", "prompt"], "让 agent 像最懒的资深工程师那样写“最少但够用”的代码（YAGNI）"),
    ("Leonxlnx/taste-skill", "G2", "Skill", ["agent-skills", "design"], "给编程 agent 审美：艺术指导 + 参考图 + 浏览器自检，专治“AI 味页面”"),
    ("op7418/guizang-ppt-skill", "G2", "Skill", ["agent-skills", "ppt"], "生成 HTML 幻灯片的 skill，杂志风/瑞士排版 + WebGL 放映"),
    ("cathrynlavery/diagram-design", "G2", "Skill", ["agent-skills", "diagram"], "45 种图表类型的编辑级图表设计 skill（HTML+SVG，不用 Mermaid）"),
    ("tt-a1i/archify", "G2", "Skill", ["agent-skills", "diagram"], "把想法、计划或代码库直接转成可交互架构图"),
    ("greensock/gsap-skills", "G2", "Skill", ["agent-skills", "animation"], "GSAP 官方 skills，教 agent 正确使用动画库与插件"),
    ("kangarooking/cangjie-skill", "G2", "Skill", ["agent-skills", "knowledge-distillation"], "把书、长视频、播客蒸馏成可执行 Agent Skills"),
    # G3 AI 编程工具链与模型网关
    ("farion1231/cc-switch", "G3", "工具", ["ai-coding", "provider-management"], "Claude Code / Codex / OpenCode 等多引擎配置与供应商一键切换"),
    ("zhukunpenglinyutong/desktop-cc-gui", "G3", "工具", ["ai-coding", "desktop"], "多引擎 AI 编程桌面客户端（Tauri）"),
    ("ZyphrZero/kiro.rs", "G3", "工具", ["ai-coding", "client"], "Rust 实现的 Kiro 客户端"),
    ("warpdotdev/warp", "G3", "工具", ["terminal", "ai-coding"], "从终端长出来的 agentic 开发环境"),
    ("cheaper-inference/OmniRoute", "G3", "工具", ["gateway", "llm"], "单端点聚合 375 家供应商的 MIT 网关，带回退与 token 压缩"),
    ("davila7/claude-code-templates", "G3", "工具", ["ai-coding", "registry"], "Claude Code 组件（agents/commands/skills/hooks/MCP）注册表与 CLI"),
    # G4 代码智能与知识库
    ("Graphify-Labs/graphify", "G4", "工具", ["knowledge-graph", "code-intelligence"], "代码库+文档+SQL+PDF 建成可查询知识图谱，本地 AST 解析、无向量库"),
    ("colbymchenry/codegraph", "G4", "工具", ["knowledge-graph", "code-intelligence"], "随代码变更自动同步的预索引代码图谱，省 token、全程本地"),
    ("abhigyanpatwari/GitNexus", "G4", "工具", ["code-intelligence", "tool"], "零服务端的代码智能引擎"),
    ("nashsu/llm_wiki", "G4", "工具", ["llm-wiki", "knowledge-management"], "LLM 增量维护持久 wiki 的桌面应用——本知识库的同类实现"),
    # G5 MCP、检索与数据采集
    ("PrefectHQ/fastmcp", "G5", "框架", ["mcp", "python"], "Pythonic 的 MCP server/client 框架"),
    ("KnockOutEZ/wigolo", "G5", "工具", ["mcp", "search"], "本地优先的 web 搜索/抓取/研究 MCP，无需 API Key"),
    ("punkpeye/awesome-mcp-servers", "G5", "清单", ["mcp", "awesome-list"], "MCP server 大全，选型第一站"),
    ("D4Vinci/Scrapling", "G5", "框架", ["scraping", "tool"], "从单请求到全站爬取的抓取框架，自带 MCP 与反爬处理"),
    # G6 学习路线、课程与面试
    ("codecrafters-io/build-your-own-x", "G6", "教程", ["learning", "awesome-list"], "通过复刻技术来学编程的教程总集"),
    ("donnemartin/system-design-primer", "G6", "教程", ["learning", "system-design"], "大规模系统设计学习与面试指南"),
    ("nilbuild/developer-roadmap", "G6", "教程", ["learning", "roadmap"], "roadmap.sh 交互式开发者路线图"),
    ("rohitg00/ai-engineering-from-scratch", "G6", "教程", ["learning", "ai-engineering"], "从零学 AI 工程：LLM、agent、CV、RL 一条线"),
    ("bojieli/ai-agent-book", "G6", "教程", ["learning", "agent", "book"], "《深入理解 AI Agent》全书正文 + PDF + 分章代码"),
    ("datawhalechina/hello-agents", "G6", "教程", ["learning", "agent"], "《从零开始构建智能体》原理与实践教程"),
    ("Lordog/dive-into-llms", "G6", "教程", ["learning", "llm"], "《动手学大模型》系列编程实践"),
    ("CyC2018/CS-Notes", "G6", "教程", ["interview", "cs-fundamentals"], "技术面试基础知识：操作系统、网络、系统设计、Leetcode"),
    ("csguide-dabai/interview-guide", "G6", "教程", ["interview", "backend"], "后端校招八股文重点总结"),
    ("SSHeRun/CS-Xmind-Note", "G6", "教程", ["learning", "cs-fundamentals"], "408 四门专业课思维导图与笔记"),
    ("xiaomabenten/system_architect", "G6", "教程", ["exam", "architecture"], "软考高级「系统架构设计师」备考资源 + 刷题软件"),
    ("2025Emma/vibe-coding-cn", "G6", "教程", ["vibe-coding", "learning"], "Vibe Coding 中文资料（仓库无描述，按名称与主题归类，待核实）"),
    # G7 前端、UI 与动效可视化
    ("greensock/GSAP", "G7", "库", ["animation", "frontend"], "现代 Web 动画库的标杆"),
    ("juliangarnier/anime", "G7", "库", ["animation", "frontend"], "轻量 JavaScript 动画引擎"),
    ("DavidHDev/react-bits", "G7", "库", ["react", "ui", "animation"], "最大的动效/交互 React 组件库"),
    ("TailAdmin/tailadmin-free-tailwind-dashboard-template", "G7", "模板", ["tailwind", "template"], "Tailwind 后台仪表盘模板，组件齐全"),
    ("jekip/naive-ui-admin", "G7", "模板", ["vue", "admin"], "Vue3 + Naive UI 企业级中后台方案，含按钮级权限"),
    ("zclzone/vue-naive-admin", "G7", "模板", ["vue", "admin"], "轻量 Vue3 + Pinia + UnoCSS 后台模板"),
    ("lin-xin/vue-manage-system", "G7", "模板", ["vue", "admin"], "Vue3 + Element Plus 后台管理系统"),
    ("justjavac/wechat-miniapp-radar", "G7", "工具", ["miniapp", "tool"], "小程序选型、趋势追踪与迁移诊断"),
    # G8 全栈脚手架与后端模板
    ("fastapi/full-stack-fastapi-template", "G8", "模板", ["fastapi", "fullstack"], "FastAPI + React + SQLModel + Docker 官方全栈模板"),
    ("JiayuXu0/FastAPI-Template", "G8", "模板", ["fastapi", "backend"], "分层清晰的企业级 FastAPI 后端模板"),
    # G9 Java / Spring 生态与实践
    ("Snailclimb/JavaGuide", "G9", "教程", ["java", "interview"], "Java 后端面试与知识体系大全"),
    ("doocs/advanced-java", "G9", "教程", ["java", "architecture"], "Java 工程师进阶：高并发、分布式、微服务、海量数据"),
    ("itwanger/toBeBetterJavaer", "G9", "教程", ["java", "learning"], "通俗风格的 Java 学习指南：并发、JVM、企业开发"),
    ("wuyouzhuguli/SpringAll", "G9", "教程", ["spring", "learning"], "Spring Boot / Cloud / Security 循序渐进示例集"),
    ("xkcoding/spring-boot-demo", "G9", "教程", ["spring", "demo"], "Spring Boot 实战 demo 大全"),
    ("yudaocode/SpringBoot-Labs", "G9", "教程", ["spring", "distributed"], "六大专栏：Spring Boot/Cloud/Alibaba/Dubbo/MQ/分布式事务"),
    ("RudeCrab/rude-java", "G9", "教程", ["java", "demo"], "SSM/Spring Security/MinIO/Vue 多框架项目实践"),
    ("lets-mica/mica", "G9", "库", ["spring", "toolkit"], "Spring Cloud 微服务核心工具集"),
    ("justauth/JustAuth", "G9", "库", ["java", "auth"], "小而全的第三方登录组件，覆盖几十家平台"),
    ("baomidou/dynamic-datasource", "G9", "库", ["spring", "database"], "Spring Boot 多数据源、读写分离、分布式事务"),
    ("hello-go-maker/Java-project", "G9", "清单", ["java", "awesome-list"], "Java 实战项目推荐合集（电商/支付/后台/论坛）"),
    # G10 视觉、3D、语音与图像
    ("img2threejs/img2threejs", "G10", "Skill", ["3d", "threejs", "agent-skills"], "把参考图重建成可动画的 Three.js 程序（token 高效的图生 3D）"),
    ("Robbyant/lingbot-map", "G10", "论文", ["3d", "academic"], "流式 3D 重建的几何上下文 Transformer（ECCV 2026 候选）"),
    ("lucidrains/vit-pytorch", "G10", "库", ["cv", "transformer"], "Vision Transformer 的极简 PyTorch 实现"),
    ("index-tts/index-tts", "G10", "库", ["tts", "audio"], "工业级零样本可控 TTS，支持跨语种与音色克隆"),
    ("aoguai/LiYing", "G10", "工具", ["image", "automation"], "照相馆证件照后期全流程自动化（换底/裁剪/排版/压缩）"),
    # G11 学术论文、算法与安全
    ("youngfish42/Awesome-FL", "G11", "清单", ["academic", "federated-learning"], "联邦学习论文/框架/数据集全景清单，持续更新"),
    ("Yangfan-Jiang/Federated-Learning-with-Differential-Privacy", "G11", "论文", ["academic", "privacy"], "差分隐私联邦学习的 PyTorch 实现"),
    ("synxlin/deep-gradient-compression", "G11", "论文", ["academic", "distributed-training"], "ICLR'18 深度梯度压缩：分布式训练省通信带宽"),
    ("hzysvilla/Academic_Smart_Contract_Papers", "G11", "清单", ["academic", "blockchain"], "智能合约学术论文清单"),
    ("the-web3/cryptography", "G11", "教程", ["cryptography", "learning"], "人人能懂的密码学教程"),
    ("ctf-wiki/ctf-wiki", "G11", "教程", ["security", "wiki"], "CTF 知识 wiki：crypto/pwn/re/web/misc"),
    # G12 金融投研、量化与加密资产
    ("paperswithbacktest/awesome-systematic-trading", "G12", "清单", ["quant", "awesome-list"], "系统化交易库、策略、书与教程清单"),
    ("xbtlin/ai-berkshire", "G12", "框架", ["finance", "agent"], "巴菲特/芒格/段永平/李录四大师方法论 + 多 agent 价值投资研究"),
    ("HKUDS/Vibe-Trading", "G12", "框架", ["finance", "agent"], "个人交易 agent，带回测与多 agent 协作"),
    ("Tangent-Wei/crypto_info", "G12", "清单", ["crypto", "awesome-list"], "币圈工具与资料大全（交易所在内，偏引流性质）"),
    # G13 资源清单、独立开发者与内容生态
    ("ripienaar/free-for-dev", "G13", "清单", ["awesome-list", "devops"], "有免费额度的 SaaS/PaaS/IaaS 清单"),
    ("GitHubDaily/GitHubDaily", "G13", "资源站", ["awesome-list", "content"], "高质量开源项目日更推荐"),
    ("Shubhamsaboo/awesome-llm-apps", "G13", "清单", ["awesome-list", "agent"], "100+ AI agent / skill / RAG 应用合集"),
    ("timqian/chinese-independent-blogs", "G13", "清单", ["indie", "blog"], "中文独立博客列表"),
    ("1c7/chinese-independent-developer", "G13", "清单", ["indie", "content"], "中国独立开发者项目列表"),
    ("easychen/opc-methodology", "G13", "教程", ["indie", "book"], "《一人企业方法论》第二版"),
    ("vikiboss/60s", "G13", "工具", ["api", "tool"], "免费聚合 API：热搜、金价油价、天气、翻译、壁纸"),
    ("dhamaniasad/awesome-postgres", "G13", "清单", ["database", "awesome-list"], "PostgreSQL 生态资源清单"),
    # G14 桌面工具、Office 与系统增强
    ("iOfficeAI/OfficeCLI", "G14", "工具", ["office", "cli", "agent"], "给 agent 用的 Office 套件 CLI：读写 Word/Excel/PPT，免装 Office"),
    ("oblien/openship", "G15", "工具", ["devops", "self-hosted"], "自托管部署平台"),
    ("OpenCut-app/OpenCut", "G14", "工具", ["video", "tool"], "开源 CapCut 替代，浏览器内视频剪辑"),
    ("Ebullioscopic/Atoll", "G14", "工具", ["macos", "desktop"], "macOS 上的灵动岛"),
    ("CorentinTh/it-tools", "G14", "工具", ["tool", "developer-tools"], "开发者在线小工具集合，UX 出色"),
    ("DevToys-app/DevToys", "G14", "工具", ["tool", "desktop"], "开发者瑞士军刀，跨平台桌面工具箱"),
    ("ailyProject/aily-blockly", "G14", "工具", ["iot", "ide"], "硬件开发 AI IDE：Arduino / ESP32 / STM32 / MicroPython"),
    # G15 网络与自托管运维
    ("jeessy2/ddns-go", "G15", "工具", ["ddns", "network", "self-hosted"], "单文件 DDNS 客户端：把动态公网 IP 自动更新到阿里云/腾讯云/Cloudflare 等解析"),
]


def load(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    return data


def fmt_stars(n: int) -> str:
    return f"{n:,}"


def main() -> int:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_JSON
    repos = load(src)
    by_name = {r["full_name"]: r for r in repos}

    mapped = {m[0] for m in MAPPING}
    missing = sorted(set(by_name) - mapped)
    unknown = sorted(mapped - set(by_name))
    if missing or unknown:
        if missing:
            print("快照里有未分类仓库（请补进 MAPPING）：")
            for n in missing:
                print("  -", n, "|", by_name[n].get("description"))
        if unknown:
            print("MAPPING 里有快照中不存在的仓库（可能已取消星标）：")
            for n in unknown:
                print("  -", n)
        return 1

    # 统计
    langs: dict[str, int] = {}
    forms: dict[str, int] = {}
    tiers = {"10 万+": 0, "5 万–10 万": 0, "1 万–5 万": 0, "1 万以下": 0}
    pushed_years: dict[str, int] = {}
    for r in repos:
        lang = r.get("language") or "未标注"
        langs[lang] = langs.get(lang, 0) + 1
        s = r["stars"]
        if s >= 100000:
            tiers["10 万+"] += 1
        elif s >= 50000:
            tiers["5 万–10 万"] += 1
        elif s >= 10000:
            tiers["1 万–5 万"] += 1
        else:
            tiers["1 万以下"] += 1
        year = (r.get("pushed") or "")[:4] or "未知"
        pushed_years[year] = pushed_years.get(year, 0) + 1
    for name, _g, form, _tags, _note in MAPPING:
        forms[form] = forms.get(form, 0) + 1

    group_names = {gid: (title, note) for gid, title, note in GROUPS}
    ai_like = sum(1 for m in MAPPING if m[1] in ("G1", "G2", "G3", "G4"))
    backend_like = sum(1 for m in MAPPING if m[1] in ("G6", "G9"))

    lines: list[str] = []
    w = lines.append

    w("---")
    w("title: GitHub 星标仓库总览")
    w("type: synthesis")
    w("date: 2026-11-14")
    w("tags: [github-stars, 资源盘点, agent, agent-skills, 学习资源]")
    w("sources:")
    w(f"  - {src.relative_to(ROOT).as_posix()}")
    w("---")
    w("")
    w("# GitHub 星标仓库总览（2026-11）")
    w("")
    w("## 一句话结论")
    w("")
    w(
        f"共 {len(repos)} 个公开星标仓库。按形态看，**工具（{forms.get('工具', 0)}）与教程（{forms.get('教程', 0)}）"
        f"合计 {forms.get('工具', 0) + forms.get('教程', 0)} 个，占了近一半**，纯框架只有 {forms.get('框架', 0)} 个——"
        "这份星标更像“工具箱 + 工具书”，而不是一套造轮子的技术栈。按主题看，与 AI agent / AI 编程直接相关的 "
        f"G1–G4 合计 {ai_like} 个（{ai_like / len(repos):.0%}），是单一方向里最集中的一块；"
        f"其次是中文后端与面试资料（G6+G9 合计 {backend_like} 个）。"
    )
    w("")
    w("## 数据与方法")
    w("")
    w("- 数据源：GitHub 公开 API `GET /users/GY0316/starred`，抓取时间 2026-11-14，快照存于 "
        f"`{src.relative_to(ROOT).as_posix()}`，字段与口径见 [[GitHub 星标快照 2026-11]]。")
    w("- 口径：仅包含**公开**星标仓库；GitHub 私有星标、以及用户在网页端自建的 star 列表（Lists）不在 API 返回里，因此本表不含“用户自己的分组标签”。")
    w("- 分类方式：先按**主题**分 14 组（组内按星数降序），再给每个仓库两个维度的标签——领域标签（如 `#agent`）与形态标签（框架/Skill/工具/库/模板/教程/清单/论文/资源站）。")
    w("- “定位”一列是根据仓库名、描述与 topics 写的一句话判断，不是仓库的官方介绍；描述缺失的仓库已单独标注。")
    w("")
    w("## 按项目形态分布")
    w("")
    w("| 形态 | 数量 | 代表仓库 |")
    w("| --- | --- | --- |")
    order = ["工具", "教程", "Skill", "清单", "框架", "库", "模板", "论文", "资源站"]
    for form in order:
        if form not in forms:
            continue
        reps = [m[0] for m in MAPPING if m[2] == form]
        reps_sorted = sorted(reps, key=lambda n: by_name[n]["stars"], reverse=True)[:3]
        w(f"| {form} | {forms[form]} | {'、'.join(reps_sorted)} |")
    w("")
    w("## 分类清单")
    w("")

    for gid, title, note in GROUPS:
        items = [m for m in MAPPING if m[1] == gid]
        items.sort(key=lambda m: by_name[m[0]]["stars"], reverse=True)
        w(f"### {gid} {title}（{len(items)}）")
        w("")
        w(f"> {note}")
        w("")
        w("| 仓库 | 语言 | ★ | 形态 | 定位 | 标签 |")
        w("| --- | --- | --- | --- | --- | --- |")
        for name, _g, form, tags, cn in items:
            r = by_name[name]
            lang = r.get("language") or "—"
            url = r.get("url") or f"https://github.com/{name}"
            tagcell = " ".join(f"`#{t}`" for t in tags)
            w(f"| [{name}]({url}) | {lang} | {fmt_stars(r['stars'])} | {form} | {cn} | {tagcell} |")
        w("")

    w("## 横向观察")
    w("")
    w(f"- **语言分布**：" + "，".join(f"{k} {v}" for k, v in sorted(langs.items(), key=lambda x: -x[1])[:6])
      + "。空语言多为纯 Markdown/提示词类仓库，代码不是主体。")
    w("- **星数梯队**：" + "，".join(f"{k} {v} 个" for k, v in tiers.items()) + "。星数在这里只反映流行度，不代表可维护性。")
    w("- **活跃度（最后推送年份）**：" + "，".join(f"{k} 年 {v} 个" for k, v in sorted(pushed_years.items(), reverse=True))
      + "。可据此判断哪些项目已停止更新、哪些仍在快速迭代。")
    w("- **同一主题的重复度偏高**：Java 教程（JavaGuide / advanced-java / toBeBetterJavaer / CS-Notes）与 Spring 示例"
      "（SpringAll / spring-boot-demo / SpringBoot-Labs / rude-java）内容高度重叠；前端中后台模板有 4 个同质项目。"
      "后续若要深入，每组只需保留 1–2 个继续读。")
    w("- **skill 类项目几乎都不靠代码取胜**：这一批（`#agent-skills`）主体是 Markdown 写的规范 + 少量脚本，"
      "说明 agent 能力的瓶颈正在从“能不能实现”转向“领域知识和验收标准写得够不够清楚”。")
    w("")
    w("## 与本知识库的关系")
    w("")
    w("星标里有一批项目和本库（Karpathy LLM Wiki 模式）在做同一件事——**把资料沉淀成可复用的结构化知识，而不是每次重新检索**：")
    w("")
    w("- [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki)：同一模式的桌面实现，可直接对照它的页面组织与增量策略。")
    w("- [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) 与 [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)："
      "用图谱替代向量库的路线——本库 AGENTS.md 明确“不做向量检索”，这两者提供了另一种“确定性 + 可解释边”的参照。")
    w("- [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill)：把书/长视频/播客蒸馏成 skill，"
      "与 ingest 的产出目标（可复用的知识页）相近，可借鉴它的蒸馏模板。")
    w("- [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)、"
      "[anthropics/skills](https://github.com/anthropics/skills)：本仓库 `CLAUDE.md/AGENTS.md` 的写法可直接对标这两处。")
    w("- [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)、[datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents)："
      "后续 ingest agent 主题时的首选读物（成体系、有代码）。")
    w("")
    w("## 尚存的缺口 / 待研究")
    w("")
    w("- [ ] 星标里 `#agent-skills` 的 12 个 skill，实际质量差异很大（星数≠可用），需要挑 3 个真跑一遍再评。")
    w("- [ ] `2025Emma/vibe-coding-cn` 无仓库描述，定位待核实。")
    w("- [ ] GitHub 网页端自建的 star 列表（Lists）未纳入，若用户有分组习惯，可导出后合并进本表。")
    w("- [ ] 私有星标不可见，本表可能少于真实星标总数。")
    w("- [ ] 下一步候选：按组各 ingest 1 个代表仓库（先 G4 知识库组与 G2 skill 组），生成实体页与概念页。")
    w("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"已生成：{OUT}")
    print(f"仓库数 {len(repos)}｜组 {len(GROUPS)}｜形态 {len(forms)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
