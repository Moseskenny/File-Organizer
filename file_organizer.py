import os
import shutil
import tkinter as tk
from tkinter import filedialog


file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.avi', '.mov', '.wmv', '.mkv'],
    'Audio': ['.mp3', '.wav', '.aac', '.ogg'],
    'Documents': ['.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx'],
    'Others': []  
}


root = tk.Tk()
root.withdraw()


mypath = filedialog.askdirectory(title="Select a Folder to Organize")


if mypath:
    
    for category in file_types.keys():
        category_path = os.path.join(mypath, category)
        os.makedirs(category_path, exist_ok=True)  

    
    for filename in os.listdir(mypath):
        full_path = os.path.join(mypath, filename)
        if os.path.isfile(full_path):
            ext = os.path.splitext(filename)[1].lower()
            categorized = False
            for category, extensions in file_types.items():
                if ext in extensions:
                    target_path = os.path.join(mypath, category, filename)
                    shutil.move(full_path, target_path)
                    categorized = True
                    break
            if not categorized:
                target_path = os.path.join(mypath, 'Others', filename)
                shutil.move(full_path, target_path)

    print("Files have been moved to their respective folders.")
else:
    print("No folder was selected.")
