import sys
import logging

from transitions.extensions import GraphMachine as Machine

from schoolboy.camera import Camera

# Behaviors
from schoolboy.behaviors.talking_to_teacher import talking_to_teacher
from schoolboy.behaviors.finding_person import finding_person
from schoolboy.behaviors.moving_to_person import moving_to_person
from schoolboy.behaviors.finding_formula import finding_formula
from schoolboy.behaviors.evaluating_formula import evaluating_formula
from schoolboy.behaviors.raising_hand import raising_hand
from schoolboy.behaviors.saying_solution import saying_solution
from schoolboy.behaviors.dancing import dancing

# configure logging
logging.basicConfig(level=logging.INFO)


class SchoolBoy(object):
    STATES = [
        "start",
        "talking_to_teacher",
        "finding_person",
        "moving_to_person",
        "finding_formula",
        "evaluating_formula",
        "raising_hand",
        "saying_solution",
        "dancing",
        "error"
    ]

    def __init__(self, robot):
        self.robot = robot
        self.camera = None

        if robot is not None:
            self.camera = Camera(robot)

            # disable external collision protection
            # because the rows of tables are too narrow
            robot.ALMotion.setExternalCollisionProtectionEnabled("All", False)

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
                trigger="find_formula",
                source="moving_to_person",
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
                trigger="fail",
                source=self.STATES,
                dest="error",
                after=self.__on_error
        )

    def __on_error(self, event):
        logging.error("Got into Error state with event: '%s'", str(event))


if __name__ == "__main__":
    # Generate FSM graph
    boy = SchoolBoy(None)
    boy.state_machine.get_graph().draw(sys.argv[1], prog="dot")
