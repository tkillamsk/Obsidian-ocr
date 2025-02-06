# Description
Simple script to OCR text on pics and put it to .md file in Obsidian vault.
Supports russian hand written text.

After script processed all files it will ask to delete these files.

# Supported image formats:
- png
- jpg
- jpeg

# Installation
```
pip install -r requilements.txt
```

# Setup
Fill in ```vault```(path to vault root) where you will upload images and ```file_name```(ie ```unsorted.md```) to store scanned texts and source images.
If You don't want to be asked on file deletion comment ```do_delete()```.
To split notes from each othe use ```#``` sign. This will add ```/n``` and create a Task from note.

# Run 

```
python ocr.py
```
check  ```unsorted.md```.
