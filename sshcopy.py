import paramiko
import os

hostname = '192.168.1.82'
port = 22
username = 'Tristan'
password = 'Mouks'
remote_dir = "E:\TestProjet"
local_dir = "C:/path/to/local/dir"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, port=port, username=username, password=password)

sftp = ssh.open_sftp()

# List all files and directories in the remote directory
remote_files = sftp.listdir(remote_dir)

# Recursively copy files and directories from remote to local
for file_name in remote_files:
    remote_path = os.path.join(remote_dir, file_name)
    local_path = os.path.join(local_dir, file_name)
    if sftp.stat(remote_path).st_mode & 0o4000:  # Directory
        os.makedirs(local_path, exist_ok=True)
        sftp.getfo(remote_path + "/", os.path.join(local_path, ""))
    else:  # File
        sftp.get(remote_path, local_path)

sftp.close()
ssh.close()
