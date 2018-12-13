import math
import time
import logging


def moving_to_person(schoolboy, forward_distance, side_distance):
    logging.info("Moving forward: %.4f and to the side: %.4f", forward_distance, side_distance)
    logging.info("Moving forward: %.4f", forward_distance)
    schoolboy.robot.ALMotion.setAngles("HeadYaw", 0.0, 0.7)
    schoolboy.robot.ALMotion.setAngles("HeadPitch", 0.0, 0.7)
    if not schoolboy.move(forward_distance, 0):
        schoolboy.recover_from_move(assumed_angle_to_formula=180)
        return

    schoolboy.robot.ALVisualCompass.moveTo(
            0, 0, theta=math.radians(90 * schoolboy.room_orientation))

    sonar_front = float("-inf")
    while sonar_front <= 1.2:
        sonar_front = schoolboy.robot.ALMemory.getData(
                "Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value")
        logging.info("Got sonar value of: %f", sonar_front)
        if sonar_front > 1.2:
            break

        schoolboy.move(
                0, -0.15 * schoolboy.room_orientation, 0)

    schoolboy.robot.ALTextToSpeech.say("Oh hey! There you are!")
    schoolboy.robot.ALMotion.setAngles("HeadYaw", 0.0, 0.7)
    schoolboy.robot.ALMotion.setAngles("HeadPitch", 0.0, 0.7)
    logging.info("Moving into bank: %.4f", side_distance)

    # do not move side distance, but actually navigate with the front sonar
    sonar_front = float("inf")
    while sonar_front >= 0.5:
        sonar_front = schoolboy.robot.ALMemory.getData(
                "Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value")
        logging.info("Got sonar value of: %f", sonar_front)
        if sonar_front < 0.5:
            break

        schoolboy.move(0.15, 0)

    # schoolboy.move(side_distance, 0, 0)
    schoolboy.robot.ALVisualCompass.moveTo(
            0, 0, theta=math.radians(90 * schoolboy.room_orientation))

    # WUAAAT
    time.sleep(2)

    schoolboy.find_formula()
