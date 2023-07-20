import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import subprocess
import os
import customtkinter

def set_variable1():
    startDate.set(entry_variable1.get())
    output_text.insert(tk.END, "Start Date set : " + startDate.get() + "\n---------------\n")

def set_variable2():
    endDate.set(entry_variable2.get())
    output_text.insert(tk.END, "End Date set : " + endDate.get() + "\n---------------\n")

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

def execute_command8(command8):
    # Exécute la commande en utilisant la fonction subprocess
    result = subprocess.run(command8, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Affiche le résultat dans la zone de texte
    output_text.insert(tk.END, "Deleted Old Map || Created New Map\n---------------\n")

def execute_command9(command9):
    # Exécute la commande en utilisant la fonction subprocess
    result = subprocess.run(command9, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Affiche le résultat dans la zone de texte
    output_text.insert(tk.END, "Map Opened In Browser\n---------------\n")

def execute_command_main(command_main):
    # Exécute la commande en utilisant la fonction subprocess
    result = subprocess.run(command_main, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Affiche le résultat dans la zone de texte
    output_text.insert(tk.END, result.stdout)

def switch_directory(directory):
    # Change le répertoire de travail courant
    os.chdir(directory)
    output_text.insert(tk.END, "Switched to "+directory+"\n---------------\n")

customtkinter.set_default_color_theme("green")

# Crée une fenêtre principale
window = customtkinter.CTk()
window.title("Umweltanalyse Benutzeroberfläche")
window.resizable(False, False)

# Create a frame for the buttons
#window = customtkinter.CTkFrame(window)
#window.grid(row=0, column=0, sticky=tk.W)

button_execute_command_main = customtkinter.CTkButton(window, text="RUN FULL SCRIPT", command=lambda: execute_command_main(["cmd.exe", "/c", "py.exe C:\\Users\\Tristan\\PycharmProjects\\pythonProject\\umweltanalysemktdrohnen\\main.py"]))

startDate = tk.StringVar()
endDate = tk.StringVar()

# Crée un bouton pour changer de répertoire
button_switch_directory = customtkinter.CTkButton(window, text="0. Switch to directory", command=lambda: switch_directory("C:\\Users\\Tristan\\PycharmProjects\\pythonProject\\umweltanalysemktdrohnen"))


# Crée un bouton pour exécuter une commande
button_execute_command = customtkinter.CTkButton(window, text="2. Clean Folder", command=lambda: execute_command(["cmd.exe", "/c", "py.exe .\\Redundancy\\clean_folder.py"]))

button_execute_command2 = customtkinter.CTkButton(window, text="3. Extract File Paths", command=lambda: execute_command2(["cmd.exe", "/c", "py.exe .\\paths\\extract_paths.py"]))

button_execute_command3 = customtkinter.CTkButton(window, text="4. Extract Photos Metadatas", command=lambda: execute_command3(["cmd.exe", "/c", "py.exe .\\metadata\\extract_metadata.py"]))

button_execute_command4 = customtkinter.CTkButton(window, text="5. Import File Paths To DB", command=lambda: execute_command4(["cmd.exe", "/c", "py.exe .\\Database\\import_to_db_paths.py"]))

button_execute_command5 = customtkinter.CTkButton(window, text="6. Import File Metadatas To DB", command=lambda: execute_command5(["cmd.exe", "/c", "py.exe .\\Database\\import_to_db_metadata.py"]))

button_execute_command6 = customtkinter.CTkButton(window, text="DEBUG : Clear DB", command=lambda: execute_command6(["cmd.exe", "/c", "py.exe .\\Database\\clearDB.py"]))

button_execute_command7 = customtkinter.CTkButton(window, text="1. Retrieve Photos From Drive", command=lambda: execute_command7(["cmd.exe", "/c", "py.exe .\\Redundancy\\retrievePhotos.py"]))

button_execute_command8 = customtkinter.CTkButton(window, text="7. Generate Map", command=lambda: execute_command8(["cmd.exe", "/c", "py.exe .\\Map\\map.py"]))

button_execute_command9 = customtkinter.CTkButton(window, text="OPEN MAP", command=lambda: execute_command9(["cmd.exe", "/c", "E:\Projet6\Map\map.html"]))

# Position the other buttons using grid()
button_execute_command_main.grid(row=0, column=0, padx=(10,10), pady=(10,10), sticky=tk.NW)
button_switch_directory.grid(row=1, column=0, padx=(10,10), pady=(10,10), sticky=tk.NW)
button_execute_command7.grid(row=2, column=0, padx=(10,10), pady=(10,10), sticky=tk.NW)
button_execute_command.grid(row=3, column=0, padx=(10,10), pady=(10,10), sticky=tk.NW)
button_execute_command2.grid(row=4, column=0, padx=(10,10), pady=(10,10), sticky=tk.NW)
button_execute_command3.grid(row=5, column=0, padx=(10,10), pady=(10,10), sticky=tk.NW)
button_execute_command4.grid(row=6, column=0, padx=(10,10), pady=(10,10), sticky=tk.NW)
button_execute_command5.grid(row=7, column=0, padx=(10,10), pady=(10,10), sticky=tk.NW)
button_execute_command8.grid(row=8, column=0, padx=(10,10), pady=(10,10), sticky=tk.NW)
button_execute_command9.grid(row=9, column=0, padx=(10,10), pady=(10,10), sticky=tk.NW)
button_execute_command6.grid(row=10, column=0, padx=(10,10), pady=(10,10), sticky=tk.NW)


# Create a button to clear the console
button_clear_console = customtkinter.CTkButton(window, text="Clear Console", command=clear_console)
button_clear_console.grid(row=10, column=1, padx=(10,10), pady=(15,15), sticky=tk.NE)

# Créer un libellé pour le premier champ d'entrée
label_variable1 = customtkinter.CTkLabel(window, text="Start Date format : dd/mm/yyyy", font=("Arial", 15))
label_variable1.grid(row = 12, column=0, pady=(5,5), padx=(5,5), sticky="NW")

# Créer un champ d'entrée pour la première variable
entry_variable1 = customtkinter.CTkEntry(window, textvariable=startDate, width=90, font=("Arial", 15))
entry_variable1.grid(row = 13, column=0, pady=(5,5), padx=(5,5), sticky="NW")

# Créer un bouton pour définir la première variable
button_set_variable1 = customtkinter.CTkButton(window, text="Définir Variable 1", command=set_variable1)
button_set_variable1.grid(row = 13, column=1, pady=(5,5), padx=(5,5), sticky="NW")

# Créer un libellé pour le deuxième champ d'entrée
label_variable2 = customtkinter.CTkLabel(window, text="End Date format: dd/mm/yyyy", font=("Arial", 15))
label_variable2.grid(row = 14, column=0, pady=(5,5), padx=(5,5), sticky="NW")

# Créer un champ d'entrée pour la deuxième variable
entry_variable2 = customtkinter.CTkEntry(window, textvariable=endDate, width=90, font=("Arial", 15))
entry_variable2.grid(row = 15, column=0, pady=(5,5), padx=(5,5), sticky="NW")

# Créer un bouton pour définir la deuxième variable
button_set_variable2 = customtkinter.CTkButton(window, text="Définir Variable 2", command=set_variable2)
button_set_variable2.grid(row = 15, column=1, pady=(5,5), padx=(5,5), sticky="NW")


# Create a text widget to display the results
output_text = customtkinter.CTkTextbox(window, height=300, width=500, wrap=tk.WORD, font=("Arial", 15))
output_text.grid(row=11, column=0, columnspan=2, sticky=tk.S)

# Create a text widget to display the console
#console_text = customtkinter.CTkTextbox(window, height=100, width=100, wrap=tk.WORD, font=("Arial", 11))
#console_text.grid(row=2, column=0, columnspan=2, sticky=tk.W)

# Configure column 0 to expand horizontally
window.grid_columnconfigure(0, weight=1)

# Lance la boucle principale de l'interface utilisateur
window.mainloop()