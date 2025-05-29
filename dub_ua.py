import os, subprocess, tempfile, whisper
from bark import generate_audio, SAMPLE_RATE
from bark.generation import preload_models
from argostranslate import package, translate
from moviepy.editor import VideoFileClip, AudioFileClip
import gradio as gr, numpy as np, scipy.io.wavfile

preload_models()
model = whisper.load_model("medium")
installed_packages = package.get_installed_packages()
en_uk = [p for p in installed_packages if p.from_code == "en" and p.to_code == "uk"]
if en_uk: translation = en_uk[0].get_translation()
else: raise Exception("Пакет en→uk не знайдено.")

def process_video(video_path):
    audio_path = tempfile.mktemp(suffix=".wav")
    subprocess.run(["ffmpeg", "-i", video_path, "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", audio_path],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    result = model.transcribe(audio_path, language="en")
    original_text = result["text"]
    translated_text = translation.translate(original_text)
    return original_text, translated_text, video_path

def synthesize_and_merge(translated_text, video_path):
    audio_array = generate_audio(translated_text)
    out_audio_path = tempfile.mktemp(suffix=".wav")
    scipy.io.wavfile.write(out_audio_path, rate=SAMPLE_RATE, data=audio_array)
    out_video_path = os.path.join(os.path.dirname(video_path), "output_dubbed.mp4")
    subprocess.run(["ffmpeg", "-i", video_path, "-i", out_audio_path,
                    "-c:v", "copy", "-map", "0:v:0", "-map", "1:a:0",
                    "-shortest", out_video_path, "-y"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return out_video_path

with gr.Blocks(title="DubUA - Український дубляж відео") as demo:
    gr.Markdown("## Автоматичний дубляж відео українською мовою Whisper + Bark")
    video_input = gr.Video(label="1. Завантаж відео")
    transcribed = gr.Textbox(label="2. Англійський текст", lines=4)
    translated = gr.Textbox(label="3. Переклад українською", lines=4)
    final_video = gr.Video(label="4. Результат з озвученням")
    with gr.Row():
        transcribe_btn = gr.Button("Обробити")
        synth_btn = gr.Button("Озвучити та зберегти")
    transcribe_btn.click(fn=process_video, inputs=video_input, outputs=[transcribed, translated, video_input])
    synth_btn.click(fn=synthesize_and_merge, inputs=[translated, video_input], outputs=final_video)
demo.launch()
