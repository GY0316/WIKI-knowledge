#!/usr/bin/env python3
"""知识库机械体检：死链、孤儿页、索引缺失、frontmatter 缺字段、sources 路径失效、待 ingest 资料。

用法:
  python3 scripts/lint.py            # 输出报告，有问题时退出码为 1
  python3 scripts/lint.py --json     # 机器可读输出
语义类问题（矛盾、过时、概念缺页）脚本不判断，由 /lint skill 交给 AI 处理。
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
SPECIAL = {"index", "log", "gaps"}  # 非内容页：不要求入链/索引登记
REQUIRED = {
    "source": ["title", "type", "sources", "date"],
    "concept": ["title", "type"],
    "entity": ["title", "type", "category"],
    "synthesis": ["title", "type", "date"],
}
FENCE = re.compile(r"```.*?```|~~~.*?~~~", re.S)
INLINE = re.compile(r"`[^`\n]*`")
LINK = re.compile(r"\[\[([^\]\n]+?)\]\]")


def strip_code(text):
    return INLINE.sub("", FENCE.sub("", text))


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    return (m.group(1), text[m.end():]) if m else (None, text)


def parse_fm(fm):
    """极简 YAML：只取顶层键，及其下的 '- ' 列表项或行内值。"""
    out, key = {}, None
    for line in fm.splitlines():
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            out[key] = [] if val in ("", "[]") else val
            continue
        m = re.match(r"^\s*-\s+(.*)$", line)
        if m and key:
            if not isinstance(out.get(key), list):
                out[key] = []
            out[key].append(m.group(1).strip())
    return out


def targets(body):
    for raw in LINK.findall(strip_code(body)):
        name = raw.split("|")[0].split("#")[0].strip()
        if name:
            yield name


def main():
    pages = {}  # stem -> Path
    dup = []
    for p in sorted(WIKI.rglob("*.md")):
        if p.stem in pages:
            dup.append(str(p.relative_to(ROOT)))
        pages[p.stem] = p

    inbound = {s: set() for s in pages}
    index_links = set()
    dead, badfm, badsrc = [], [], []

    for stem, p in pages.items():
        rel = str(p.relative_to(ROOT))
        text = p.read_text(encoding="utf-8")
        fm_raw, body = split_frontmatter(text)
        for t in targets(body):
            if t not in pages:
                dead.append(f"{rel} -> [[{t}]]")
            elif stem == "index":
                index_links.add(t)
            elif stem not in SPECIAL and t != stem:
                inbound[t].add(stem)
        if stem in SPECIAL:
            continue
        if fm_raw is None:
            badfm.append(f"{rel}: 缺少 frontmatter")
            continue
        fm = parse_fm(fm_raw)
        typ = fm.get("type")
        for k in REQUIRED.get(typ, ["title", "type"]):
            if k not in fm:
                badfm.append(f"{rel}: 缺少字段 {k}")
        for s in fm.get("sources", []) if isinstance(fm.get("sources"), list) else []:
            if s.startswith("raw/"):
                alt = s.replace("raw/", "raw/09-archive/", 1)
                if not (ROOT / s).exists() and not (ROOT / alt).exists():
                    badsrc.append(f"{rel}: 找不到 {s}")

    content = [s for s in pages if s not in SPECIAL]
    orphans = [str(pages[s].relative_to(ROOT)) for s in content if not inbound[s]]
    unindexed = [str(pages[s].relative_to(ROOT)) for s in content if s not in index_links]

    pending = [
        str(p.relative_to(ROOT))
        for p in sorted(RAW.rglob("*"))
        if p.is_file()
        and p.name not in (".gitkeep", ".DS_Store")
        and "09-archive" not in p.parts
        and "assets" not in p.parts
    ]

    report = {
        "死链": dead,
        "孤儿页": orphans,
        "索引缺失": unindexed,
        "frontmatter 问题": badfm,
        "sources 路径失效": badsrc,
        "重名页面": dup,
    }
    info = {"待 ingest 的 raw 文件": pending}

    if "--json" in sys.argv:
        print(json.dumps({**report, **info}, ensure_ascii=False, indent=2))
    else:
        print(f"扫描 {len(pages)} 个 wiki 页面（其中内容页 {len(content)}）\n")
        for k, v in {**report, **info}.items():
            print(f"## {k}：{len(v)}")
            for item in v:
                print(f"  - {item}")
        print()
    return 1 if any(report.values()) else 0


if __name__ == "__main__":
    sys.exit(main())
