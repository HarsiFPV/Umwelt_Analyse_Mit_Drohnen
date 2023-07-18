import pymongo

def clearDB(url, db, collection):
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

clearDB(r"mongodb://localhost:27017/","P6","file_metadata")
clearDB(r"mongodb://localhost:27017/","P6","file_path")