import pymongo

def import_to_db_metadata(txt_file, url, db, collection_name):

    client = pymongo.MongoClient(url)

    database = client[db]

    # Check if the collection exists
    if collection_name not in database.list_collection_names():
        collection = database[collection_name]
    else:
        collection = database[collection_name]

    with open(txt_file, 'r') as f:
        for line in f:
            if line.startswith("Image Metadata: "):
                json_data = line[len("Image Metadata: "):]

                # Convert the JSON string to a Python dictionary
                data = eval(json_data)

                # Extract the required fields
                file_name = data["File"]
                latitude = data["GPS"]["Latitude"]
                longitude = data["GPS"]["Longitude"]
                altitude = data["GPS"]["Altitude"]
                date = data["DateTaken"]

                existing_document = collection.find_one({"data.File": file_name})

                if not existing_document:
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
                    collection.insert_one(document)


import_to_db_metadata(r"E:\Projet6\Données\metadata.txt", "mongodb://localhost:27017/", "P6", "file_metadata")
