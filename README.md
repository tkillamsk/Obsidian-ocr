# Description
Simple script to OCR text on pics and put it to .md file in Obsidian vault.
Supports russian hand written text
To split notes from each othe use "#" sign. This will create a Task from note and add /n.

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
Fill in "vault"(path to vault root) and "file_name"(ie "unsorted.md") vars.
If You don't want to be asked on file deletion comment do_delete().
# Run 

```
python ocr.py
```
check unsorted.md.
