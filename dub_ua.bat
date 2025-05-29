@echo off
title DubUA - Автоматичний дубляж відео українською
cd /d D:\DubUA

:: 1. Перевірка Python
where python >nul 2>nul
if errorlevel 1 (
    echo [!] Встановіть Python 3.10 вручну та додайте до PATH
    pause
    exit /b
)

:: 2. Встановлення віртуального середовища
python -m venv venv
call venv\Scripts\activate

:: 3. Оновлення pip
python -m pip install --upgrade pip

:: 4. Встановлення залежностей
pip install git+https://github.com/suno-ai/bark.git
pip install git+https://github.com/openai/whisper.git
pip install argostranslate
pip install gradio moviepy torchaudio

:: 5. Завантаження українського пакету для ArgosTranslate
argos-translate-cli --install translate-en_uk

:: 6. Запуск Gradio
python dub_ua.py
