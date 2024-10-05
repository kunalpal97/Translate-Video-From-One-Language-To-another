# import pyaudio
#
# import speech_recognition as sr
#
# r = sr.Recognizer()
#
# with sr.Microphone() as source:
#     print("Begin recording ")
#
#     audio = r.listen(source)
#
# try:
#     print(r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Google specch recognization could not understand audio")
# except sr.RequestError as e:
#     print("Could not request result from google speech recognition services; {0}",format(e))

import speech_recognition as sr

from os import path
audio_file = path.join("test1.mp3")

r = sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio = r.record(source)

try:

    print("Audio to text : " +r.recognize_google(audio))
    first_line = r.recognize_google(audio)


except sr.UnknownValueError:

    print("Google speech recognition could not understand audio")

except sr.RequestError as e:
    print("Could not request result from google speech recognition services; {0}",format(e))