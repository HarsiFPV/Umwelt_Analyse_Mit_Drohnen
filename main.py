from Database import import_to_db_paths, import_to_db_metadata
from metadata import extract_image_metadata
from paths import extract_path
from Redundancy import clean_folder

def main():
    # Nettoyer le dossier
    clean_folder(r"E:\Projet6\Données")
    print("Folder has been cleaned")

    # Extraire les chemins
    extract_path(r"E:\Projet6\Photos", r"E:\Projet6\Données\paths.txt")
    print("Paths exported")

    # Extraire les métadonnées GPS des images
    extract_image_metadata(r"E:\Projet6\Photos", r"E:\Projet6\Données\metadata.txt")
    print("GPS Metadata exported")

    # Importer les chemins dans la base de données
    import_to_db_paths(r"E:\Projet6\Données\paths.txt", "mongodb://localhost:27017/", "P6", "file_path")
    print("Paths imported to DB")

    # Importer les métadonnées GPS dans la base de données
    import_to_db_metadata(r"E:\Projet6\Données\metadata.txt", "mongodb://localhost:27017/", "P6", "file_metadata")
    print("GPS Metadata imported to DB")

# Exécuter la fonction principale
if __name__ == "__main__":
    main()
