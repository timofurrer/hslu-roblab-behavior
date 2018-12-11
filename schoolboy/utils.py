import math
import time
import logging
import itertools

import paramiko


def download_file_from_pepper(config, remote_path, local_path):
    """Download a file via SFTP from the pepper to a local file system."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
            config.Ip,
            username=config.Username,
            password=config.Password
    )
    sftp = ssh.open_sftp()
    sftp.get(remote_path, local_path)
    sftp.remove(remote_path)
    sftp.close()
    ssh.close()


def upload_file_to_pepper(config, local_path, remote_path):
    """Upload a file to the pepper."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
            config.Ip,
            username=config.Username,
            password=config.Password
    )
    sftp = ssh.open_sftp()
    sftp.put(local_path, remote_path)
    sftp.close()
    ssh.close()


def rotate_head_until(robot, predicate):
    ANGLES = [15, -15, 30, -30, 45, -45, 60, -60, 75, -75, 90, -90]

    # move head pitch to middle position
    robot.ALMotion.setAngles("HeadPitch", 0, 1)
    robot.ALMotion.setAngles("HeadYaw", 0, 0.1)

    angles_cycle = itertools.cycle(ANGLES)
    while True:
        result = predicate()
        if result:
            return result

        angle = next(angles_cycle)
        logging.info("Rotating head angle to %f", angle)
        robot.ALMotion.setAngles("HeadYaw", math.radians(angle), 0.2)
        time.sleep(0.5)
