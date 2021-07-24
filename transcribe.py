#!/usr/bin/env python3

import speech_recognition as sr

# ffmpeg -i audio.ogg audio.wav (para converter de .ogg (ou outro) para .wav)

from os import path
import sys

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), f"{sys.argv[1]}")

# usar AUDIO_FILE como fonte
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as fonte:
    r.adjust_for_ambient_noise(fonte) # se necessaario
    audio = r.record(fonte)  # le todo o arquivo de audio para a memoria

#print("Áudio em memória.")
try:
    # Para testes, estamos usando a chave default da API
    # par usar outra chave de API, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`

    print(r.recognize_google(audio, language="pt-BR"))
except sr.UnknownValueError:
    print("Google Speech Recognition não entendeu o áudio")
except sr.RequestError as e:
    print(f"Não foi possível solicitar resultados do serviço Google Speech Recognition: {e}")
