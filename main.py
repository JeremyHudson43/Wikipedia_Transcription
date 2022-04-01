import os
import pyttsx3
import wikipedia
from moviepy.editor import concatenate_audioclips, AudioFileClip
from pydub import AudioSegment
import time

articles_to_get = open("stuff_to_transcribe.txt", "r").readlines()

engine = pyttsx3.init()
engine.setProperty("rate", 400)

volume = engine.getProperty('volume')
engine.setProperty('volume', 0.5)


def scrape_wikipedia(articles_to_get):
    counter = 1

    for article in articles_to_get:
        try:
            if not os.path.exists(f'./output_mp3/{counter}_{article}.mp3'):
                article = article.strip()

                if 'Level 2' in article:
                    article = article.replace('(Level 2)', '')
                elif 'Level 1' in article:
                    article = article.replace('(Level 1)', '')

                p = wikipedia.page(article, auto_suggest=False)

                content = p.content.split('== See also ==')[0]

                engine.save_to_file(content, f'./output_mp3/{counter}_{article}.mp3')

                # run and wait method, it processes the voice commands.
                engine.runAndWait()

                sound = AudioSegment.from_file(f"./output_mp3/{counter}_{article}.mp3")
                sound.export(f"./output_mp3/{counter}_{article}.mp3", format="mp3", bitrate="64k")

                counter = counter + 1

                if counter % 10 == 0:
                    time.sleep(3)

        except Exception as err:
            print(err)


scrape_wikipedia(articles_to_get)
