import os


def get_files(path):
    cwd = path
    global files
    files = [os.path.join(cwd, f) for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
    print(files)
    return files
