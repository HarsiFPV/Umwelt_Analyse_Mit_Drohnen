from paths import extract_paths
from Redundancy import clean_folder, retrievePhotos
import time

def main():

    print("|--STARTING--|")

    # Nettoyer le dossier
    clean_folder.clean_folder(r"E:\Projet6\Données")
    print("Folder has been cleaned\n------------------------------")

    time.sleep(0.5)

    retrievePhotos.copy_and_delete_files(f"E:\Drive\p6", f"E:\Projet6\Photos")
    print("New photos have been retrieved\n------------------------------")

    time.sleep(1)

    # Extraire les chemins
    extract_paths.extract_path(f"E:\\Projet6\\Photos", f"E:\\Projet6\\Données\\paths.txt")
    print("Paths exported\n------------------------------")

    from metadata import extract_metadata

    # Extraire les métadonnées GPS des images
    extract_metadata.extract_image_metadata(r"E:\Projet6\Photos", r"E:\Projet6\Données\metadata.txt")
    print("GPS Metadata exported\n------------------------------")

    time.sleep(1)

    from Database import import_to_db_paths, import_to_db_metadata
    # Importer les chemins dans la base de données
    import_to_db_paths.import_to_db_paths(r"E:\Projet6\Données\paths.txt", "mongodb://localhost:27017/", "P6", "file_path")
    print("Paths imported to DB\n------------------------------")

    # Importer les métadonnées GPS dans la base de données
    import_to_db_metadata.import_to_db_metadata(r"E:\Projet6\Données\metadata.txt", "mongodb://localhost:27017/", "P6", "file_metadata")
    print("GPS Metadata imported to DB\n------------------------------")

    time.sleep(1)
    print("|--DONE--|")

# Exécuter la fonction principale
if __name__ == "__main__":
    main()
