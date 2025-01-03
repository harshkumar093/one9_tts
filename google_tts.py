from gtts import gTTS
import os
# function to covert a text to a speach with the choice of language.
def tts(text='This is default text for testing the google text to speech', filename='./output.mp3', language='en', tld='us'):
    try:
        print(f"[info] Trying to create audio :: text: {text}, output_filename: {filename}, lang: {language} and tld: {tld}")
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        tts = gTTS(text=text, lang=language, tld=tld)
        tts.save(filename)
    except Exception as e:
        print(f"[error] Failed to create audio :: text: {text}, output_filename: {filename}, lang: {language}, tld: {tld}, error: {e}")
        raise Exception(e)


tts('This is default text for testing the google text to speech','./output.mp3','en','ie')