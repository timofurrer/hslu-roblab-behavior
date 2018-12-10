import logging


def saying_solution(schoolboy, solution):
    schoolboy.robot.ALAnimatedSpeech("I have calculated: {}".format(solution))
    schoolboy.dance()
