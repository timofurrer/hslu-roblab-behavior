import logging


def resting(schoolboy):
    say = "I'm so tired, I'm going to rest"
    logging.info(say)
    schoolboy.robot.ALAnimatedSpeech.say(say)
    schoolboy.robot.ALMotion.rest()
