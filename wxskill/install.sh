#!/usr/bin/env bash
# WXSkill 一键安装脚本 (macOS / Linux)
# 把本仓库复制到所有主流 AI 工具的 skill 目录。
set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)"   # 仓库根（skill 包）
NAME="wechat-typesetting"

targets=(
  "${HOME}/.claude/skills/${NAME}"    # Claude Code 全局
  "${HOME}/.agents/skills/${NAME}"    # Codex 及开放 Agent Skills 标准工具
)

# 当前项目级 Claude Code
if [ "$( pwd )" != "${HOME}/.claude/skills" ]; then
  targets+=("$(pwd)/.claude/skills/${NAME}")
fi

echo "==> WXSkill 安装到以下位置："
for t in "${targets[@]}"; do
  mkdir -p "$(dirname "$t")"
  if [ -d "$t" ]; then
    cp -R "$SRC"/. "$t"/
    echo "    [更新] $t"
  else
    cp -R "$SRC" "$t"
    echo "    [安装] $t"
  fi
done

echo ""
echo "==> 完成。请重启你的 AI 会话使技能生效。"
echo "    Claude Code 里运行 /wechat-typesetting 即可开始。"
