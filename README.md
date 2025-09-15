
# StyleTTS 2 Ukrainian EXP 🇺🇦

<div align="center">

**Високоякісний синтез українського мовлення на основі архітектури StyleTTS 2.**

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Platform](https://img.shields.io/badge/platform-Windows-blue.svg)]()
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()

</div>

---

## 📖 Зміст

- [✨ Огляд](#-огляд)
- [🚀 Можливості](#-можливості)
- [📂 Файлова структура](#-файлова-структура)
- [🧠 Використані моделі](#-використані-моделі)
- [📦 Залежності](#-залежності)
- [▶️ Як запустити та використовувати](#️-як-запустити-та-використовувати)
- [⚙️ Принцип роботи](#️-принцип-роботи)
- [💻 Ключові фрагменти коду](#-ключові-фрагменти-коду)

---

## ✨ Огляд

**StyleTTS 2 Ukrainian EXP** — це готова до використання портативна система для синтезу мовлення (Text-to-Speech), розроблена для генерації високоякісного українського мовлення. Система базується на сучасній архітектурі **StyleTTS 2** і надає зручний веб-інтерфейс для взаємодії.

Проект є повністю **портативним** завдяки наявності власного середовища Python (`python-portable`), що дозволяє запускати його на ОС Windows без необхідності встановлювати Python чи будь-які залежності в систему. Просто запустіть `run.bat` і відкрийте веб-сторінку в браузері.

## 🚀 Можливості

- **Якість мовлення, близька до людської**: Завдяки архітектурі StyleTTS 2.
- **Багатоголосний синтез**: Підтримка десятків різних українських голосів.
- **Вербалізація тексту**: Автоматичне перетворення чисел, дат, та абревіатур у слова.
- **Ручне керування наголосом**: Можливість вказати правильний наголос у слові за допомогою символу `+` (наприклад, `за+мок`).
- **Налаштування швидкості**: Простий слайдер для контролю темпу мовлення.
- **Портативність**: Не потребує інсталяції, працює "з коробки" на Windows.
- **Інтуїтивний веб-інтерфейс**: Створений за допомогою Gradio.

## 📂 Файлова структура

Проект має наступну структуру ключових файлів та директорій:

```
D:/STYLETTS2-UKRAINIANEXP/
├── run.bat                # ▶️ Головний файл для запуску програми
├── app.py                 # 🐍 Основний скрипт з логікою Gradio та синтезу
├── verbalizer.py          # 🗣️ Модуль для вербалізації тексту
├── config.yml             # ⚙️ Конфігурація архітектури моделі StyleTTS 2
├── requirements.txt       # 📦 Список Python-залежностей
├── filatov.pt             # 🎤 Файл стилю для одноголосної моделі
├── voices/                # 📁 Папка з файлами стилів (.pt) для багатоголосної моделі
│   ├── Анастасія Павленко.pt
│   ├── Артем Окороков.pt
│   └── ... (та багато інших)
├── models/                # 📁 Локально збережені нейронні моделі
│   ├── models--patriotyk--styletts2_ukrainian_multispeaker/ # Багатоголосна модель
│   ├── models--patriotyk--styletts2_ukrainian_single/     # Одноголосна модель
│   └── models--skypro1111--mbart-large-50-verbalization/ # Модель вербалізації
└── python-portable/       # 🐍 Ізольоване середовище Python з усіма бібліотеками
```

## 🧠 Використані моделі

Система використовує три основні нейронні моделі, які зберігаються локально:

1.  **`patriotyk/styletts2_ukrainian_multispeaker`**: Основна багатоголосна модель StyleTTS 2 для синтезу мовлення.
2.  **`patriotyk/styletts2_ukrainian_single`**: Одноголосна версія моделі.
3.  **`skypro1111/mbart-large-50-verbalization`**: Модель на основі mBART, що використовується для перетворення чисел, дат та абревіатур у слова перед синтезом.

## 📦 Залежності

Всі залежності вже встановлені у портативному середовищі `python-portable`. Основні з них:

- **`torch`**: Фреймворк для глибокого навчання.
- **`gradio` / `spaces`**: Для створення веб-інтерфейсу.
- **`transformers`**: Для роботи з моделлю вербалізації.
- **`ukrainian-word-stress`**: Для автоматичної розстановки наголосів.
- **`ipa-uk`**: Для транскрипції тексту в Міжнародний фонетичний алфавіт (IPA).
- **`styletts2-inference`**: Спеціалізована бібліотека для роботи з моделями StyleTTS 2.
- **`librosa`, `SoundFile`**: Для обробки аудіо.

## ▶️ Як запустити та використовувати

1.  **Запустіть `run.bat`**. З'явиться вікно консолі.
2.  **Дочекайтеся завантаження**. В консолі з'явиться повідомлення:
    ```
    Running on local URL: http://127.0.0.1:7860
    ```
3.  **Відкрийте адресу** `http://127.0.0.1:7860` у вашому улюбленому веб-браузері.
4.  **Використовуйте інтерфейс:**
    - Оберіть вкладку **`Multі speaker`** (рекомендовано) або `Single speaker`.
    - Введіть текст у поле `Text`.
    - Оберіть `Голос` зі списку.
    - Налаштуйте `Швидкість`.
    - Натисніть кнопку **`Синтезувати`**.
    - Прослухайте результат у полі `Audio`.

## ⚙️ Принцип роботи

Процес перетворення тексту в мовлення складається з наступних етапів:

1.  **Введення тексту**: Користувач вводить текст в інтерфейсі.
2.  **Вербалізація (опційно)**: Текст обробляється моделлю mBART для розкриття скорочень (напр., `100 грн` -> `сто гривень`).
3.  **Лінгвістична обробка**:
    - **Наголоси**: Програма автоматично розставляє наголоси.
    - **Фонетизація**: Текст з наголосами перетворюється на фонетичну транскрипцію (IPA).
4.  **Синтез**:
    - Фонеми подаються на вхід моделі **StyleTTS 2**.
    - Модель генерує аудіо-спектрограму, враховуючи обраний стиль голосу.
5.  **Вокодинг**: Спектрограма перетворюється на фінальну аудіо-хвилю.
6.  **Відтворення**: Аудіо з'являється в інтерфейсі для прослуховування.

## 💻 Ключові фрагменти коду

<details>
<summary><b><code>app.py</code> — Основний файл програми</b></summary>

```python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import glob
import os
import re
import gradio as gr

import spaces
from verbalizer import Verbalizer

import torch
from ipa_uk import ipa
from unicodedata import normalize
from styletts2_inference.models import StyleTTS2
from ukrainian_word_stress import Stressifier, StressSymbol
stressify = Stressifier()

device = 'cuda' if torch.cuda.is_available() else 'cpu'

prompts_dir = 'voices'

# --- Вказуємо локальний шлях до моделі вербалізатора ---
verbalizer = Verbalizer(model_path='models/models--skypro1111--mbart-large-50-verbalization', device=device)


def split_to_parts(text):
    split_symbols = '.?!:'
    parts = ['']
    index = 0
    for s in text:
        parts[index] += s
        if s in split_symbols and len(parts[index]) > 150:
            index += 1
            parts.append('')
    return parts


# --- Вказуємо локальний шлях до single-speaker моделі ---
single_model = StyleTTS2(hf_path='models/models--patriotyk--styletts2_ukrainian_single', device=device)
single_style = torch.load('filatov.pt')


# --- Вказуємо локальний шлях до multi-speaker моделі ---
multi_model = StyleTTS2(hf_path='models/models--patriotyk--styletts2_ukrainian_multispeaker', device=device)
multi_styles = {}

prompts_list = sorted(glob.glob(os.path.join(prompts_dir, '*.pt')))
prompts_list = [os.path.splitext(os.path.basename(p))[0] for p in prompts_list]

for audio_prompt in prompts_list:
    audio_path = os.path.join(prompts_dir, audio_prompt+'.pt')
    multi_styles[audio_prompt] = torch.load(audio_path)
    print('loaded ', audio_prompt)

models = {
    'multi': {
        'model': multi_model,
        'styles': multi_styles
    },
    'single': {
        'model': single_model,
        'style': single_style
    }
}


@spaces.GPU
def verbalize(text):
    parts = split_to_parts(text)
    verbalized = ''
    for part in parts:
        if part.strip():
            verbalized += verbalizer.generate_text(part) + ' '
    return verbalized

# ... (решта коду для створення інтерфейсу Gradio) ...

@spaces.GPU
def synthesize(model_name, text, speed, voice_name = None, progress=gr.Progress()):
    
    if text.strip() == "":
        raise gr.Error("You must enter some text")
    if len(text) > 50000:
        raise gr.Error("Text must be <50k characters")
    
    result_wav = []
    for t in progress.tqdm(split_to_parts(text)):

        t = t.strip().replace('"', '')
        if t:
            t = t.replace('+', StressSymbol.CombiningAcuteAccent)
            t = normalize('NFKC', t)
            t = re.sub(r'[᠆‐‑‒–—―⁻₋−⸺⸻]', '-', t)
            t = re.sub(r' - ', ': ', t)
            ps = ipa(stressify(t))

            if ps:
                tokens = models[model_name]['model'].tokenizer.encode(ps)
                if voice_name:
                    style = models[model_name]['styles'][voice_name]
                else:
                    style = models[model_name]['style']
                
                wav = models[model_name]['model'](tokens, speed=speed, s_prev=style)
                result_wav.append(wav)

    return 24000, torch.concatenate(result_wav).cpu().numpy()

# ... (код для створення інтерфейсу Gradio) ...

if __name__ == "__main__":
    demo.queue(api_open=True, max_size=15).launch(show_api=True)
```
</details>

<details>
<summary><b><code>verbalizer.py</code> — Модуль вербалізації</b></summary>

```python
import torch
from transformers import AutoModelForSeq2SeqLM, MBartTokenizer

class Verbalizer:
    def __init__(self, model_path: str = "ina-speech-research/Ukrainian-Verbalizer-g2p-v1", device: str = 'cpu'):
        try:
            # Викликаємо MBartTokenizer напряму, щоб уникнути помилок конвертації
            self.tokenizer = MBartTokenizer.from_pretrained(
                model_path,
                local_files_only=True
            )
            
            self.model = AutoModelForSeq2SeqLM.from_pretrained(
                model_path, 
                local_files_only=True
            )
            
        except Exception as e:
            print(f"--- An error occurred during model loading: {e}")
            raise

        self.to(device)

    def to(self, device):
        self.device = device
        self.model.to(self.device)

    def generate_text(self, text, **kwargs):
        inputs = self.tokenizer(text, return_tensors="pt")
        inputs = inputs.to(self.device)

        translated = self.model.generate(**inputs, **kwargs)
        output = [self.tokenizer.decode(t, skip_special_tokens=True) for t in translated]
        
        return output[0]
```
</details>
