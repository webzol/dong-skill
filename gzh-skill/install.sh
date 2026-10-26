#!/usr/bin/env bash
# gzh-skill 一键安装脚本 (macOS / Linux)
# 把整个 skill（含 design / wx 两套引擎）复制到所有主流 AI 工具的 skill 目录。
#
# 用法：
#   bash install.sh            # 只装全局（推荐）
#   bash install.sh --project  # 额外装到当前目录的 .claude/skills
#
# 语义：整包替换（先删目标目录再复制），避免源里删掉的脚本残留在旧安装里。
set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)"   # skill 包根
NAME="gzh-skill"
PROJECT=0
[ "${1:-}" = "--project" ] && PROJECT=1

targets=(
  "${HOME}/.claude/skills/${NAME}"    # Claude Code 全局
  "${HOME}/.agents/skills/${NAME}"    # Codex 及开放 Agent Skills 标准工具
)

if [ "$PROJECT" = "1" ]; then
  proj="$(pwd)/.claude/skills/${NAME}"
  [ "$proj" != "${HOME}/.claude/skills/${NAME}" ] && targets+=("$proj")
fi

echo "==> gzh-skill 安装到以下位置（整包替换）："
for t in "${targets[@]}"; do
  mkdir -p "$(dirname "$t")"
  rm -rf "$t"
  cp -R "$SRC" "$t"
  echo "    [写入] $t"
done

# 斜杠命令：/zaobao 跑每日热点
if [ -f "$SRC/commands/zaobao.md" ]; then
  for d in "${HOME}/.claude/commands" "${HOME}/.config/opencode/command"; do
    mkdir -p "$d"
    cp "$SRC/commands/zaobao.md" "$d/zaobao.md"
    echo "    [命令] $d/zaobao.md"
  done
fi

echo ""
echo "==> 完成。请重启你的 AI 会话使技能生效。"
echo ""
echo "==> 📖 使用提示："
echo "    · 每日 AI 热点：说「早报」/「今天的热点」/「每日 3 篇」，或运行 /zaobao"
echo "    · 排版：说「公众号排版」或运行 /gzh-skill；默认 minimal-tech × dongpro"
echo "    · 指定主题：例如「排版文章使用千问 qianwen 主题」「用摸鱼绿排这篇」"
echo "    · 指定模板（wx 引擎）：例如「科技蓝 + 卡片模板」"
echo "    · 产物自动归档到 generated/<当天日期>/，一个带「复制」按钮的 HTML，点按钮即可粘贴公众号"
