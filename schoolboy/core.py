import sys
import logging

from transitions.extensions import GraphMachine as Machine

from schoolboy.camera import Camera

# Behaviors
from schoolboy.behaviors.talking_to_teacher import talking_to_teacher
from schoolboy.behaviors.finding_person import finding_person
from schoolboy.behaviors.moving_to_person import moving_to_person
from schoolboy.behaviors.recovering_from_move import recovering_from_move
from schoolboy.behaviors.finding_formula import finding_formula
from schoolboy.behaviors.evaluating_formula import evaluating_formula
from schoolboy.behaviors.raising_hand import raising_hand
from schoolboy.behaviors.saying_solution import saying_solution
from schoolboy.behaviors.dancing import dancing
from schoolboy.behaviors.resting import resting

# school room orientations
SCHOOL_ON_HIS_RIGHT = -1
SCHOOL_ON_HIS_LEFT = 1


class SchoolBoy(object):
    STATES = [
        "start",
        "talking_to_teacher",
        "finding_person",
        "moving_to_person",
        "recovering_from_move",
        "finding_formula",
        "evaluating_formula",
        "raising_hand",
        "saying_solution",
        "dancing",
        "resting",
        "error"
    ]

    def __init__(self, robot, room_orientation=SCHOOL_ON_HIS_RIGHT):
        self.robot = robot
        self.room_orientation = room_orientation
        self.camera = None

        if robot is not None:
            self.camera = Camera(robot)

            # disable external collision protection
            # because the rows of tables are too narrow
            robot.ALMotion.setExternalCollisionProtectionEnabled("All", True)
            robot.ALMotion.setTangentialSecurityDistance(0.05)
            robot.ALMotion.setOrthogonalSecurityDistance(0.05)

        self.state_machine = Machine(model=self, states=self.STATES, queued=True, initial="start")
        self.state_machine.add_transition(
                trigger="talk_to_teacher",
                source="start",
                dest="talking_to_teacher",
                after=lambda *args, **kwargs: talking_to_teacher(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="find_person",
                source="talking_to_teacher",
                dest="finding_person",
                after=lambda *args, **kwargs: finding_person(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="move_to_person",
                source="finding_person",
                dest="moving_to_person",
                after=lambda *args, **kwargs: moving_to_person(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="recover_from_move",
                source="moving_to_person",
                dest="recovering_from_move",
                after=lambda *args, **kwargs: recovering_from_move(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="find_formula",
                source=["moving_to_person", "recovering_from_move"],
                dest="finding_formula",
                after=lambda *args, **kwargs: finding_formula(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="eval_formula",
                source="finding_formula",
                dest="evaluating_formula",
                after=lambda *args, **kwargs: evaluating_formula(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="raise_hand",
                source="evaluating_formula",
                dest="raising_hand",
                after=lambda *args, **kwargs: raising_hand(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="say_solution",
                source="raising_hand",
                dest="saying_solution",
                after=lambda *args, **kwargs: saying_solution(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="dance",
                source="saying_solution",
                dest="dancing",
                after=lambda *args, **kwargs: dancing(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="rest",
                source=["saying_solution", "dancing"],
                dest="resting",
                after=lambda *args, **kwargs: resting(self, *args, **kwargs)
        )
        self.state_machine.add_transition(
                trigger="fail",
                source=self.STATES,
                dest="error",
                after=self.__on_error
        )

    def __on_error(self, reason):
        logging.error("Got into Error state becase: '%s'", reason)
        self.robot.ALAnimatedSpeech.say("Oh no! What a pitty!")
        self.robot.ALAnimatedSpeech.say("I'm in an uncomfortable situation and don't know what to do")
        self.robot.ALAnimatedSpeech.say("I think the reason is that {}".format(reason))

    def move(self, x, y):
        # return self.robot.ALNavigation.navigateTo(x, y)
        self.robot.ALMotion.moveTo(x, y, 0)
        return True


if __name__ == "__main__":
    # Generate FSM graph
    boy = SchoolBoy(None)
    boy.state_machine.get_graph().draw(sys.argv[1], prog="dot")
