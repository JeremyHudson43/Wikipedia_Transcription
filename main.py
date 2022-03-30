import os

import pyttsx3
import wikipedia
from pydub import AudioSegment

articles_to_get = open("people_to_transcribe.txt", "r").readlines()

engine = pyttsx3.init()

engine.setProperty("rate", 400)

volume = engine.getProperty('volume')
engine.setProperty('volume', 0.01)


for article in articles_to_get:

    try:

        article = article.strip()

        p = wikipedia.page(article, auto_suggest=False)
        content = p.content.split('== See also ==')[0]

        engine.save_to_file(content, f'./mp3_output/{article}.wav')

        # run and wait method, it processes the voice commands.
        engine.runAndWait()

    except Exception as err:
        print(err)


all_files = os.listdir('./mp3_output')

combined = []

for file in all_files:
    print(file)
    try:
        audio = AudioSegment.from_mp3(f'./mp3_output/{file}')
        combined.append(audio)
    except Exception as err:
        print(err)

combined.export(f"./mp3_output/combined_output.wav", format="wav")
