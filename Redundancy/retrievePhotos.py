import os
import shutil

def copy_and_delete_files(source_dir, destination_dir):

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    files = os.listdir(source_dir)

    for file_name in files:
        source_file = os.path.join(source_dir, file_name)
        destination_file = os.path.join(destination_dir, file_name)
        shutil.copy(source_file, destination_file)
        os.remove(source_file)

copy_and_delete_files(f"E:\Drive\p6", f"E:\Projet6\Photos")