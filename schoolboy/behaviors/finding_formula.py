import re
import logging

from schoolboy.service import find_formula
from schoolboy.utils import rotate_head_until


def finding_formula(schoolboy):
    # move head to initial position
    schoolboy.robot.ALMotion.setAngles("HeadYaw", 0.0, 0.2)
    schoolboy.robot.ALMotion.setAngles("HeadPitch", 0.0, 0.2)

    def __find_formula():
        schoolboy.camera.take_picture("/tmp/picture_formula.jpg")
        calc_result = find_formula("/tmp/picture_formula.jpg")
        logging.info("Got formula result '%s'", str(calc_result))
        if calc_result["success"]:
            match = re.search(r"(\([0-9+/*()-]+\))", calc_result["result"])
            if match:
                formula = match.group(0)
                logging.info("Extracted formula: '%s'", formula)
                return formula
        return None

    # rotate head until formula is found
    formula = rotate_head_until(schoolboy.robot, predicate=__find_formula)
    if formula is not None:
        schoolboy.eval_formula(formula)
    else:
        schoolboy.fail(reason="Unable to find formula")
