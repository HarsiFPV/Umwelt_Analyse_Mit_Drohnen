import pymongo


def import_to_db(txt_file, url, db, collection):
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

import_to_db(r"C:\Users\Tristan\Documents\Project\datei_path.csv", "mongodb://localhost:27017/", "paths", "file_path")
