import pymongo

url = "mongodb://localhost:27017"

def test_connection(client):
    try:
        # Test connection
        client.admin.command('ismaster')
        print("Connexion réussie")
    except pymongo.errors.ConnectionFailure:
        print("La connexion a échoué")

def delete_non_matching_paths(client, path_prefix):
    # Connect to the MongoDB server
    client = pymongo.MongoClient(url)

    # Select the database
    db = client.paths
    collection = db.file_path

    # Delete all objects that do not match the path prefix
    query = {"data": {"$not": {"$regex": "^{}.*".format(path_prefix)}}}
    collection.delete_many(query)

# Test connection
client = pymongo.MongoClient(url)
test_connection(client)

delete_non_matching_paths(client, r"E:\\Projet6\\DJI")
