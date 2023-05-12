import csv
import os
from importlib.metadata import files


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
