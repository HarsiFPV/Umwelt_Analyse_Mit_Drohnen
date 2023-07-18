import pymongo


def import_to_db_paths(txt_file, url, db, collection):
    # Connect to the MongoDB server
    client = pymongo.MongoClient(url)

    # Select the database
    db = client[db]

    # Check if the collection exists, create it if it doesn't
    if collection not in db.list_collection_names():
        db.create_collection(collection)
    collection = db[collection]

    # Clear the collection
    collection.delete_many({})
    print(f"Cleared the collection.")

    # Open the text file
    with open(txt_file, "r") as file:
        # Read the contents of the file
        contents = file.read()

    # Split the contents of the file into a list of lines
    lines = contents.split("\n")

    # Iterate over the list of lines and insert each line as a document in the collection
    for line in lines:
        document = {"data": line}
        collection.insert_one(document)

import_to_db_paths(r"E:\Projet6\Données\paths.txt", "mongodb://localhost:27017/", "P6", "file_path")

def import_to_db_metadata(txt_file, url, db, collection):
    # Connect to the MongoDB server
    client = pymongo.MongoClient(url)

    # Select the database
    db = client[db]

    # Check if the collection exists, create it if it doesn't
    if collection not in db.list_collection_names():
        db.create_collection(collection)
    collection = db[collection]

    # Clear the collection
    collection.delete_many({})
    print(f"Cleared the collection.")

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
