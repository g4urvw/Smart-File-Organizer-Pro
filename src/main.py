import tkinter as tk
from tkinter import filedialog, messagebox
from organizer import organize_files

def choose_folder():
    folder = filedialog.askdirectory()

    if folder:
        try:
            moved = organize_files(folder)
            messagebox.showinfo(
                "Success",
                f"Successfully organized {moved} files!"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Smart File Organizer Pro")
root.geometry("500x300")

title = tk.Label(
    root,
    text="📂 Smart File Organizer Pro",
    font=("Arial", 18, "bold")
)
title.pack(pady=30)

button = tk.Button(
    root,
    text="Select Folder",
    command=choose_folder,
    font=("Arial", 14),
    width=20,
    height=2
)
button.pack()

root.mainloop()
