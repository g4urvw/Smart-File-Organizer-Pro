import shutil
from pathlib import Path

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Code": [".py", ".cpp", ".java", ".html", ".css", ".js"]
}

def organize_files(folder):
    folder = Path(folder)
    moved_files = 0

    for file in folder.iterdir():
        if file.is_file():
            destination = "Others"

            for category, extensions in FILE_TYPES.items():
                if file.suffix.lower() in extensions:
                    destination = category
                    break

            target = folder / destination
            target.mkdir(exist_ok=True)

            shutil.move(str(file), str(target / file.name))
            moved_files += 1

    return moved_files
    
