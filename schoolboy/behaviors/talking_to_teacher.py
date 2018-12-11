import time
import logging
import functools

LATE_SENTENCE = "You are late"
PERSON_CRITERIA = {
    "happiest": lambda x: x["joy"] >= 2,
    "sleepiest": lambda x: x["tilt"] <= -2
}

VOCABULARY = [
    LATE_SENTENCE,
]
VOCABULARY.extend(PERSON_CRITERIA.keys())

IS_SPEAKING = False
RECO_STATE = 0
GO_TO_PERSON = None


def talking_to_teacher(schoolboy):
    schoolboy.robot.ALMotion.setAngles("HeadYaw", 0.0, 0.3)
    schoolboy.robot.ALMotion.setAngles("HeadPitch", 0.0, 0.3)

    logging.info("Talking to teacher ...")

    # initiale speech recognition
    recognizer = schoolboy.robot.ALSpeechRecognition
    recognizer.setLanguage("English")

    schoolboy.robot.ALAnimatedSpeech.say("Hello everyone!")

    # setup subscriptions
    memory = schoolboy.robot.ALMemory
    speech_subscriber = memory.subscriber("WordRecognized")
    speech_subscriber.signal.connect(
            functools.partial(speech_detected, schoolboy, recognizer))
    recognizer.pause(True)
    recognizer.removeAllContext()
    recognizer.setVocabulary(VOCABULARY, False)
    recognizer.pause(False)
    recognizer.subscribe2("Teacher")

    while GO_TO_PERSON is None:
        time.sleep(0.5)

    schoolboy.find_person(criteria=GO_TO_PERSON)


def speech_detected(schoolboy, recognizer, *args):
    global IS_SPEAKING

    if IS_SPEAKING:
        return

    global RECO_STATE
    global GO_TO_PERSON

    for recognized_voc, accuracy in args:
        logging.info("Recognized '%s' with accuracy of %.4f",  recognized_voc, accuracy)

        if RECO_STATE == 0 and recognized_voc == LATE_SENTENCE and accuracy > 0.4:
            IS_SPEAKING = True
            schoolboy.robot.ALAnimatedSpeech.say("I'm so sorry. My Tesla wasn't charged so I had to take the bus")
            IS_SPEAKING = False
            RECO_STATE = 1
            return

        if RECO_STATE == 1 and recognized_voc in PERSON_CRITERIA and accuracy > 0.30:
            IS_SPEAKING = True
            schoolboy.robot.ALAnimatedSpeech.say("Alrighty! I'm going to the {} student".format(
                recognized_voc))
            IS_SPEAKING = False

            RECO_STATE = 2
            GO_TO_PERSON = PERSON_CRITERIA[GO_TO_PERSON]
            try:
                recognizer.unsubscribe("Teacher")
            except Exception as e:
                logging.error("Could not unsubscribe because: '%s'", str(e))
                return
            return
