import time
import functools
import logging

VOCABULARY = [
    "this is correct",
    "this is wrong"
]
SOLUTION_CORRECT = None


def saying_solution(schoolboy, solution):
    schoolboy.robot.ALAnimatedSpeech.say("I have calculated: {}".format(solution))

    # initiale speech recognition
    recognizer = schoolboy.robot.ALSpeechRecognition
    recognizer.setLanguage("English")

    # setup subscriptions
    memory = schoolboy.robot.ALMemory
    speech_subscriber = memory.subscriber("WordRecognized")
    speech_subscriber.signal.connect(
            functools.partial(speech_detected, schoolboy, recognizer))
    recognizer.pause(True)
    recognizer.removeAllContext()
    recognizer.setVocabulary(VOCABULARY, False)
    recognizer.pause(False)
    recognizer.subscribe2("Teacher_Correct")

    while SOLUTION_CORRECT is None:
        time.sleep(0.5)

    if SOLUTION_CORRECT:
        schoolboy.dance()
    else:
        schoolboy.rest()


def speech_detected(schoolboy, recognizer, *args):
    global SOLUTION_CORRECT

    for recognized_voc, accuracy in args:
        logging.info(
                "Recognized '%s' with accuracy of %.4f",
                recognized_voc, accuracy)

        if recognized_voc == "this is correct" and accuracy > 0.4:
            SOLUTION_CORRECT = True

            schoolboy.robot.ALAnimatedSpeech.say(
                "Of course, sir! I've had math by Joseph!")

            try:
                recognizer.unsubscribe("Teacher_Correct")
            except Exception as e:
                logging.error("Could not unsubscribe because: '%s'", str(e))
            return

        if recognized_voc == "this is wrong" and accuracy > 0.4:
            SOLUTION_CORRECT = False

            schoolboy.robot.ALAnimatedSpeech.say(
                "Oh, damn it! I've studied soo hard ...")

            try:
                recognizer.unsubscribe("Teacher_Correct")
            except Exception as e:
                logging.error("Could not unsubscribe because: '%s'", str(e))
            return
