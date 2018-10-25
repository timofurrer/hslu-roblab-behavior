import paramiko


def download_file_from_pepper(config, remote_path, local_path):
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
