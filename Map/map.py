import folium
from folium import plugins
import pymongo
import os
import re
import time

def map(folder_path, data_path):
    files = os.listdir(folder_path)

    # Iterate through the list of files
    for file in files:
        # Use the os.remove() function to delete the file
        os.remove(os.path.join(folder_path, file))

    time.sleep(1)

    lat, lon = 47.57, 7.52
    carte = folium.Map(location=[lat, lon], zoom_start=10)

#    with open(data_path, "r") as file:
#        data = file.read()
#
#    # Expression régulière pour extraire les informations du texte
#    pattern = r"File: (.*?) GPS Data: {'GPS': {'latitude': (.*?), 'longitude': (.*?), 'altitude':"
#
#    # Recherche des correspondances dans le texte
#    matches = re.findall(pattern, data)
#
#    # Parcours des correspondances et ajout des marqueurs sur la carte
#    for match in matches:
#        file_name, latitude, longitude = match
#        photo_lat, photo_lon = float(latitude), float(longitude)
#        folium.Marker([photo_lat, photo_lon], popup=file_name).add_to(carte)

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["P6"]
    collection = db["file_metadata"]

    data = collection.find({})

    # Parcours des documents de la collection et ajout des marqueurs sur la carte
    for document in data:
        gps_data = document.get("data", {}).get("GPS", {})
        latitude = gps_data.get("latitude", 0)
        longitude = gps_data.get("longitude", 0)
        file_name = document.get("data", {}).get("File", "")

        # Vérification des coordonnées GPS non nulles
        if latitude != 0 and longitude != 0:
            photo_lat, photo_lon = float(latitude), float(longitude)
            folium.Marker([photo_lat, photo_lon], popup=file_name).add_to(carte)

    carte.save(f"E:\\Projet6\\Map\\map.html")

map(f"E:\\Projet6\\Map", f"E:\Projet6\Données\metadata.txt")