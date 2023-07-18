import tkinter as tk
import subprocess
import os

def execute_command(command):
    # Exécute la commande en utilisant la fonction subprocess
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Affiche le résultat dans la zone de texte
    output_text.insert(tk.END, result.stdout)

def execute_command2(command):
    # Exécute la commande en utilisant la fonction subprocess
    result = subprocess.run(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Affiche le résultat dans la zone de texte
    output_text.insert(tk.END, result.stdout)

def execute_command_main(command_main):
    # Exécute la commande en utilisant la fonction subprocess
    result = subprocess.run(command_main, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Affiche le résultat dans la zone de texte
    output_text.insert(tk.END, result.stdout)

def switch_directory(directory):
    # Change le répertoire de travail courant
    os.chdir(directory)
    print("Switched to ", directory)

# Crée une fenêtre principale
window = tk.Tk()
window.title("Interface utilisateur")

# Crée un cadre pour les boutons
button_frame = tk.Frame(window)
button_frame.pack()

button_execute_command_main = tk.Button(button_frame, text="RUN FULL SCRIPT", command=lambda: execute_command_main(["cmd.exe", "/c", "py.exe C:\\Users\\Tristan\\PycharmProjects\\pythonProject\\umweltanalysemktdrohnen\\main.py"]))
button_execute_command_main.pack()

# Crée un bouton pour changer de répertoire
button_switch_directory = tk.Button(button_frame, text="0. Switch to directory", command=lambda: switch_directory("C:\\Users\\Tristan\\PycharmProjects\\pythonProject\\umweltanalysemktdrohnen"))
button_switch_directory.pack()

# Crée un bouton pour exécuter une commande
button_execute_command = tk.Button(button_frame, text="1. Clean Folder", command=lambda: execute_command(["cmd.exe", "/c", "py.exe .\\Redundancy\\clean_folder.py"]))
button_execute_command.pack()

button_execute_command2 = tk.Button(button_frame, text="2. Extract File Paths", command=lambda: execute_command2(["cmd.exe", "/c", "py.exe .\\paths\\extract_paths"]))
button_execute_command2.pack()

# Crée une zone de texte pour afficher les résultats
output_text = tk.Text(window, height=50, width=100)
output_text.pack()

# Lance la boucle principale de l'interface utilisateur
window.mainloop()