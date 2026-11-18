# Klip hatti - Windows kurulumu (Threadripper 3960X / 128 GB icin ayarli)
# Calistirma: PowerShell'i bu klasorde acin ve su komutu girin:
#   powershell -ExecutionPolicy Bypass -File .\kurulum.ps1
# Ne yapar: Python, FFmpeg ve Ollama'yi winget ile kurar, Python ortamini hazirlar,
# yuz modelini, konusma modelini (large-v3) ve puanlama modelini (Qwen3 30B-A3B) indirir.
# Toplam indirme yaklasik 25 GB. Ekran karti kullanilmaz; tum is islemcide yapilir.

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

function Adim($m) { Write-Host "`n==> $m" -ForegroundColor Cyan }
function Yenile-Path {
    $env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [Environment]::GetEnvironmentVariable("Path", "User")
}

if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
    throw "winget bulunamadi. Microsoft Store'dan 'App Installer' uygulamasini kurup tekrar deneyin."
}

Adim "Python, FFmpeg ve Ollama kuruluyor (zaten kuruluysa atlanir)"
foreach ($id in @("Python.Python.3.12", "Gyan.FFmpeg", "Ollama.Ollama")) {
    winget install --id $id -e --silent --accept-source-agreements --accept-package-agreements
    if ($LASTEXITCODE -ne 0 -and $LASTEXITCODE -ne -1978335189) { Write-Warning "$id kurulumu kod $LASTEXITCODE ile bitti; zaten kurulu olabilir." }
}
Yenile-Path

Adim "FFmpeg altyazi destegi kontrol ediliyor"
$filters = & ffmpeg -hide_banner -filters 2>$null
if (-not ($filters -match "subtitles")) { throw "FFmpeg'de altyazi (libass) destegi yok. Gyan.FFmpeg tam surumunu kurun." }

Adim "Python ortami hazirlaniyor"
if (-not (Test-Path ".\venv")) { & py -3.12 -m venv venv }
& .\venv\Scripts\python.exe -m pip install --upgrade pip --quiet
& .\venv\Scripts\python.exe -m pip install faster-whisper opencv-python-headless numpy yt-dlp --quiet

Adim "Yuz bulucu modeli indiriliyor"
if (-not (Test-Path ".\yunet.onnx")) {
    Invoke-WebRequest -Uri "https://github.com/opencv/opencv_zoo/raw/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx" -OutFile ".\yunet.onnx"
}

Adim "Konusma modeli (large-v3-turbo, ~1.6 GB) indiriliyor"
& .\venv\Scripts\python.exe -c "from faster_whisper import WhisperModel; WhisperModel('large-v3-turbo', device='cpu', compute_type='int8'); print('large-v3-turbo hazir')"

Adim "Puanlama modeli (Qwen3 30B-A3B, ~19 GB) indiriliyor"
try { Invoke-RestMethod "http://127.0.0.1:11434/api/version" -TimeoutSec 3 | Out-Null }
catch { Start-Process ollama -ArgumentList "serve" -WindowStyle Hidden; Start-Sleep -Seconds 5 }
$model = "qwen3:30b-a3b-instruct-2507-q4_K_M"
& ollama pull $model
if ($LASTEXITCODE -ne 0) {
    Write-Warning "$model indirilemedi, qwen3:30b-a3b deneniyor."
    $model = "qwen3:30b-a3b"
    & ollama pull $model
    if ($LASTEXITCODE -ne 0) { throw "Ollama modeli indirilemedi. Ollama uygulamasinin acik oldugundan emin olun." }
}

Adim "Calistirma kisayolu (klip.cmd) yaziliyor"
$fiziksel = (Get-CimInstance Win32_Processor | Measure-Object -Property NumberOfCores -Sum).Sum
@"
@echo off
rem Kullanim: klip.cmd video.mp4 cikti_klasoru 3
set KLIP_WHISPER=large-v3-turbo
set HF_HUB_DISABLE_SYMLINKS_WARNING=1
set KLIP_MODEL=$model
set KLIP_THREADS=$fiziksel
"%~dp0venv\Scripts\python.exe" "%~dp0klip.py" %*
"@ | Set-Content -Encoding ASCII ".\klip.cmd"

Adim "Kurulum tamam"
Write-Host "Ornek kullanim:  .\klip.cmd kaynak.webm cikti 3"
Write-Host "Ayarlar: konusma modeli large-v3-turbo, puanlama modeli $model, $fiziksel islemci cekirdegi."
