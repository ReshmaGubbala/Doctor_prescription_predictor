from google.cloud import translate_v2 as translate

def translate_text_google(text, target_lang='en'):
    client = translate.Client()
    result = client.translate(text, target_language=target_lang)
    return result['translatedText']
