import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.avi', '.mov', '.wmv', '.mkv'],
    'Audio': ['.mp3', '.wav', '.aac', '.ogg'],
    'Documents': ['.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx'],
    'Others': []
}

def organize_folder(folder_path):
    try:
        # Create category folders
        for category in FILE_TYPES.keys():
            os.makedirs(os.path.join(folder_path, category), exist_ok=True)

        # Organize files
        for filename in os.listdir(folder_path):
            full_path = os.path.join(folder_path, filename)

            if os.path.isfile(full_path):
                ext = os.path.splitext(filename)[1].lower()
                moved = False

                for category, extensions in FILE_TYPES.items():
                    if ext in extensions:
                        move_file(full_path, os.path.join(folder_path, category, filename))
                        moved = True
                        break

                if not moved:
                    move_file(full_path, os.path.join(folder_path, 'Others', filename))

        messagebox.showinfo("Success", "Files organized successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")


def move_file(src, dest):
    # Handle duplicate filenames
    base, ext = os.path.splitext(dest)
    counter = 1

    while os.path.exists(dest):
        dest = f"{base}_{counter}{ext}"
        counter += 1

    shutil.move(src, dest)


def select_folder_and_organize():
    root = tk.Tk()
    root.withdraw()

    folder = filedialog.askdirectory(title="Select Folder to Organize")
    if folder:
        organize_folder(folder)
    else:
        messagebox.showwarning("Cancelled", "No folder selected.")


if __name__ == "__main__":
    select_folder_and_organize()
