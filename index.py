import subprocess
import os
from tkinter import Tk, simpledialog

# Function to ask for the file name
def ask_file_name():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_name = simpledialog.askstring("File Name", "Enter the name for the file:")
    root.destroy()
    return file_name

# Specify the directory path
directory_path = 'Documents/Assistants Material/Computer Basics/Articles (v2)'

# Ask the user for the file name
file_name = ask_file_name()
if file_name:  # Check if the user entered a name
    # Add .txt suffix if not present
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    file_path = os.path.join(directory_path, file_name)

    # Extract base file name without extension
    base_file_name = os.path.splitext(file_name)[0]
    
    # Check if the file exists, create it and write the base file name if it doesn't
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(base_file_name + "\n")  # Write the base file name at the beginning
    
    # Open the file in the default text editor
    subprocess.run(['gedit', file_path])
else:
    print("File creation cancelled.")  # The user cancelled the operation.
