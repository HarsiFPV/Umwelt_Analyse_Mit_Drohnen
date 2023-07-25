import pymongo


def import_to_db_paths(txt_file, url, db, collection):

    client = pymongo.MongoClient(url)

    db = client[db]

    if collection not in db.list_collection_names():
        db.create_collection(collection)
    collection = db[collection]

    collection.delete_many({})

    with open(txt_file, "r") as file:
        contents = file.read()

    lines = contents.split("\n")

    for line in lines:
        document = {"data": line}
        collection.insert_one(document)


import_to_db_paths(r"C:\P6\Data\paths.txt", "mongodb://localhost:27017/", "P6", "file_path")
