from google.cloud import storage, speech, translate_v2 as translate

# Set up your Google Cloud credentials
# You can obtain the JSON credentials file from your Google Cloud project
# and set the GOOGLE_APPLICATION_CREDENTIALS environment variable to its path.

# Initialize Google Cloud clients
storage_client = storage.Client()
speech_client = speech.SpeechClient()
translate_client = translate.Client()

# Define the input video file and output text file
input_video_uri = "C:\Desktop 1\SIH\checkfinalproject\video1.mp4"  # Replace with your video's URL
output_text_file = "output.txt"

# Extract audio from the video and save it to a file
def extract_audio_from_video(video_uri):
    audio_config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",  # Change to the video's language
    )

    audio_source = speech.RecognitionAudio(uri=video_uri)

    response = speech_client.recognize(config=audio_config, audio=audio_source)

    with open(output_text_file, "w") as text_file:
        for result in response.results:
            text_file.write(result.alternatives[0].transcript + "\n")

# Translate the extracted text to another language
def translate_text(input_text, target_language):
    translation = translate_client.translate(input_text, target_language=target_language)
    return translation["translatedText"]

# Main function
def main():
    extract_audio_from_video(input_video_uri)

    with open(output_text_file, "r") as text_file:
        text_to_translate = text_file.read()

    target_languages = ["hi", "gu", "mr", "ta", "te", "kn", "ml"]  # Add more languages as needed

    for language in target_languages:
        translated_text = translate_text(text_to_translate, language)
        print(f"Translated text in {language}: {translated_text}")

if __name__ == "__main__":
    main()
