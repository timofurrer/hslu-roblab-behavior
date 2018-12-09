import re
import logging

from schoolboy.service import find_formula


def finding_formula(schoolboy):
    # move head to initial position
    start_pos_yaw = 0.0
    max_rot_yaw = 1.4
    yaw_move_interval = 0.2
    schoolboy.robot.ALMotion.setAngles("HeadYaw", start_pos_yaw, 0.3)
    schoolboy.robot.ALMotion.setAngles("HeadPitch", 0.0, 0.3)

    result = None
    while not result and start_pos_yaw <= max_rot_yaw:
        print("Searching for formula, moving head 10 degrees to the left from {} to {}".format(
            start_pos_yaw, start_pos_yaw + yaw_move_interval))
        start_pos_yaw += yaw_move_interval
        schoolboy.robot.ALMotion.setAngles("HeadYaw", start_pos_yaw, 0.3)

        schoolboy.camera.take_picture("/tmp/picture_{}.jpg".format(start_pos_yaw))
        calc_result = find_formula("/tmp/picture_{}.jpg".format(start_pos_yaw))
        print("Got result {}".format(calc_result))
        if calc_result["success"]:
            match = re.search(r"(\([0-9+/*()-]+\))", calc_result["formula"])
            if match:
                logging.info("Extracted formula: '%s'", match.group(0))
                result = eval(match.group(0))
            else:
                pass
                # print("Formula {} didn't match".format(calc_result["formula"]))

    if result is None:
        logging.info("EMERGENCY, couldn't find a formula. Dying")
        schoolboy.robot.ALAnimatedSpeech.say("EMERGENCY, couldn't find a formula. Dying")
        exit(1)

    logging.info("Calculated result '%s'", result)
    schoolboy.robot.ALAnimatedSpeech.say("I calculated {}".format(result))
