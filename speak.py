from openai import OpenAI
import playsound
import os
import datetime
from config import api_key, delete_recordings

client = OpenAI(api_key=api_key)

def speak(phrase):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=phrase,
    )
    print(datetime.datetime.now())
    filename = str(datetime.datetime.now()) + '.mp3'

    response.stream_to_file(filename)
    playsound.playsound(filename)
    if delete_recordings is True:
        os.remove(filename)
