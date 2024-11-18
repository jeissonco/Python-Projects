"""
Jeisson Nino
15/06-2024
Practice sessions for python
"""

import os

def list_files(folder):
    try:
        content = os.listdir(folder)
        files = [f for f in content if os.path.isfile(os.path.join(folder, f))]
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"The directory {folder} does not exist.")
    except PermissionError:
        print(f"You don't have permission to access this folder: {folder}.")

# Calling the function with the path to search for, here you replace the path with the path to search for
list_files('/Users/jeissonnino/Python TAFE')
