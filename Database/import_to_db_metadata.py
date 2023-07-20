import pymongo

def import_to_db_metadata(txt_file, url, db, collection_name):
    # Connect to the MongoDB server
    client = pymongo.MongoClient(url)

    # Select the database
    db = client[db]

    collection = db[collection_name]

    with open(txt_file, 'r') as f:
        for line in f:
            # Extraction des informations de ligne
            file_info, gps_info = line.split("GPS Data: ")
            _, file_name = file_info.strip().split("File: ")
            gps_data = eval(gps_info.strip())

            # Accès aux données de latitude, longitude et altitude
            gps_info = gps_data["GPS"]
            latitude = gps_info["latitude"]
            longitude = gps_info["longitude"]
            altitude = gps_info["altitude"]

            # Recherche d'un document avec le même nom de fichier dans la collection
            existing_document = collection.find_one({"data.File": file_name})

            # Si un document avec le même nom de fichier existe, mise à jour des données GPS
            if existing_document:
                collection.update_one(
                    {"data.File": file_name},
                    {"$set": {
                        "data.GPS.latitude": latitude,
                        "data.GPS.longitude": longitude,
                        "data.GPS.altitude": altitude
                    }}
                )
            else:
                # Création du document à insérer dans la collection
                document = {
                    "data": {
                        "File": file_name,
                        "GPS": {
                            "latitude": latitude,
                            "longitude": longitude,
                            "altitude": altitude
                        }
                    }
                }
                # Insertion du document dans la collection MongoDB
                collection.insert_one(document)

import_to_db_metadata(r"E:\Projet6\Données\metadata.txt","mongodb://localhost:27017/","P6","file_metadata")