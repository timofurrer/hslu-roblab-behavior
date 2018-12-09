import re
import math
import time
import logging
import random

import requests
import numpy as np

from naoqi import ALProxy


def finding_person(schoolboy):
    pass

# configure logging
logging.basicConfig(level=logging.INFO)

#: Holds the name of the Pepper
PEPPER_NAME = "Porter"
SERVICE_URL = "http://localhost:5000"


SCHOOL_ON_HIS_RIGHT = -1
SCHOOL_ON_HIS_LEFT = 1

SCHOOL_ORIENTATION = SCHOOL_ON_HIS_RIGHT


def see_faces(local_image_path):
    response = requests.post(
            SERVICE_URL + "/faces",
            files={"file": open(local_image_path, "rb")}
    )
    return response.json()["result"]


def rotate(robot, grad):
    robot.ALVisualCompass.moveTo(0, 0, theta=grad * (math.pi / 180))


def calc_poly_area(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def calc_distances(moved_distance, first_angle, second_angle):
    beta1 = 180 - second_angle
    alpha1 = 180 - first_angle - beta1

    alpha = 180 - first_angle - 90

    b = moved_distance * math.sin(beta1 * math.pi / 180)/math.sin(alpha1 * math.pi / 180)
    print("beta1:" + str(beta1) + " alpha1:" + str(alpha1) + " b %.2f" % b)

    a = b * math.sin(alpha * math.pi / 180) / math.sin(90 * math.pi / 180)
    a2 = a - moved_distance
    c = b * math.sin(first_angle * math.pi/180) / math.sin(90 * math.pi/180)
    print("c: " + str(c) + " a2 %.2f" % a2)

    return a2, c


def analyze_faces(camera):
    st = time.time()
    camera.take_picture("/tmp/picture_faces.jpg", resolution=3)
    faces = see_faces("/tmp/picture_faces.jpg")
    print("Took {} seconds".format(time.time() - st))
    print(faces)
    return faces


def move_to_person(robot, camera, criteria=lambda x: x["joy"] >= 2):
    def get_head_angle():
        return robot.ALMotion.getAngles("HeadYaw", False)[0] * (180 / math.pi)

    def set_head_angle(angle):
        robot.ALMotion.setAngles("HeadYaw", angle * (math.pi / 180), 0.1)
        robot.ALMotion.setAngles("HeadPitch", 0, 1)

    # move head to initial position
    robot.ALMotion.setAngles("HeadYaw", 0.8 * SCHOOL_ORIENTATION, 0.3)
    robot.ALMotion.setAngles("HeadPitch", 0.0, 0.3)

    # take first picture
    matching_face = None
    while matching_face is None:
        faces = analyze_faces(camera)
        matching_face = next((x for x in faces if criteria(x)), None)
        if matching_face is None:
            robot.ALTextToSpeech.say("Extra head rotation, because I like it! Fock yeah!")
            set_head_angle(get_head_angle() + (10.0 if get_head_angle() > 0 else -10.0))
    first_angle = matching_face["pan"]

    # move a little bit forward
    moved_distance = 1
    robot.ALMotion.moveTo(moved_distance, 0, 0)
    head_angle = get_head_angle()
    set_head_angle(head_angle + (10.0 if head_angle > 0 else -10.0))

    # take second picture
    matching_face = None
    while matching_face is None:
        faces = analyze_faces(camera)
        matching_face = next((x for x in faces if criteria(x)), None)
        if matching_face is None:
            robot.ALTextToSpeech.say("Extra head rotation, because I like it! Fock yeah!")
            set_head_angle(get_head_angle() + (10.0 if get_head_angle() > 0 else -10.0))
    second_angle = matching_face["pan"]

    print("Given angles:", first_angle, second_angle)
    remaining_forward_distance, remaining_side_distance = calc_distances(
            moved_distance, first_angle, second_angle)
    print("Got remaining distances:", remaining_forward_distance, remaining_side_distance)

    # adding half a meter to the remaining forward distance, so it finds the entrance
    remaining_forward_distance += remaining_forward_distance  * 1 / 4

    # subtracting a meter to the remaining side distance, so it doesn't collide with student
    remaining_side_distance -= 1.2

    robot.ALMotion.setAngles("HeadYaw", 0.0, 0.7)
    robot.ALMotion.setAngles("HeadPitch", 0.0, 0.7)
    print("Moving forward", remaining_forward_distance)
    robot.ALMotion.moveTo(remaining_forward_distance, 0, 0)
    rotate(robot, 90 * SCHOOL_ORIENTATION)
    robot.ALMotion.setAngles("HeadYaw", 0.0, 0.7)
    robot.ALMotion.setAngles("HeadPitch", 0.0, 0.7)
    robot.ALTextToSpeech.say("Oh hey! There you are!")
    print("Moving into bank", remaining_side_distance)
    robot.ALMotion.moveTo(remaining_side_distance, 0, 0)
    rotate(robot, 90 * SCHOOL_ORIENTATION)
    time.sleep(5)

def main():
    config = PepperConfiguration(PEPPER_NAME)
    robot = Robot(config)
    camera = Camera(robot)

    robot.ALMotion.setExternalCollisionProtectionEnabled("All", False)

    move_to_person(robot, camera, criteria=lambda x: x["tilt"] <= -2)
