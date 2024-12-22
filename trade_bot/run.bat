@echo off
cd /d "%~dp0"

echo ========================================
echo      TRADE BOT - by CEBBOT
echo ========================================

:START

echo.
echo Islem secin:
echo 1. Modeli Egit ve Gorsellestir
echo 2. Test Modunda Calistir
echo 3. Gercek Modda Calistir (DİKKAT: Gercek para kullanilir!)
echo 4. Cikis
echo.

set /p MODE="Seciminiz (1-4): "

if "%MODE%"=="1" goto TRAIN
if "%MODE%"=="2" goto TEST
if "%MODE%"=="3" goto REAL
if "%MODE%"=="4" goto EXIT
goto START

:TRAIN
echo.
echo Model egitiliyor ve sonuclar gorsellestiriliyor...
python main.py --train
echo Model egitimi ve gorsellestirme tamamlandi.
echo Sonuclar "results" klasorunde.
goto END

:TEST
echo.
echo Test modunda calistiriliyor...
echo Lutfen TESTNET API anahtarlarinizi config.py dosyasinda dogru girdiginizden emin olun.
echo Dikkat: Test modu, sanal para ile islem yapar.
python main.py
goto END

:REAL
echo.
echo GERCEK MODDA CALISTIRILIYOR...
echo Lutfen GERCEK HESAP API anahtarlarinizi config.py dosyasında dogru girdiginizden emin olun.
echo DIKKAT: Bu modda GERCEK PARA ile islem yapilir!!!
echo Devam etmek istediginize emin misiniz? (E/H)
set /p CONFIRM="Devam edilsin mi? (E/H): "
if /I "%CONFIRM%" NEQ "E" goto START
python main.py
goto END

:EXIT
echo.
echo Cikis yapiliyor...
goto END

:END
echo.
echo Islem tamamlandi.
echo trade_bot.log dosyasinda detayli loglari bulabilirsiniz.
echo.
pause