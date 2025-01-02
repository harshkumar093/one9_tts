from gtts import gTTS
import os
# function to covert a text to a speach with the choice of language.
def tts(text='This is default text for testing the google text to speech', filename='./output.mp3', language='en'):
    print(text, filename, language)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    tts = gTTS(text=text, lang=language)
    tts.save(filename)
