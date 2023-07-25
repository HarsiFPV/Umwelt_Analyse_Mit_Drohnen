from paths import extract_paths
from Redundancy import clean_folder, retrievePhotos
import time
import subprocess

start_date = "0001:01:01"
end_date = "9999:12:31"
folder_path = r"E:\Projet6\Map"


def execute_shell_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")


def main():

    print("|--STARTING--|")

    clean_folder.clean_folder(r"C:\P6\Data")
    print("Folder has been cleaned\n------------------------------")

    time.sleep(0.5)

    retrievePhotos.copy_and_delete_files(r"G:\Mon Drive\p6", r"C:\P6\Photos")
    print("New photos have been retrieved\n------------------------------")

    time.sleep(1)

    extract_paths.extract_path(r"C:\P6\Photos", r"C:\P6\Data\paths.txt")
    print("Paths exported\n------------------------------")

    from metadata import extract_metadata

    extract_metadata.extract_image_metadata(r"C:\P6\Photos", r"C:\P6\Data\metadata.txt")
    print("GPS Metadata exported\n------------------------------")

    time.sleep(1)

    from Database import import_to_db_paths, import_to_db_metadata

    import_to_db_paths.import_to_db_paths(r"C:\P6\Data\paths.txt", "mongodb://localhost:27017/", "P6", "file_path")
    print("Paths imported to DB\n------------------------------")

    import_to_db_metadata.import_to_db_metadata(r"C:\P6\Data\metadata.txt", "mongodb://localhost:27017/", "P6", "file_metadata")
    print("GPS Metadata imported to DB\n------------------------------")

    time.sleep(1)

    from Map import map

    folder_path = r"C:\P6\Map"

    command = [
        "python",
        r"C:\Users\Tristan\PycharmProjects\P6\umweltanalysemktdrohnen\Map\map.py",
        folder_path, start_date, end_date
    ]

    execute_shell_command(" ".join(command))

    print("Old Map deleted\n------------------------------")
    print("New map generated\n------------------------------")

    print("|--DONE--|")


if __name__ == "__main__":
    main()
