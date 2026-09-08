#!/usr/bin/env bash
# gzh-skill 一键安装脚本 (macOS / Linux)
# 把整个 skill（含 design / wx 两套引擎）复制到所有主流 AI 工具的 skill 目录。
set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)"   # skill 包根
NAME="gzh-skill"

targets=(
  "${HOME}/.claude/skills/${NAME}"    # Claude Code 全局
  "${HOME}/.agents/skills/${NAME}"    # Codex 及开放 Agent Skills 标准工具
)

# 当前项目级 Claude Code
if [ "$( pwd )" != "${HOME}/.claude/skills" ]; then
  targets+=("$(pwd)/.claude/skills/${NAME}")
fi

echo "==> gzh-skill 安装到以下位置："
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
echo ""
echo "==> 📖 使用提示："
echo "    · 直说「公众号排版」或运行 /gzh-skill 即可开始"
echo "    · 指定主题：例如「排版文章使用千问 qianwen 主题」「用摸鱼绿排这篇」"
echo "    · 指定模板（wx 引擎）：例如「科技蓝 + 卡片模板」"
echo "    · 不说主题时，会自动弹出风格选择框（14 套：design 6 套 + wx 8 套），点选即可，不会默认"
echo "    · 产物自动归档到 generated/<当天日期>/，一个带「复制」按钮的 HTML，点按钮即可粘贴公众号"
