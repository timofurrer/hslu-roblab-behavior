# -*- coding: utf-8 -*-

import logging

from pynaoqi_mate import Robot
from configuration import PepperConfiguration

from schoolboy.core import SchoolBoy, SCHOOL_ON_HIS_RIGHT
from schoolboy.behaviors.finding_formula import finding_formula

# configure logging
logging.basicConfig(level=logging.INFO)

#: Holds the name of the Pepper
PEPPER_NAME = "Amber"


def main():
    config = PepperConfiguration(PEPPER_NAME)
    robot = Robot(config)

    schoolboy = SchoolBoy(robot, room_orientation=SCHOOL_ON_HIS_RIGHT)
    schoolboy.talk_to_teacher()


if __name__ == "__main__":
    main()
