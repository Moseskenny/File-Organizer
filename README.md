# 📁 File Organizer (GUI Tool)

A simple Python tool that automatically organizes files in a selected folder into categorized subfolders such as Images, Videos, Audio, Documents, and Others.

This tool uses a graphical folder picker and organizes files instantly with a single click.

---

## ✨ Features

* 📂 Select any folder using GUI dialog
* 🗂 Automatically categorizes files into:

  * Images
  * Videos
  * Audio
  * Documents
  * Others
* ⚡ Fast and lightweight
* 🧠 Smart extension-based classification
* 🖥 No command-line knowledge required

---

## 📸 Example

Before:

```

Downloads/
file1.jpg
song.mp3
movie.mp4
notes.pdf

```

After running tool:

```

Downloads/
Images/file1.jpg
Audio/song.mp3
Videos/movie.mp4
Documents/notes.pdf

```

---

## 📂 Project Structure

```id="bcsux8"
File-Organizer/
│── organizer.py
│── README.md
│── requirements.txt
│── LICENSE
│── .gitignore
```

---

## ⚙️ Installation

### 1. Clone repository

```bash id="p7e7yh"
git clone https://github.com/Moseskenny/File-Organizer.git
cd File-Organizer
```

### 2. Install dependencies

```bash id="0dyf1o"
pip install -r requirements.txt
```

---

## 🚀 How to Use

Run the script:

```bash id="2h2sxt"
python organizer.py
```

Then:

1. Select the folder you want to organize
2. The tool will automatically create category folders
3. Files will be moved into their respective folders

---

## 🗂 Supported File Types

| Category  | Extensions                           |
| --------- | ------------------------------------ |
| Images    | .jpg, .jpeg, .png, .gif, .bmp, .tiff |
| Videos    | .mp4, .avi, .mov, .wmv, .mkv         |
| Audio     | .mp3, .wav, .aac, .ogg               |
| Documents | .txt, .pdf, .doc, .docx, .xls, .xlsx |
| Others    | Everything else                      |

---

## 🧰 Technologies Used

* Python
* Tkinter (GUI)
* os & shutil (file handling)

---

## 📜 License

MIT License

---

## 👤 Author

**Moses Kenny**
GitHub: https://github.com/Moseskenny

---

## ⭐ Support

If you like this project, please ⭐ the repository!
