import io

from google.cloud import vision_v1p3beta1 as vision


def detect_faces(path):
    """Detects faces in an image."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    result = []
    for i, face in enumerate(faces):
        print("Face {} has pan angle of {}".format(i, face.pan_angle))
        result.append({
            "pan": face.pan_angle,
            "tilt": face.tilt_angle,
            "joy": face.joy_likelihood,
            "headwear": face.headwear_likelihood,
            "bounding_poly": [
                (v.x, v.y) for v in face.bounding_poly.vertices
            ]
        })
    return result
