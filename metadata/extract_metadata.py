import os
from GPSPhoto import gpsphoto
import exifread

def extract_image_metadata(image_folder_path, output_file):

    os.chdir(image_folder_path)
    image_list = os.listdir()
    image_list = [a for a in image_list if a.endswith('.JPG') | a.endswith('.jpg')]

    with open(output_file, 'w') as f:
        for image_file in image_list:
            image_path = os.path.join(image_folder_path, image_file)
            data = gpsphoto.getGPSData(image_path)

            # Transformation des données GPS
            new_data = {
                "GPS": {
                    "latitude": data.get("Latitude"),
                    "longitude": data.get("Longitude"),
                    "altitude": data.get("Altitude")
                }
            }

            # Écriture dans le fichier texte
            f.write(f"File: {image_file} GPS Data: {new_data}\n")

extract_image_metadata(f"E:\Projet6\Photos", f"E:\Projet6\Données\metadata.txt")
