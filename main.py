import os
from os.path import isfile, join
import csv
import requests
import pandas as pd
import json
from PIL import Image, ExifTags, TiffTags
import pymongo
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


def clean_folder(folder_path):
    files = os.listdir(folder_path)

    # Iterate through the list of files
    for file in files:
        # Use the os.remove() function to delete the file
        os.remove(os.path.join(folder_path, file))

    print('All files have been deleted from the folder.')


def get_files(path):
    cwd = path
    global files
    files = [os.path.join(cwd, f) for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
    print(files)
    return files


def write_to_csv(file_path, file_name, data):
    path = os.path.join(file_path, file_name)

    with open(os.path.join(file_path, 'datei_path.csv'), 'w') as csvfile:
        # Use a dictionary writer to write the header row with the column name "Datei_path"
        csvwriter = csv.DictWriter(csvfile, fieldnames=["Datei_path"])
        csvwriter.writeheader()
        # Write the list of files to the CSV file, starting from the second file in the list
        for file in files[1:]:
            csvwriter.writerow({"Datei_path": file})

    return files


def extract_image_metadata(image_folder_path, metadata_file_path):
    # Create a new file to store the metadata in
    metadata_file = open(metadata_file_path, "w")

    # Loop through all the files in the image folder
    for file_name in os.listdir(image_folder_path):
        # Get the full path of the file
        file_path = os.path.join(image_folder_path, file_name)

        # Open the image file using the Pillow library
        img = Image.open(file_path)

        # Extract the metadata from the image
        metadata = img.getexif()

        print(metadata)

        # Write the metadata to the file as key-value pairs
        for tag, value in metadata.items():
            metadata_file.write(f"{file_name} - {tag}: {value}\n")

        metadata_file.write("\r")

    # Close the file when we're done
    metadata_file.close()


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


def import_csv_to_db(csv_file, url, db, collection):
    # Connect to the MongoDB server
    client = pymongo.MongoClient(url)

    # Select the database and collection where you want to import the data
    db = client[db]
    collection = db[collection]

    # Open the CSV file
    with open(csv_file, "r") as file:
        # Use the csv module to parse the file
        reader = csv.DictReader(file)

        # Iterate over the rows in the CSV and insert each row as a document in the collection
        for row in reader:
            collection.insert_one(row)

def delete_non_matching_paths(client, path_prefix):
    db = client.paths
    collection = db.file_path

    # Find all objects that match the path prefix
    matching_objects = collection.find({"data": {"$regex": "^{}.*".format(path_prefix)}})

    # Delete all objects that do not match the path prefix
    collection.delete_many({"data": {"$not": {"$regex": "^{}.*".format(path_prefix)}}})

<<<<<<< HEAD
clean_folder(r"C:\Users\user\Documents\Python")

get_files(r"C:\Users\Tristan\Pictures\Project")

write_to_csv(r"C:\Users\Tristan\Documents\Project", 'datei_path.csv', [files])

extract_image_metadata(r"C:\Photos ice nath\Relevé 2",
                       r"C:\Users\Tristan\Documents\Project\metadata.txt")

import_to_db(r"C:\Users\Tristan\Documents\Project\metadata.txt", "mongodb://localhost:27017/", "paths", "metadata_path")
import_to_db(r"C:\Users\Tristan\Documents\Project\datei_path.csv", "mongodb://localhost:27017/", "paths", "file_path")
=======

#clean_folder(r"C:\Users\Tristan\Documents\Project")
#
#get_files(r"D:\DCIM\100MEDIA")
#
#write_to_csv(r"C:\Users\Tristan\Documents\Project", 'datei_path.csv', [files])
#
#extract_image_metadata(r"D:\DCIM\100MEDIA",
#    r"C:\Users\Tristan\Documents\Project\metadata.txt")
#
#import_to_db(r"C:\Users\Tristan\Documents\Project\metadata.txt", "mongodb://localhost:27017/", "paths", "metadata_path")
#import_to_db(r"C:\Users\Tristan\Documents\Project\datei_path.csv", "mongodb://localhost:27017/", "paths", "file_path")

#delete_non_matching_paths("mongodb://localhost:27017/","D:\DCIM\100MEDIA*")
>>>>>>> 942b8409cffc26b871b4d39c46a5ff0766a59c62
