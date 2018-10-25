import requests


SERVICE_URL = "http://localhost:5000"


def calculate(local_image_path):
    response = requests.post(
            SERVICE_URL + "/calculate",
            files={"file": open(local_image_path, "rb")}
    )
    return response.json()
