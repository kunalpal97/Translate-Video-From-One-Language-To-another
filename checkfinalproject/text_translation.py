from google.cloud import translate_v2 as translate

def translate_to_indian_languages(input_file, credentials_json_path):
    # Initialize the Google Cloud Translation client with your service account credentials
    client = translate.Client.from_service_account_json(credentials_json_path)

    # Read the input text file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Define the target Indian languages and their language codes
    target_languages = {

        "Hindi": "hi",
        # "Marathi": "mr",
        # "Bengali": "bn",
        # "Gujarati": "gu",
        # "Tamil": "ta",
        # "Telugu": "te"
    }
    # Translate the text to each target Indian language and save to separate files
    for language, language_code in target_languages.items():
        translation = client.translate(text, target_language="hi")

        # Create a separate output file for each translation
        output_file = f"{language}_translation.txt"
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(translation['translatedText'])

# Example usage
if __name__ == "__main__":
    input_file = "audio_to_text_sample.txt"  # Replace with the path to your input text file
    credentials_json_path = "myfirstproject-399807-b982439feb10.json"

    translate_to_indian_languages(input_file, credentials_json_path)

    print("Translations saved to separate files.")

    
# from google.cloud import translate_v2 as translate

# def translate_to_indian_languages(input_file, credentials_json_path):
#     # Initialize the Google Cloud Translation client with your service account credentials
#     client = translate.Client.from_service_account_json(credentials_json_path)

#     # Read the input text from the file
#     with open(input_file, 'r', encoding='utf-8') as file:
#         input_text = file.read()

#     # Define the target Indian languages and their language codes
#     target_languages = {
#         "Hindi": "hi",
#         # "Marathi": "mr",
#         # "Bengali": "bn",
#         # "Gujarati": "gu",
#         # "Tamil": "ta",
#         # "Telugu": "te"
        
#     }

#     # Translate the input text into each target Indian language
#     translations = {}
#     for language, language_code in target_languages.items():
#         translation = client.translate(input_text, target_language=language_code)
#         translations[language] = translation['translatedText']

#     return translations

# if __name__ == "__main__":
#     input_file = "audio_to_text_sample.txt"  # Replace with the path to your input text file
#     credentials_json_path = "myfirstproject-399807-b982439feb10.json"

#     translations = translate_to_indian_languages(input_file, credentials_json_path)

#     # Save translations to separate files
#     for language, translation in translations.items():
#         output_file = f"{language}.txt"
#         with open(output_file, 'w', encoding='utf-8') as output:
#             output.write(translation)

#     print("Translations saved to separate files.")
