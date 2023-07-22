import pymongo

def clearDB(url, db, collection):

    client = pymongo.MongoClient(url)

    db = client[db]

    if collection not in db.list_collection_names():
        db.create_collection(collection)
    collection = db[collection]

    collection.delete_many({})
    print(f"Cleared the collection.")

clearDB(r"mongodb://localhost:27017/","P6","file_metadata")
clearDB(r"mongodb://localhost:27017/","P6","file_path")