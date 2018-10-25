import logging

from pynaoqi_mate import Robot
from configuration import PepperConfiguration

from .camera import Camera
from .calculation_api import calculate
from .school_boy import run_school_boy_dialog

# configure logging
logging.basicConfig(level=logging.INFO)

#: Holds the name of the Pepper
PEPPER_NAME = "Porter"


def main():
    config = PepperConfiguration(PEPPER_NAME)
    robot = Robot(config)

    run_school_boy_dialog(robot)

    camera = Camera(robot)

    camera.take_picture("/tmp/picture.jpg")
    result = calculate("/tmp/picture.jpg")

    if result["success"]:
        logging.info("Calculated result '%s'", result["result"])
        robot.ALAnimatedSpeech.say("I calculated {}".format(result["result"]))
    else:
        logging.info("Error '%s'", result["result"])
        robot.ALAnimatedSpeech.say("Error while calculating: {}".format(
            result["result"]))


if __name__ == "__main__":
    main()
