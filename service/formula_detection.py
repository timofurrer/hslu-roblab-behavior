import io

from google.cloud import vision_v1p3beta1 as vision


def detect_formula(path):
    """Detects handwritten characters in a local image.

    Args:
    path: The path to the local file.
    """
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    # Language hint codes for handwritten OCR:
    # en-t-i0-handwrit, mul-Latn-t-i0-handwrit
    # Note: Use only one language hint code per request for handwritten OCR.
    image_context = vision.types.ImageContext(
        language_hints=['en-t-i0-handwrit'])

    response = client.document_text_detection(
            image=image,
            image_context=image_context)

    return response.full_text_annotation.text.strip()
