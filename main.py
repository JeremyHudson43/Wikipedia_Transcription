import os
import pyttsx3
import wikipedia
from moviepy.editor import concatenate_audioclips, AudioFileClip

articles_to_get = open("people_to_transcribe.txt", "r").readlines()

engine = pyttsx3.init()

engine.setProperty("rate", 400)

volume = engine.getProperty('volume')
engine.setProperty('volume', 0.01)


def scrape_wikipedia(articles_to_get):
    for article in articles_to_get:

        try:

            article = article.strip()

            p = wikipedia.page(article, auto_suggest=False)
            content = p.content.split('== See also ==')[0]

            engine.save_to_file(content, f'./output_wav/{article}.wav')

            # run and wait method, it processes the voice commands.
            engine.runAndWait()

        except Exception as err:
            print(err)


def concatenate_audio_moviepy(audio_clip_paths, output_path):
    clips = [AudioFileClip(os.path.join(output_path, c)) for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(os.path.join(output_path, 'combined.mp3'))


all_files = os.listdir('./output_wav')

scrape_wikipedia(articles_to_get)
concatenate_audio_moviepy(all_files, './output_wav')
