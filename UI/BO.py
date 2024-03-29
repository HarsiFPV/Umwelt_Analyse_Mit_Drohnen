import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import subprocess
import os
import customtkinter
from datetime import datetime

window = customtkinter.CTk()
startDate = tk.StringVar()
endDate = tk.StringVar()
show_debug_buttons = False

def init_gui():

    global entry_variable1, entry_variable2

    def set_variable1():
        startDate = tk.StringVar()
        startDate.set(entry_variable1.get())
        entry_variable1.delete(0, tk.END)
        entry_variable1.insert(0, startDate.get())
        output_text.insert(tk.END, "Start Date set : " + startDate.get() + "\n---------------\n")

    def set_variable2():
        endDate = tk.StringVar()
        endDate.set(entry_variable2.get())
        entry_variable2.delete(0, tk.END)
        entry_variable2.insert(0, endDate.get())
        output_text.insert(tk.END, "End Date set : " + endDate.get() + "\n---------------\n")

    def clear_console():
        output_text.delete("1.0", tk.END)

    def execute_command(command):
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output_text.insert(tk.END, "Cleared Folder\n---------------\n")

    def execute_command2(command2):
        result = subprocess.run(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output_text.insert(tk.END, "File Paths Extracted\n---------------\n")

    def execute_command3(command3):
        result = subprocess.run(command3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output_text.insert(tk.END, "Photos Metadatas Extracted\n---------------\n")

    def execute_command4(command4):
        result = subprocess.run(command4, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output_text.insert(tk.END, "File Paths Imported To DB\n---------------\n")

    def execute_command5(command5):
        result = subprocess.run(command5, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output_text.insert(tk.END, "File Metadatas Imported To DB\n---------------\n")

    def execute_command6(command6):
        result = subprocess.run(command6, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output_text.insert(tk.END, "Cleared DB\n---------------\n")

    def execute_command7(command7):
        result = subprocess.run(command7, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output_text.insert(tk.END, "Retrieved Photos From Drive\n---------------\n")

    def execute_command8(command8):
        folder_path = "E:\\Projet6\\Map"

        start_date = startDate.get()
        end_date = endDate.get()

        if not start_date and not end_date:
            start_date = "0001:01:01"
            end_date = "9999:12:31"

        start_date_str = str(start_date)
        end_date_str = str(end_date)

        command = ["python", "C:\\Users\\Tristan\\PycharmProjects\\pythonProject\\umweltanalysemktdrohnen\\Map\\map.py", folder_path, start_date_str, end_date_str]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        output_text.insert(tk.END, "Placed photos taken between " + start_date_str + " and " + end_date_str + " on the map\n---------------\n")

    def execute_command9(command9):
        result = subprocess.run(command9, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output_text.insert(tk.END, "Map Opened In Browser\n---------------\n")

    def execute_command_main(command_main):
        result = subprocess.run(command_main, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output_text.insert(tk.END, result.stdout)

    def switch_directory(directory):
        os.chdir(directory)
        output_text.insert(tk.END, "Switched to " + directory + "\n---------------\n")

    def toggle_debug_buttons():
        global show_debug_buttons
        show_debug_buttons = not show_debug_buttons
        if show_debug_buttons:
            show_buttons()
        else:
            hide_buttons()

    def show_buttons():
        button_switch_directory.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky=tk.SW)
        button_execute_command7.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky=tk.SW)
        button_execute_command.grid(row=4, column=0, padx=(10, 10), pady=(10, 10), sticky=tk.SW)
        button_execute_command2.grid(row=5, column=0, padx=(10, 10), pady=(10, 10), sticky=tk.SW)
        button_execute_command3.grid(row=6, column=0, padx=(10, 10), pady=(10, 10), sticky=tk.SW)
        button_execute_command4.grid(row=7, column=0, padx=(10, 10), pady=(10, 10), sticky=tk.SW)
        button_execute_command5.grid(row=8, column=0, padx=(10, 10), pady=(10, 10), sticky=tk.SW)
        button_execute_command8.grid(row=9, column=0, padx=(10, 10), pady=(10, 10), sticky=tk.SW)
        button_execute_command6.grid(row=11, column=0, padx=(10, 10), pady=(10, 10), sticky=tk.SW)

    def hide_buttons():
        button_execute_command7.grid_forget()
        button_execute_command8.grid_forget()
        button_switch_directory.grid_forget()
        button_execute_command.grid_forget()
        button_execute_command2.grid_forget()
        button_execute_command3.grid_forget()
        button_execute_command4.grid_forget()
        button_execute_command5.grid_forget()
        button_execute_command6.grid_forget()


    customtkinter.set_default_color_theme("green")

    window.title("Umweltanalyse Benutzeroberfläche")
    window.resizable(False, False)


    button_execute_command_main = customtkinter.CTkButton(window, text="RUN FULL SCRIPT",command=lambda: execute_command_main(["cmd.exe", "/c","py.exe C:\\Users\\Tristan\\PycharmProjects\\pythonProject\\umweltanalysemktdrohnen\\main.py"]))

    button_switch_directory = customtkinter.CTkButton(window, text="0. Switch to directory",command=lambda: switch_directory("C:\\Users\\Tristan\\PycharmProjects\\pythonProject\\umweltanalysemktdrohnen"))

    button_execute_command = customtkinter.CTkButton(window, text="2. Clean Folder", command=lambda: execute_command(["cmd.exe", "/c", "py.exe .\\Redundancy\\clean_folder.py"]))

    button_execute_command2 = customtkinter.CTkButton(window, text="3. Extract File Paths",command=lambda: execute_command2(["cmd.exe", "/c", "py.exe .\\paths\\extract_paths.py"]))

    button_execute_command3 = customtkinter.CTkButton(window, text="4. Extract Photos Metadatas",command=lambda: execute_command3(["cmd.exe", "/c", "py.exe .\\metadata\\extract_metadata.py"]))

    button_execute_command4 = customtkinter.CTkButton(window, text="5. Import File Paths To DB",command=lambda: execute_command4(["cmd.exe", "/c","py.exe .\\Database\\import_to_db_paths.py"]))

    button_execute_command5 = customtkinter.CTkButton(window, text="6. Import File Metadatas To DB",command=lambda: execute_command5(["cmd.exe", "/c","py.exe .\\Database\\import_to_db_metadata.py"]))

    button_execute_command6 = customtkinter.CTkButton(window, text="DEBUG : Clear DB", command=lambda: execute_command6(["cmd.exe", "/c", "py.exe .\\Database\\clearDB.py"]))

    button_execute_command7 = customtkinter.CTkButton(window, text="1. Retrieve Photos From Drive",command=lambda: execute_command7(["cmd.exe", "/c", "py.exe .\\Redundancy\\retrievePhotos.py"]))

    button_execute_command8 = customtkinter.CTkButton(window, text="7. Generate Map", command=lambda: execute_command8([]))

    button_execute_command9 = customtkinter.CTkButton(window, text="OPEN MAP", command=lambda: execute_command9(["cmd.exe", "/c", "E:\Projet6\Map\map.html"]))

    button_execute_command10 = customtkinter.CTkButton(window, text="Generate New Map Using Dates", command=lambda: execute_command8(["cmd.exe", "/c", "E:\Projet6\Map\map.html"]), font=("Arial", 15))


    button_execute_command_main.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky=tk.NW)
    button_execute_command9.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky=tk.NW)

    button_execute_command10.grid(row=17, column=0, pady=(15, 15), padx=(5, 15), sticky="NW")

    button_toggle_debug = customtkinter.CTkButton(window, text="Show Debug Functions", command=toggle_debug_buttons, font=("Arial", 15))
    button_toggle_debug.grid(row=0, column=1, padx=(10, 10), pady=(15, 15), sticky=tk.NE)

    button_clear_console = customtkinter.CTkButton(window, text="Clear Console", command=clear_console, font=("Arial", 15))
    button_clear_console.grid(row=1, column=1, padx=(10, 10), pady=(15, 15), sticky=tk.NE)

    label_variable1 = customtkinter.CTkLabel(window, text="Start Date format : yyyy:mm:dd", font=("Arial", 15),  fg_color=("grey25"), corner_radius=8)
    label_variable1.grid(row=13, column=0, pady=(5, 5), padx=(5, 5), sticky="NW")

    entry_variable1 = customtkinter.CTkEntry(window, textvariable=startDate, width=90, font=("Arial", 15))
    entry_variable1.grid(row=14, column=0, pady=(15, 5), padx=(5, 5), sticky="NW")

    button_set_variable1 = customtkinter.CTkButton(window, text="Set Start Date", command=set_variable1, font=("Arial", 15))
    button_set_variable1.grid(row=14, column=1, pady=(15, 5), padx=(5, 10), sticky="NE")

    label_variable2 = customtkinter.CTkLabel(window, text="End Date format: yyyy:mm:dd", font=("Arial", 15), fg_color=("grey25"), corner_radius=8)
    label_variable2.grid(row=15, column=0, pady=(5, 5), padx=(5, 5), sticky="NW")

    entry_variable2 = customtkinter.CTkEntry(window, textvariable=endDate, width=90, font=("Arial", 15))
    entry_variable2.grid(row=16, column=0, pady=(5, 5), padx=(5, 5), sticky="NW")

    button_set_variable2 = customtkinter.CTkButton(window, text="Set End Date", command=set_variable2, font=("Arial", 15))
    button_set_variable2.grid(row=16, column=1, pady=(5, 5), padx=(5, 10), sticky="NE")

    output_text = customtkinter.CTkTextbox(window, height=370, width=500, wrap=tk.WORD, font=("Arial", 15))
    output_text.grid(row=12, column=0, columnspan=2, sticky=tk.S)

    window.grid_columnconfigure(0, weight=1)

    window.mainloop()

if __name__ == "__main__":
    init_gui()
    global entry_variable1, entry_variable2