import time
import math
import logging


def recovering_from_move(
        schoolboy, assumed_angle_to_formula, backup_distance=(-0.5, 0.0)):
    logging.error("Couldn't move to person, because of obsticles in my way ...")
    schoolboy.robot.ALAnimatedSpeech.say(
            "Oh Oh! I can't move to you. I think I'm stuck. "
            "But I'll attend class from here. No worries!"
    )

    # backup
    if not schoolboy.move(backup_distance[0], backup_distance[1]):
        schoolboy.fail(reason="I'm unable to recover from the failed move.")
        return

    schoolboy.robot.ALVisualCompass.moveTo(
            0, 0, theta=math.radians(assumed_angle_to_formula))

    # WUAAAT
    time.sleep(2)

    schoolboy.find_formula()
