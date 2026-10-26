# 每天开机预建当天目录（可选）。不生成内容，只准备落地位置。
# 注册（管理员 PowerShell，执行一次）：
#   schtasks /create /tn "GZH-Daily-Prep" /tr "powershell -ExecutionPolicy Bypass -File E:\dong-skill\gzh-skill\engine-wx\scripts\daily_prep.ps1" /sc daily /st 08:30
# 取消：
#   schtasks /delete /tn "GZH-Daily-Prep" /f

$today = Get-Date -Format 'yyyy-MM-dd'
$dirs = @("E:\WX\$today", "E:\dong-skill\generated\$today")
foreach ($d in $dirs) {
  if (-not (Test-Path $d)) { New-Item -ItemType Directory -Force -Path $d | Out-Null }
}
Write-Output "ready: $($dirs -join ' , ')"
