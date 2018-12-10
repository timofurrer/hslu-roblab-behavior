import requests


SERVICE_URL = "http://localhost:5000"


def find_formula(local_image_path):
    response = requests.post(
            SERVICE_URL + "/find-formula",
            files={"file": open(local_image_path, "rb")}
    )
    return response.json()


def find_faces(local_image_path):
    response = requests.post(
            SERVICE_URL + "/find-faces",
            files={"file": open(local_image_path, "rb")}
    )
    return response.json()["result"]
