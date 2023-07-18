import os
from importlib.metadata import files

def extract_path(path, output_file):

    cwd = path
    files = [os.path.join(cwd, f) for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]

    with open(output_file, 'w') as f:
        for file_path in files:
            f.write(file_path)
            f.write('\n')

extract_path(f"E:\Projet6\Photos", f"E:\Projet6\Données\paths.txt")