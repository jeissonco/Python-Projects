import tkinter as tk
from tkinter import filedialog

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window.
    file_path = filedialog.askopenfilename()  # Open the file dialog.
    if file_path:
        print(f"File selected: {file_path}")
    else:
        print("No file selected.")
    root.destroy()  # Close the tkinter window.

select_file()