import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import subprocess
import os

def clear_console():
    # Clear the console_text widget
    output_text.delete("1.0", tk.END)

def execute_command(command):
    # Exécute la commande en utilisant la fonction subprocess
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Affiche le résultat dans la zone de texte
    output_text.insert(tk.END, "Cleared Folder\n---------------\n")

def execute_command2(command2):
    # Exécute la commande en utilisant la fonction subprocess
    result = subprocess.run(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Affiche le résultat dans la zone de texte
    output_text.insert(tk.END, "File Paths Extracted\n---------------\n")

def execute_command3(command3):
    # Exécute la commande en utilisant la fonction subprocess
    result = subprocess.run(command3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Affiche le résultat dans la zone de texte
    output_text.insert(tk.END, "Photos Metadatas Extracted\n---------------\n")

def execute_command4(command4):
    # Exécute la commande en utilisant la fonction subprocess
    result = subprocess.run(command4, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Affiche le résultat dans la zone de texte
    output_text.insert(tk.END, "File Paths Imported To DB\n---------------\n")

def execute_command5(command5):
    # Exécute la commande en utilisant la fonction subprocess
    result = subprocess.run(command5, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Affiche le résultat dans la zone de texte
    output_text.insert(tk.END, "File Metadatas Imported To DB\n---------------\n")

def execute_command6(command6):
    # Exécute la commande en utilisant la fonction subprocess
    result = subprocess.run(command6, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Affiche le résultat dans la zone de texte
    output_text.insert(tk.END, "Cleared DB\n---------------\n")

def execute_command7(command7):
    # Exécute la commande en utilisant la fonction subprocess
    result = subprocess.run(command7, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Affiche le résultat dans la zone de texte
    output_text.insert(tk.END, "Retrieved Photos From Drive\n---------------\n")

def execute_command_main(command_main):
    # Exécute la commande en utilisant la fonction subprocess
    result = subprocess.run(command_main, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Affiche le résultat dans la zone de texte
    output_text.insert(tk.END, result.stdout)

def switch_directory(directory):
    # Change le répertoire de travail courant
    os.chdir(directory)
    output_text.insert(tk.END, "Switched to "+directory+"\n---------------\n")


# Crée une fenêtre principale
window = ThemedTk(theme="ubuntu")
window.title("Umweltanalyse Benutzeroberfläche")

# Create a frame for the buttons
button_frame = ttk.Frame(window)
button_frame.grid(row=0, column=0, sticky=tk.W)

button_execute_command_main = ttk.Button(button_frame, text="RUN FULL SCRIPT", command=lambda: execute_command_main(["cmd.exe", "/c", "py.exe C:\\Users\\Tristan\\PycharmProjects\\pythonProject\\umweltanalysemktdrohnen\\main.py"]))


# Crée un bouton pour changer de répertoire
button_switch_directory = ttk.Button(button_frame, text="0. Switch to directory", command=lambda: switch_directory("C:\\Users\\Tristan\\PycharmProjects\\pythonProject\\umweltanalysemktdrohnen"))


# Crée un bouton pour exécuter une commande
button_execute_command = ttk.Button(button_frame, text="2. Clean Folder", command=lambda: execute_command(["cmd.exe", "/c", "py.exe .\\Redundancy\\clean_folder.py"]))

button_execute_command2 = ttk.Button(button_frame, text="3. Extract File Paths", command=lambda: execute_command2(["cmd.exe", "/c", "py.exe .\\paths\\extract_paths.py"]))

button_execute_command3 = ttk.Button(button_frame, text="4. Extract Photos Metadatas", command=lambda: execute_command3(["cmd.exe", "/c", "py.exe .\\metadata\\extract_metadata.py"]))

button_execute_command4 = ttk.Button(button_frame, text="5. Import File Paths To DB", command=lambda: execute_command4(["cmd.exe", "/c", "py.exe .\\Database\\import_to_db_paths.py"]))

button_execute_command5 = ttk.Button(button_frame, text="6. Import File Metadatas To DB", command=lambda: execute_command5(["cmd.exe", "/c", "py.exe .\\Database\\import_to_db_metadata.py"]))

button_execute_command6 = ttk.Button(button_frame, text="DEBUG : Clear DB", command=lambda: execute_command6(["cmd.exe", "/c", "py.exe .\\Database\\clearDB.py"]))

button_execute_command7 = ttk.Button(button_frame, text="1. Retrieve Photos From Drive", command=lambda: execute_command7(["cmd.exe", "/c", "py.exe .\\Redundancy\\retrievePhotos.py"]))

# Position the other buttons using grid()
button_execute_command_main.grid(row=0, column=0, sticky=tk.NW)
button_switch_directory.grid(row=1, column=0, sticky=tk.NW)
button_execute_command.grid(row=3, column=0, sticky=tk.NW)
button_execute_command2.grid(row=4, column=0, sticky=tk.NW)
button_execute_command3.grid(row=5, column=0, sticky=tk.NW)
button_execute_command4.grid(row=6, column=0, sticky=tk.NW)
button_execute_command5.grid(row=7, column=0, sticky=tk.NW)
button_execute_command6.grid(row=8, column=0, sticky=tk.NW)
button_execute_command7.grid(row=2, column=0, sticky=tk.NW)

# Create a button to clear the console
button_clear_console = ttk.Button(window, text="Clear Console", command=clear_console)
button_clear_console.grid(row=0, column=1, sticky=tk.SE)

# Create a text widget to display the results
output_text = tk.Text(window, height=30, width=100)
output_text.grid(row=1, column=0, columnspan=2, sticky=tk.W)

# Create a text widget to display the console
console_text = tk.Text(window, height=10, width=100)
console_text.grid(row=2, column=0, columnspan=2, sticky=tk.W)

# Configure column 0 to expand horizontally
window.grid_columnconfigure(0, weight=1)

# Lance la boucle principale de l'interface utilisateur
window.mainloop()