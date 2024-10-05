from google.cloud import texttospeech

def generate_speech(input_text_file, output_audio_file, credentials_json_path):
    # Initialize the Google Text-to-Speech client with your service account credentials
    client = texttospeech.TextToSpeechClient.from_service_account_json(credentials_json_path)

    # Read the input text from the file
    with open(input_text_file, 'r', encoding='utf-8') as file:
        input_text = file.read()

    # Configure the synthesis input
    synthesis_input = texttospeech.SynthesisInput(text=input_text)

    # Configure the voice parameters for Hindi with a male voice
    voice = texttospeech.VoiceSelectionParams(
        language_code='hi-IN',  # Hindi language code
        name='hi-IN-Wavenet-C',  # Adjust voice name as needed (check available voices)
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE  # Ensure a male voice
    )

    # Configure the audio output
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    # Generate the speech and save it to an audio file
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open(output_audio_file, 'wb') as audio_file:
        audio_file.write(response.audio_content)

if __name__ == "__main__":
    input_text_file = "Hindi.txt"  # Replace with the path to your input text file
    output_audio_file = "test_to_audio.mp3"  # Replace with the desired output audio file path
    credentials_json_path = "myfirstproject-399807-6e9a9331769a.json"

    generate_speech(input_text_file, output_audio_file, credentials_json_path)
    print(f"Speech generated and saved to {output_audio_file}.")
