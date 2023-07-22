import os


def clean_folder(folder_path):
    files = os.listdir(folder_path)

    for file in files:
        os.remove(os.path.join(folder_path, file))

clean_folder(f"E:\\Projet6\\Données")
