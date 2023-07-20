import sys
import folium
import pymongo
import os
import re
import time
from datetime import datetime, timedelta

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from UI.BO import startDate, endDate

def format_date(date_str):
    # Split the date string and take the first part, then replace hyphens with colons
    date_parts = date_str.split()[0].split("-")
    return ":".join(date_parts)

def map(folder_path, start_date, end_date):

    files = os.listdir(folder_path)

    # Iterate through the list of files
    for file in files:
        # Use the os.remove() function to delete the file
        os.remove(os.path.join(folder_path, file))

    time.sleep(1)

    lat, lon = 47.57, 7.52
    carte = folium.Map(location=[lat, lon], zoom_start=10)

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["P6"]
    collection = db["file_metadata"]

    data = collection.find({})

    if start_date and end_date:

        # Convert the start_date_str and end_date_str to datetime objects
        start_date = datetime.strptime(start_date, "%Y:%m:%d")
        end_date = datetime.strptime(end_date, "%Y:%m:%d")

        # Set the time component to midnight (00:00:00)
        start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = end_date.replace(hour=0, minute=0, second=0, microsecond=0)
    else:
        # If startDate or endDate is empty, consider all dates
        start_date = datetime.min
        end_date = datetime.max

    for document in data:
        gps_data = document.get("data", {}).get("GPS", {})
        latitude = gps_data.get("latitude", 0)
        longitude = gps_data.get("longitude", 0)
        file_name = document.get("data", {}).get("File", "")
        date_taken_str = document.get("data", {}).get("DateTaken", "")

        # Vérification des coordonnées GPS non nulles
        if latitude != 0 and longitude != 0:
            photo_lat, photo_lon = float(latitude), float(longitude)

            # Check if the date_taken_str is not empty or None before splitting
            if date_taken_str and date_taken_str.strip():
                date_taken = datetime.strptime(date_taken_str.split()[0], "%Y:%m:%d")
                #print(start_date, date_taken, end_date)

                # Check if the photo's date is within the specified date range
                if start_date <= date_taken <= end_date:
                    folium.Marker([photo_lat, photo_lon], popup=file_name).add_to(carte)


    carte.save(f"E:\\Projet6\\Map\\map.html")

#map(f"E:\\Projet6\\Map", f"E:\\Projet6\\Données\\metadata.txt", "2023:07:19", "2023:07:19")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python map.py <folder_path> <start_date> <end_date>")
        sys.exit(1)

    folder_path = sys.argv[1]
    start_date_str = sys.argv[2]
    end_date_str = sys.argv[3]

    map(folder_path, start_date_str, end_date_str)