#!/usr/bin/env python3

import speech_recognition as sr

# ffmpeg -i audio.ogg audio.wav (to convert from .ogg to .wav)

from os import path
import sys

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), f"{sys.argv[1]}")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    r.adjust_for_ambient_noise(source) # if necessary
    audio = r.record(source)  # read the entire audio file

#print("Áudio em memória.")
# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`

    print(r.recognize_google(audio, language="pt-BR"))
except sr.UnknownValueError:
    print("Google Speech Recognition não entendeu o áudio")
except sr.RequestError as e:
    print(f"Não foi possível solicitar resultados do serviço Google Speech Recognition: {e}")
