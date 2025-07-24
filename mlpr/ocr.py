from google.cloud import vision
import io

def extract_text_google(image_bytes):
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=image_bytes)
    response = client.document_text_detection(image=image)

    texts = response.text_annotations
    return texts[0].description if texts else ""
