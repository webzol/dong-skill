# gzh-skill 一键安装脚本 (Windows / PowerShell)
# 把整个 skill（含 design / wx 两套引擎）复制到所有主流 AI 工具的 skill 目录。

$ErrorActionPreference = "Stop"
$src = $PSScriptRoot            # skill 包根
$name = "gzh-skill"

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

Write-Host "==> gzh-skill 安装到以下位置：" -ForegroundColor Cyan
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
Write-Host ""
Write-Host "==> 使用提示：" -ForegroundColor Cyan
Write-Host "    · 直说「公众号排版」或运行 /gzh-skill 即可开始"
Write-Host "    · 指定主题：例如「排版文章使用千问 qianwen 主题」「用摸鱼绿排这篇」"
Write-Host "    · 指定模板（wx 引擎）：例如「科技蓝 + 卡片模板」"
Write-Host "    · 不说主题时，会自动弹出风格选择框（14 套：design 6 套 + wx 8 套），点选即可，不会默认"
Write-Host "    · 产物自动归档到 generated/<当天日期>/，一个带「复制」按钮的 HTML，点按钮即可粘贴公众号"
