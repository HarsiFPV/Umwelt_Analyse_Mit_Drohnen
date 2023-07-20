import os
from GPSPhoto import gpsphoto
import exifread

def extract_image_metadata(image_folder_path, output_file):
    os.chdir(image_folder_path)
    image_list = os.listdir()
    image_list = [a for a in image_list if a.lower().endswith(('.jpg', '.jpeg'))]

    with open(output_file, 'w') as f:
        for image_file in image_list:
            image_path = os.path.join(image_folder_path, image_file)
            data = gpsphoto.getGPSData(image_path)
            tags = exifread.process_file(open(image_path, 'rb'))

            # Extract date information from EXIF data
            date_taken = None
            if 'EXIF DateTimeOriginal' in tags:
                date_taken = tags['EXIF DateTimeOriginal']

            # Transformation des données GPS et date
            new_data = {
                "File": image_file,
                "GPS": {
                    "Latitude": data.get("Latitude"),
                    "Longitude": data.get("Longitude"),
                    "Altitude": data.get("Altitude")
                },
                "DateTaken": str(date_taken)
            }

            # Écriture dans le fichier texte
            f.write(f"Image Metadata: {new_data}\n")

extract_image_metadata(r"E:\Projet6\Photos", r"E:\Projet6\Données\metadata.txt")
