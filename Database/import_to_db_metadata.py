import pymongo

def import_to_db_metadata(txt_file, url, db, collection_name):
    # Connect to the MongoDB server
    client = pymongo.MongoClient(url)

    # Select the database
    database = client[db]

    # Check if the collection exists
    if collection_name not in database.list_collection_names():
        # Create the collection if it doesn't exist
        collection = database[collection_name]
    else:
        # Collection already exists, use the existing collection
        collection = database[collection_name]

    with open(txt_file, 'r') as f:
        for line in f:
            # Check if the line starts with "Image Metadata: "
            if line.startswith("Image Metadata: "):
                # Extract the JSON part from the line
                json_data = line[len("Image Metadata: "):]

                # Convert the JSON string to a Python dictionary
                data = eval(json_data)

                # Extract the required fields
                file_name = data["File"]
                latitude = data["GPS"]["Latitude"]
                longitude = data["GPS"]["Longitude"]
                altitude = data["GPS"]["Altitude"]
                date = data["DateTaken"]

                # Recherche d'un document avec le même nom de fichier dans la collection
                existing_document = collection.find_one({"data.File": file_name})

                # Si un document avec le même nom de fichier n'existe pas, l'importer
                if not existing_document:
                    # Création du document à insérer dans la collection
                    document = {
                        "data": {
                            "File": file_name,
                            "GPS": {
                                "latitude": latitude,
                                "longitude": longitude,
                                "altitude": altitude
                            },
                            "DateTaken": date
                        }
                    }
                    # Insertion du document dans la collection MongoDB
                    collection.insert_one(document)


import_to_db_metadata(r"E:\Projet6\Données\metadata.txt", "mongodb://localhost:27017/", "P6", "file_metadata")
