import os


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

