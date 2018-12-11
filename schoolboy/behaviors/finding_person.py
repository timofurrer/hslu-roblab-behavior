import math
import time
import logging

from schoolboy.service import find_faces


def calc_distances(moved_distance, first_angle, second_angle):
    """Calculate the distances in X and Y for two given angles and
       a distance in X between those two angles.

    """
    beta1 = 180 - second_angle
    alpha1 = 180 - first_angle - beta1

    alpha = 180 - first_angle - 90

    b = moved_distance * math.sin(beta1 * math.pi / 180)/math.sin(alpha1 * math.pi / 180)
    logging.debug("beta1:" + str(beta1) + " alpha1:" + str(alpha1) + " b %.2f" % b)

    a = b * math.sin(alpha * math.pi / 180) / math.sin(90 * math.pi / 180)
    a2 = a - moved_distance
    c = b * math.sin(first_angle * math.pi/180) / math.sin(90 * math.pi/180)
    logging.debug("c: " + str(c) + " a2 %.2f" % a2)

    return a2, c


def analyze_faces(camera):
    st = time.time()
    camera.take_picture("/tmp/picture_faces.jpg", resolution=3)
    faces = find_faces("/tmp/picture_faces.jpg")
    logging.debug("Took {} seconds".format(time.time() - st))
    logging.debug("Faces data: %s", str(faces))
    return faces


def finding_person(schoolboy, criteria=lambda x: x["joy"] >= 2):
    def get_head_angle():
        return math.degrees(
                schoolboy.robot.ALMotion.getAngles("HeadYaw", False)[0])

    def set_head_angle(angle):
        schoolboy.robot.ALMotion.setAngles("HeadYaw", math.radians(angle), 0.1)
        schoolboy.robot.ALMotion.setAngles("HeadPitch", 0, 1)

    # rotate into room
    schoolboy.robot.ALVisualCompass.moveTo(
            0, 0, theta=math.radians(-90 * schoolboy.room_orientation))

    # move head to initial position
    schoolboy.robot.ALMotion.setAngles("HeadYaw", 0.8 * schoolboy.room_orientation, 0.3)
    schoolboy.robot.ALMotion.setAngles("HeadPitch", 0.0, 0.3)

    # take first picture
    matching_face = None
    while matching_face is None:
        faces = analyze_faces(schoolboy.camera)
        matching_face = next((x for x in faces if criteria(x)), None)
        if matching_face is None:
            schoolboy.robot.ALTextToSpeech.say("Extra head rotation, because I like it! Fock yeah!")
            set_head_angle(get_head_angle() + (10.0 if get_head_angle() > 0 else -10.0))
    first_angle = matching_face["pan"]

    # move a little bit forward
    moved_distance = 1.2
    sonar_back_start = schoolboy.robot.ALMemory.getData(
            "Device/SubDeviceList/Platform/Back/Sonar/Sensor/Value")
    schoolboy.robot.ALMotion.moveTo(moved_distance, 0, 0)
    sonar_back_end = schoolboy.robot.ALMemory.getData(
            "Device/SubDeviceList/Platform/Back/Sonar/Sensor/Value")

    actual_moved_distance = sonar_back_end - sonar_back_start
    logging.info("Planned to move %.4fm but sonar says %.4fm",
                 moved_distance, actual_moved_distance)
    head_angle = get_head_angle()
    set_head_angle(head_angle + (10.0 if head_angle > 0 else -10.0))

    # take second picture
    matching_face = None
    while matching_face is None:
        faces = analyze_faces(schoolboy.camera)
        matching_face = next((x for x in faces if criteria(x)), None)
        if matching_face is None:
            schoolboy.robot.ALTextToSpeech.say("Extra head rotation, because I like it! Fock yeah!")
            set_head_angle(get_head_angle() + (10.0 if get_head_angle() > 0 else -10.0))
    second_angle = matching_face["pan"]

    logging.info("Given angles: first=%f second=%f", first_angle, second_angle)
    remaining_forward_distance, remaining_side_distance = calc_distances(
            actual_moved_distance, first_angle, second_angle)
    logging.info("Got remaining distances: forward=%f side=%f", remaining_forward_distance, remaining_side_distance)

    # adding half a meter to the remaining forward distance, so it finds the entrance
    # remaining_forward_distance += remaining_forward_distance * (1 / 7)
    # subtracting a meter to the remaining side distance, so it doesn't collide with student
    remaining_forward_distance -= 0.75
    remaining_side_distance -= 2
    # remaining_side_distance = 2

    schoolboy.move_to_person(remaining_forward_distance, remaining_side_distance)
