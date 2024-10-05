import os
import subprocess
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech
from pydub import AudioSegment

# Replace these with your Google Cloud API credentials and settings
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'your-credentials.json'
translate_client = translate.Client()
speech_client = speech.SpeechClient()
tts_client = texttospeech.TextToSpeechClient()

# Function to extract audio from video
def extract_audio(video_file, audio_file):
    command = f"ffmpeg -i {video_file} -vn -acodec pcm_s16le -ar 44100 -ac 2 {audio_file}"
    subprocess.call(command, shell=True)

# Function to transcribe audio to text using Google Speech-to-Text API
def transcribe_audio(audio_file):
    with open(audio_file, 'rb') as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='en-US'
    )
    response = speech_client.recognize(config=config, audio=audio)
    transcript = ''
    for result in response.results:
        transcript += result.alternatives[0].transcript + ' '
    return transcript.strip()

# Function to translate text to multiple languages
def translate_text(text, target_languages):
    translations = {}
    for target_language in target_languages:
        translation = translate_client.translate(text, target_language=target_language)
        translations[target_language] = translation['translatedText']
    return translations

# Function to synthesize text to speech using Google Text-to-Speech API
def synthesize_speech(text, output_file, target_language):
    input_text = texttospeech.SynthesisInput(text=text)
    voice_params = texttospeech.VoiceSelectionParams(
        language_code=target_language,
        name=target_language + '-Wavenet-B',
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
    )
    response = tts_client.synthesize_speech(
        input=input_text, voice=voice_params, audio_config=audio_config
    )
    with open(output_file, 'wb') as out_file:
        out_file.write(response.audio_content)

# Function to merge translated audio with the original video
def merge_audio_with_video(video_file, translated_audio_file, output_video_file):
    video = AudioSegment.from_file(video_file)
    audio = AudioSegment.from_file(translated_audio_file)
    mixed_audio = video.overlay(audio)
    mixed_audio.export(output_video_file, format='mp4')

# Paths to input video and output files
video_file = 'input_video.mp4'
audio_file = 'audio.wav'
translated_audio_file = 'translated_audio.wav'
output_video_file = 'output_video.mp4'

# Extract audio from the video
extract_audio(video_file, audio_file)

# Transcribe audio to text
transcript = transcribe_audio(audio_file)

# Define target languages for translation
target_languages = ['hi', 'gu', 'mr', 'ta', 'te', 'kn', 'ml']

# Translate text to target languages
translations = translate_text(transcript, target_languages)

# Synthesize translated text into speech and merge with video
for lang in target_languages:
    translated_audio_file = f'translated_audio_{lang}.wav'
    synthesize_speech(translations[lang], translated_audio_file, lang)
    merge_audio_with_video(video_file, translated_audio_file, output_video_file)
