import math
import time
import logging


def moving_to_person(schoolboy, forward_distance, side_distance):
    logging.info("Moving forward", forward_distance)
    schoolboy.robot.ALMotion.setAngles("HeadYaw", 0.0, 0.7)
    schoolboy.robot.ALMotion.setAngles("HeadPitch", 0.0, 0.7)
    schoolboy.robot.ALMotion.moveTo(forward_distance, 0, 0)
    schoolboy.robot.ALVisualCompass.moveTo(
            0, 0, theta=math.radians(90 * schoolboy.room_orientation))

    schoolboy.robot.ALTextToSpeech.say("Oh hey! There you are!")
    schoolboy.robot.ALMotion.setAngles("HeadYaw", 0.0, 0.7)
    schoolboy.robot.ALMotion.setAngles("HeadPitch", 0.0, 0.7)
    logging.info("Moving into bank", side_distance)
    schoolboy.robot.ALMotion.moveTo(side_distance, 0, 0)
    schoolboy.robot.ALVisualCompass.moveTo(
            0, 0, theta=math.radians(90 * schoolboy.room_orientation))

    # WUAAAT
    time.sleep(5)

    schoolboy.find_formula()
