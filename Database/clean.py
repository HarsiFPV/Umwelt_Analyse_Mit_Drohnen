def delete_non_matching_paths(client, path_prefix):
    db = client.paths
    collection = db.file_path

    # Find all objects that match the path prefix
    matching_objects = collection.find({"data": {"$regex": "^{}.*".format(path_prefix)}})

    # Delete all objects that do not match the path prefix
    collection.delete_many({"data": {"$not": {"$regex": "^{}.*".format(path_prefix)}}})
