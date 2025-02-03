@echo off
setlocal enabledelayedexpansion
chcp 65001
color 0A

:: JL ComfyUI Installer
:: Created by John LapTev
:: https://github.com/John-LapTev

:: Установка временных переменных окружения
set APPDATA=tmp
set USERPROFILE=tmp
set TEMP=tmp

echo JL ComfyUI Installer
echo ===================
echo Created by John LapTev
echo.

:: Загрузка и установка портативного Git
if not exist "git" (
    echo Загрузка портативного Git...
    curl -L -o git.zip "https://github.com/alexbofa/BATNIKI/releases/download/assets/git.zip"
    echo Распаковка Git...
    tar -xf git.zip
    del git.zip /q
)

:: Добавляем Git в PATH
set "PATH=%~dp0git\cmd;%PATH%"

:: Загрузка и установка портативного Python
if not exist "python_embeded" (
    echo Загрузка Python 3.11.9...
    curl -L -o python.zip "https://www.python.org/ftp/python/3.11.9/python-3.11.9-embed-amd64.zip"
    echo Распаковка Python...
    powershell -command "Expand-Archive -Path python.zip -DestinationPath python_embeded"
    del python.zip

    :: Загрузка pip
    echo Загрузка pip...
    curl -L -o get-pip.py "https://bootstrap.pypa.io/get-pip.py"
    .\python_embeded\python.exe get-pip.py
    del get-pip.py

    :: Настройка путей Python
    echo python311.zip>>python_embeded\python311._pth
    echo .>>python_embeded\python311._pth
    echo python_embeded\Lib\site-packages>>python_embeded\python311._pth
)

:: Загрузка установщика
echo Загрузка скрипта установки...
curl -L -o JL_setup_ComfyUI.py "https://raw.githubusercontent.com/John-LapTev/JL-ComfyUI-Installer/main/JL_setup_ComfyUI.py"

:: Запуск Python-скрипта установки
echo Запуск установщика...
.\python_embeded\python.exe JL_setup_ComfyUI.py

echo.
echo Установка завершена!
pause