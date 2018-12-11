import logging


from naoqi import ALProxy

def raising_hand(schoolboy, solution):
    # Choregraphe bezier export in Python.
    names = []
    times = []
    keys = []

    names.append("HeadPitch")
    times.append([0, 2.24])
    keys.append([[-0.37378, [3, -0.0133333, 0], [3, 0.746667, 0]], [-0.37378, [3, -0.746667, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0, 2.24])
    keys.append([[0.0111198, [3, -0.0133333, 0], [3, 0.746667, 0]], [0.0111198, [3, -0.746667, 0], [3, 0, 0]]])

    names.append("HipPitch")
    times.append([0, 2.24])
    keys.append([[-0.0357752, [3, -0.0133333, 0], [3, 0.746667, 0]], [-0.0357752, [3, -0.746667, 0], [3, 0, 0]]])

    names.append("HipRoll")
    times.append([0, 2.24])
    keys.append([[-0.00549066, [3, -0.0133333, 0], [3, 0.746667, 0]], [-0.00549066, [3, -0.746667, 0], [3, 0, 0]]])

    names.append("KneePitch")
    times.append([0, 2.24])
    keys.append([[-0.0074207, [3, -0.0133333, 0], [3, 0.746667, 0]], [-0.0074207, [3, -0.746667, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0, 2.24])
    keys.append([[-0.110891, [3, -0.0133333, 0], [3, 0.746667, 0]], [-0.110891, [3, -0.746667, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0, 2.24])
    keys.append([[-1.71736, [3, -0.0133333, 0], [3, 0.746667, 0]], [-1.71736, [3, -0.746667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0, 2.24])
    keys.append([[0.626022, [3, -0.0133333, 0], [3, 0.746667, 0]], [0.626022, [3, -0.746667, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0, 2.24])
    keys.append([[1.77271, [3, -0.0133333, 0], [3, 0.746667, 0]], [1.77271, [3, -0.746667, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0, 2.24])
    keys.append([[0.103867, [3, -0.0133333, 0], [3, 0.746667, 0]], [0.114239, [3, -0.746667, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0, 2.24])
    keys.append([[0.0425655, [3, -0.0133333, 0], [3, 0.746667, 0]], [0.0425655, [3, -0.746667, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0, 1.16, 2.24])
    keys.append(
        [[0.102232, [3, -0.0133333, 0], [3, 0.386667, 0]], [0.242601, [3, -0.386667, -0.140369], [3, 0.36, 0.130688]],
         [0.95644, [3, -0.36, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0, 2.24])
    keys.append([[1.69033, [3, -0.0133333, 0], [3, 0.746667, 0]], [0.509636, [3, -0.746667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0, 2.24])
    keys.append([[0.688049, [3, -0.0133333, 0], [3, 0.746667, 0]], [0.688049, [3, -0.746667, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0, 1.16, 2.24])
    keys.append([[1.75191, [3, -0.0133333, 0], [3, 0.386667, 0]], [2.08567, [3, -0.386667, 0], [3, 0.36, 0]],
                 [-0.92677, [3, -0.36, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0, 1.16, 2.24])
    keys.append([[-0.0973568, [3, -0.0133333, 0], [3, 0.386667, 0]], [-1.30376, [3, -0.386667, 0], [3, 0.36, 0]],
                 [-0.671952, [3, -0.36, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0, 2.24])
    keys.append([[-0.0258008, [3, -0.0133333, 0], [3, 0.746667, 0]], [-0.0258008, [3, -0.746667, 0], [3, 0, 0]]])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        # motion = ALProxy("ALMotion", IP, 9559)
        motion = ALProxy("ALMotion")
        motion.angleInterpolationBezier(names, times, keys)
    except Exception as exc:
        fail_reason = "Oh, I can't raise my hand! Because: {}".format(exc)
        logging.error(fail_reason)
        schoolboy.fail(reason=fail_reason)
    else:
        schoolboy.say_solution(solution)
