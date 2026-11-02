@echo off
echo ===================================================
echo Memasang Patch Bahasa Indonesia ke Folder APK...
echo ===================================================
set "SRC=%~dp0Content"
set "DST=G:\ApkStudio\Data\stardew-valley_1.6.15.3-stardewapkvalley.com.apk-decompiled\assets\Content"

if not exist "%DST%" (
    echo [ERROR] Target folder APK tidak ditemukan: %DST%
    pause
    exit /b 1
)

xcopy "%SRC%" "%DST%" /E /I /Y /Q

echo [SUKSES] 184 file terjemahan berhasil ditimpa ke folder assets APK!
echo Sekarang kamu bisa recompile dan sign APK di ApkStudio.
pause
