import os


def clean_folder(folder_path):
    files = os.listdir(folder_path)

    # Iterate through the list of files
    for file in files:
        # Use the os.remove() function to delete the file
        os.remove(os.path.join(folder_path, file))

    print('All files have been deleted from the folder.')
