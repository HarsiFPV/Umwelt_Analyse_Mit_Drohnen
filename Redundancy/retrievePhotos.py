import os
import shutil

def copy_and_delete_files(source_dir, destination_dir):
    # Vérifier si le dossier de destination existe, sinon le créer
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Obtenir la liste des fichiers dans le dossier source
    files = os.listdir(source_dir)

    # Parcourir tous les fichiers du dossier source
    for file_name in files:
        # Chemin complet du fichier source
        source_file = os.path.join(source_dir, file_name)

        # Chemin complet du fichier destination
        destination_file = os.path.join(destination_dir, file_name)

        # Copier le fichier source vers le dossier de destination
        shutil.copy(source_file, destination_file)

        # Supprimer le fichier source
        os.remove(source_file)

    #print("Copie et suppression terminées avec succès!")

# Exemple d'utilisation
source_folder = "/chemin/vers/dossier/source"
destination_folder = "/chemin/vers/dossier/destination"

copy_and_delete_files(f"E:\Drive\p6", f"E:\Projet6\Photos")