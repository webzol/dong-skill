# WXSkill 一键安装脚本 (Windows / PowerShell)
# 把本仓库复制到所有主流 AI 工具的 skill 目录。

$ErrorActionPreference = "Stop"
$src = $PSScriptRoot            # 仓库根（skill 包）
$name = "wechat-typesetting"

$targets = @()

# Claude Code（全局 ~/.claude/skills/ 与项目级都给一份提示）
$claude = Join-Path $HOME ".claude\skills\$name"
$targets += $claude

# Codex 及开放 Agent Skills 标准工具（~/.agents/skills/）
$agents = Join-Path $HOME ".agents\skills\$name"
$targets += $agents

# 项目级 Claude Code（若当前在某个项目目录下可能想装到 .claude/skills/）
$projClaude = Join-Path (Get-Location) ".claude\skills\$name"
if ($projClaude -ne (Join-Path $HOME ".claude\skills\$name")) {
    $targets += $projClaude
}

Write-Host "==> WXSkill 安装到以下位置：" -ForegroundColor Cyan
foreach ($t in $targets) {
    try {
        $parent = Split-Path $t -Parent
        if ($parent) { New-Item -ItemType Directory -Force -Path $parent | Out-Null }
        if (Test-Path $t) {
            Copy-Item -Path (Join-Path $src "*") -Destination $t -Recurse -Force
            Write-Host "    [更新] $t" -ForegroundColor Green
        } else {
            Copy-Item -Path $src -Destination $t -Recurse
            Write-Host "    [安装] $t" -ForegroundColor Green
        }
    } catch {
        Write-Host "    [失败] $t -> $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "==> 完成。请重启你的 AI 会话使技能生效。" -ForegroundColor Cyan
Write-Host "    Claude Code 里运行 /wechat-typesetting 即可开始。"
