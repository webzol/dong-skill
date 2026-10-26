# gzh-skill 一键安装脚本 (Windows / PowerShell)
# 把整个 skill（含 design / wx 两套引擎）复制到所有主流 AI 工具的 skill 目录。
#
# 用法：
#   powershell -ExecutionPolicy Bypass -File .\install.ps1            # 只装全局（推荐）
#   powershell -ExecutionPolicy Bypass -File .\install.ps1 -Project   # 额外装到当前目录的 .claude\skills
#
# 语义：整包替换（先删目标目录再复制），避免源里删掉的脚本残留在旧安装里。

param(
    [switch]$Project
)

$ErrorActionPreference = "Stop"
$src = $PSScriptRoot            # skill 包根
$name = "gzh-skill"

$targets = @()

# Claude Code（全局 ~/.claude/skills/）
$targets += Join-Path $HOME ".claude\skills\$name"

# Codex 及开放 Agent Skills 标准工具（~/.agents/skills/）
$targets += Join-Path $HOME ".agents\skills\$name"

# 项目级 Claude Code：只在显式 -Project 时安装，避免"在哪个目录跑就装到哪"
if ($Project) {
    $projClaude = Join-Path (Get-Location) ".claude\skills\$name"
    if ($projClaude -ne (Join-Path $HOME ".claude\skills\$name")) { $targets += $projClaude }
}

Write-Host "==> gzh-skill 安装到以下位置（整包替换）：" -ForegroundColor Cyan
foreach ($t in $targets) {
    try {
        $parent = Split-Path $t -Parent
        if ($parent) { New-Item -ItemType Directory -Force -Path $parent | Out-Null }
        if (Test-Path $t) { Remove-Item $t -Recurse -Force }
        Copy-Item -Path $src -Destination $t -Recurse -Force
        Write-Host "    [写入] $t" -ForegroundColor Green
    } catch {
        Write-Host "    [失败] $t -> $($_.Exception.Message)" -ForegroundColor Red
    }
}

# 斜杠命令：/zaobao 跑每日热点
$cmdSrc = Join-Path $src "commands\zaobao.md"
if (Test-Path $cmdSrc) {
    foreach ($dir in @((Join-Path $HOME ".claude\commands"), (Join-Path $HOME ".config\opencode\command"))) {
        try {
            New-Item -ItemType Directory -Force -Path $dir | Out-Null
            Copy-Item $cmdSrc (Join-Path $dir "zaobao.md") -Force
            Write-Host "    [命令] $(Join-Path $dir 'zaobao.md')" -ForegroundColor Green
        } catch {
            Write-Host "    [命令失败] $dir -> $($_.Exception.Message)" -ForegroundColor Red
        }
    }
}

Write-Host ""
Write-Host "==> 完成。请重启你的 AI 会话使技能生效。" -ForegroundColor Cyan
Write-Host ""
Write-Host "==> 换机器核对清单（对应 DAILY_NEWS_WORKFLOW.md §0.2，装完先看一眼）" -ForegroundColor Yellow

# 1) 成品根目录
$wxOut = "E:\WX"
$wxState = if (Test-Path $wxOut) { "已存在" } else { "不存在" }
if (-not (Test-Path $wxOut) -and (Test-Path "E:\")) {
    try { New-Item -ItemType Directory -Force -Path $wxOut | Out-Null; $wxState = "已自动创建" } catch { }
}
Write-Host ("    1) 成品根目录  {0}  [{1}]" -f $wxOut, $wxState)
Write-Host "       要改就改：DAILY_NEWS_WORKFLOW.md §0.2 第 1 行 + §7，以及 AGENTS.md「常驻约定」"
if (-not (Test-Path $wxOut)) {
    Write-Host ("       E: 盘不存在或建不了 → 手动建：New-Item -ItemType Directory -Force -Path <你的目录>") -ForegroundColor Yellow
}

# 2) 仓库路径
$repoRoot = Split-Path $src -Parent
Write-Host ("    2) 仓库路径    {0}" -f $repoRoot)
Write-Host "       通常不用改：脚本全用相对路径，只有 §6 的 wrap_preview.py 靠 ..\engine-design 定位"

# 3) 浏览器
$browser = @(
    "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
    "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
    "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe",
    "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1
if ($browser) {
    Write-Host ("    3) 浏览器      {0}  [OK]" -f $browser)
} else {
    Write-Host "    3) 浏览器      未找到 Chrome / Edge  [缺] → xshot.ps1 截图会失败，先装一个" -ForegroundColor Yellow
}

Write-Host "    · 这三处就够，其余脚本会自动探测；改完不用重装，直接跑 /zaobao"
Write-Host ""
Write-Host "==> 使用提示：" -ForegroundColor Cyan
Write-Host "    · 每日 AI 热点：说「早报」/「今天的热点」/「每日 3 篇」，或运行 /zaobao"
Write-Host "    · 排版：说「公众号排版」或运行 /gzh-skill；默认 minimal-tech × dongpro"
Write-Host "    · 指定主题：例如「排版文章使用千问 qianwen 主题」"
Write-Host "    · 产物自动归档到 generated/<当天日期>/，一个带「复制」按钮的 HTML，点按钮即可粘贴公众号"
