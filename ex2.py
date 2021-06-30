from google.cloud import speech
from os import path
import sys
import io

client = speech.SpeechClient()

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), f"{sys.argv[1]}")

with io.open(AUDIO_FILE, "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    #sample_rate_hertz=8000,
    language_code="pt-BR",
    enable_automatic_punctuation=True,
)

response = client.recognize(config=config, audio=audio)

for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print("-" * 20)
    print(f"primeira alternativa do resultado {i}")
    print(f"Transcrição:\n{alternative.transcript}")
