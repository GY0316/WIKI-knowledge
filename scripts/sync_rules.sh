#!/usr/bin/env bash
# 以 CLAUDE.md 为准，同步到 AGENTS.md（供 Codex/OpenCode 读取）。
# 用法: scripts/sync_rules.sh          同步
#       scripts/sync_rules.sh --check  仅检查是否一致（不一致时退出码 1）
set -euo pipefail
cd "$(dirname "$0")/.."

if [ "${1:-}" = "--check" ]; then
  if cmp -s CLAUDE.md AGENTS.md; then echo "一致"; else echo "CLAUDE.md 与 AGENTS.md 不一致，请运行 scripts/sync_rules.sh" >&2; exit 1; fi
else
  cp CLAUDE.md AGENTS.md
  echo "已同步 CLAUDE.md -> AGENTS.md"
fi
