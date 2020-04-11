@echo off

:start
cls
echo The current IP configuration:
netsh int ip show config LAN
echo.
echo Choose:
echo [A] Set Static IP
echo [B] Set DHCP
echo [C] Dont' change config
echo.

:choice
SET /P C=[A,B,C]?
for %%? in (A) do if /I "%C%"=="%%?" goto A
for %%? in (B) do if /I "%C%"=="%%?" goto B
for %%? in (C) do if /I "%C%"=="%%?" goto C
goto choice

:A
echo.
echo Please enter Static IP Address Information
echo Static IP Address:
set /p IP_Addr=

echo Default Gateway:
set /p D_Gate=

:: echo "Subnet Mask:"
:: set /p Sub_Mask=

echo Setting Static IP Information
echo .
netsh interface ip set address "LAN" static %IP_Addr% 255.255.255.0 %D_Gate% 1
echo Configuration loaded
echo Waiting 5 seconds
ping 127.0.0.1 -n 6 > nul
netsh int ip show config LAN
goto D

:B
echo Resetting IP Address and Subnet Mask For DHCP
netsh int ip set address name = "LAN" source = dhcp
ipconfig /renew
echo Waiting 5 seconds
ping 127.0.0.1 -n 6 > nul
echo Here are the new settings for %computername%:
netsh int ip show config LAN
goto E

:C
echo Exiting...
pause
goto end

:D
echo.
echo.
echo.
echo "Do you want to try ping to the server? (Y/N)"
set /p CH=[Y,N]?
for %%? in (Y) do if /I "%CH%"=="%%?" goto IP
for %%? in (N) do if /I "%CH%"=="%%?" goto restart
goto D

:IP
echo.
echo.
echo.
echo "Give me the server IP:"
set /p Server_IP=
echo.

ping %Server_IP%

:restart
echo.
echo.
echo.
echo "Choose:"
echo "[S] Start configuration again"
echo "[F] Finish program"
:E
set /p CH=[S,F]?
for %%? in (S) do if /I "%CH%"=="%%?" goto start
for %%? in (F) do if /I "%CH%"=="%%?" goto end
goto E

:end