import os
import logging

from .utils import upload_file_to_pepper


LOCAL_DIALOG_TOPIC = os.path.join(
        os.path.dirname(__file__),
        "SchoolDialog_enu.top"
)
REMOTE_DIALOG_TOPIC = "/tmp/SchoolDialog_enu.top"

def run_school_boy_dialog(robot):
    logging.info("Uploading dialog to pepper ...")
    upload_file_to_pepper(robot.configuration, LOCAL_DIALOG_TOPIC, REMOTE_DIALOG_TOPIC)
    logging.info("Uploaded dialog from %s to pepper at %s",
            LOCAL_DIALOG_TOPIC, REMOTE_DIALOG_TOPIC)

    robot.ALAnimatedSpeech.say("Sorry, I am late")
    topic_name = robot.ALDialog.loadTopic(REMOTE_DIALOG_TOPIC)

    logging.info("Has confidence threshold of %s",
            robot.ALDialog.getASRConfidenceThreshold())
    robot.ALDialog.setASRConfidenceThreshold(0.75)
    logging.info("Set confidence threshold of %s",
            robot.ALDialog.getASRConfidenceThreshold())

    robot.ALDialog.activateTopic(topic_name)
    robot.ALDialog.subscribe2('schoolboy_dialog')

    try:
        raw_input("\nSpeak to the robot using rules from the just loaded .top file. Press Enter when finished:")
    finally:
        # stopping the dialog engine
        robot.ALDialog.unsubscribe('schoolboy_dialog')

        # Deactivating the topic
        robot.ALDialog.deactivateTopic(topic_name)

        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload our topic and free the associated memory
        robot.ALDialog.unloadTopic(topic_name)
