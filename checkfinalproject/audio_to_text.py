from google.cloud import speech_v1p1beta1 as speech
from pydub import AudioSegment

def transcribe_audio_and_save(audio_file_path, credentials_json_path, output_text_file):
    audio = AudioSegment.from_mp3(audio_file_path)
    wav_file_path = audio_file_path.replace(".mp3", ".wav")
    audio.export(wav_file_path, format="wav")
    # Initialize the Google Speech-to-Text client with your service account credentials
    client = speech.SpeechClient.from_service_account_json(credentials_json_path)

    # Read the audio file
    with open(audio_file_path, 'rb') as audio_file:
        content = audio_file.read()

    # Configure the recognition request
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=48000,  # Adjust this based on your audio file
        language_code="en-US",  # Adjust language code as needed
        model = "video",
    )

    audio = speech.RecognitionAudio(content=content)

    # Perform the speech-to-text recognition
    response = client.recognize(config=config, audio=audio)

    # Process and store the transcribed text in a text file
    with open(output_text_file, 'w', encoding='utf-8') as output_file:
        for result in response.results:
            transcribed_text = result.alternatives[0].transcript
            output_file.write(transcribed_text + " ")

# Example usage
if __name__ == "__main__":
    audio_file_path = "test_sample.mp3"
    credentials_json_path = "myfirstproject-399807-502e6ada243d.json"
    output_text_file = "audio_to_text_sample.txt"

    transcribe_audio_and_save(audio_file_path, credentials_json_path, output_text_file)
    print("Transcribed text saved to:", output_text_file)


# #222222second method using uri of google
# from google.cloud import speech_v1p1beta1 as speech
# from google.protobuf import duration_pb2
# from pydub import AudioSegment

# def transcribe_audio_and_save(audio_file_path, credentials_json_path, output_text_file):
#     audio = AudioSegment.from_mp3(audio_file_path)
#     wav_file_path = audio_file_path.replace(".mp3", ".wav")
#     audio.export(wav_file_path, format="wav")

#     # Initialize the Google Speech-to-Text client with your service account credentials
#     client = speech.SpeechClient.from_service_account_json(credentials_json_path)

#     # Configure the recognition request
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=audio.frame_rate,
#         language_code="en-US",
#         enable_automatic_punctuation=True,  # Enable punctuation in transcription
#         model="video",
#     )

#     # Use a publicly accessible URL for your audio file
#     # Replace 'YOUR_AUDIO_URL' with the actual URL
#     audio_uri = "test_sample.mp3"

#     audio = speech.RecognitionAudio(uri=audio_uri)

#     # Perform the long-running speech-to-text recognition
#     operation = client.long_running_recognize(config=config, audio=audio)

#     print("Waiting for long-running operation to complete...")
#     response = operation.result(timeout=90)  # You can adjust the timeout as needed

#     # Process and store the transcribed text in a text file
#     with open(output_text_file, 'w', encoding='utf-8') as output_file:
#         for result in response.results:
#             transcribed_text = result.alternatives[0].transcript
#             output_file.write(transcribed_text + " ")

# # Example usage
# if __name__ == "__main__":
#     audio_file_path = "test_sample.mp3"
#     credentials_json_path = "myfirstproject-399807-502e6ada243d.json"
#     output_text_file = "audio_to_text_sample.txt"

#     transcribe_audio_and_save(audio_file_path, credentials_json_path, output_text_file)
#     print("Transcribed text saved to:", output_text_file)





# from google.cloud import speech_v1p1beta1 as speech
# from google.protobuf import duration_pb2

# def transcribe_audio_with_pause_detection(audio_file_path, credentials_json_path):
#     # Initialize the Google Cloud Speech-to-Text client with your service account credentials
#     client = speech.SpeechClient.from_service_account_json(credentials_json_path)

#     # Read the audio file
#     with open(audio_file_path, 'rb') as audio_file:
#         audio_data = audio_file.read()

#     # Configure the audio input
#     audio = speech.RecognitionAudio(content=audio_data)

#     # Configure the audio recognition request
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=48000,  # Adjust based on your audio file's sample rate
#         language_code='en-US',   # Change to the appropriate language code if needed
#         enable_word_time_offsets=True,
#         enable_music_detection=True,
#     )

#     # Perform the speech recognition
#     response = client.recognize(config=config, audio=audio)

#     transcribed_text = ""
#     pause_segments = []
#     music_segments = []

#     # Process the response
#     for result in response.results:
#         alternative = result.alternatives[0]
#         transcribed_text += alternative.transcript.strip() + ' '

#         # Detect pauses and music segments
#         for word_info in alternative.words:
#             if word_info.speaker_tag == 0:  # Speaker 0 usually represents silence
#                 pause_segments.append((word_info.start_time.seconds + word_info.start_time.nanos / 1e9,
#                                        word_info.end_time.seconds + word_info.end_time.nanos / 1e9))
#             elif word_info.music_info.instrumental:
#                 music_segments.append((word_info.start_time.seconds + word_info.start_time.nanos / 1e9,
#                                        word_info.end_time.seconds + word_info.end_time.nanos / 1e9))

#     return transcribed_text.strip(), pause_segments, music_segments

# if __name__ == "__main__":
#     audio_file_path = "test_sample.wav"  # Replace with the path to your audio file
#     credentials_json_path = "myfirstproject-399807-502e6ada243d.json"  # Replace with your JSON credentials file

#     transcribed_text, pause_segments, music_segments = transcribe_audio_with_pause_detection(audio_file_path, credentials_json_path)

#     print("Transcribed Text:")
#     print(transcribed_text)

#     print("\nPause Segments (start time, end time):")
#     for segment in pause_segments:
#         print(segment)

#     print("\nMusic Segments (start time, end time):")
#     for segment in music_segments:
#         print(segment)
