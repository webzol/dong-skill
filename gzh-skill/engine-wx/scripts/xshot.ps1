param(
  [Parameter(Mandatory=$true)][string]$Url,
  [Parameter(Mandatory=$true)][string]$Name,
  [int]$W = 640,
  [int]$H = 1500,
  [int]$Wait = 25000,
  [double]$Scale = 1,
  [string]$OutDir = "$env:TEMP\opencode"
)

# Chrome headless 截图。
# 关键：必须传普通 Chrome UA，否则 X / 部分站点会 403 掉 HeadlessChrome。
# 用法：.\xshot.ps1 -Url "https://x.com/user/status/123" -Name tweet1 -W 640 -H 1500

$chrome = @(
  "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
  "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
  "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe",
  "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1

if (-not $chrome) { Write-Error "未找到 Chrome / Edge"; exit 1 }
if (-not (Test-Path $OutDir)) { New-Item -ItemType Directory -Force -Path $OutDir | Out-Null }

$out  = Join-Path $OutDir "$Name.png"
$prof = Join-Path $OutDir "prof-$Name"
$log  = Join-Path $OutDir "log-$Name.txt"
Remove-Item $out -ErrorAction SilentlyContinue

$ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
$args = @(
  '--headless=new','--disable-gpu','--no-sandbox','--hide-scrollbars',
  "--user-data-dir=$prof","--window-size=$W,$H","--virtual-time-budget=$Wait",
  "--force-device-scale-factor=$Scale",
  "--user-agent=`"$ua`"","--screenshot=$out",$Url
)
$p = Start-Process -FilePath $chrome -ArgumentList $args -Wait -PassThru -NoNewWindow -RedirectStandardError $log

if (Test-Path $out) {
  Write-Output ("OK  {0}  {1} bytes  ({2}x{3})" -f $out, (Get-Item $out).Length, $W, $H)
} else {
  Write-Output ("FAIL {0}  exit={1}" -f $Url, $p.ExitCode)
  if (Test-Path $log) { Get-Content $log -Tail 5 }
  exit 2
}

# 清理临时用户目录，避免每次截图留几十 MB 的 prof-<name>
if (Test-Path $prof) { try { Remove-Item $prof -Recurse -Force -ErrorAction Stop } catch { } }
