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
    
    # Create a new .txt file in the directory
    with open(file_path, 'w') as file:
        file.write('')  # Creates an empty file
    
    # Open the newly created file in the default text editor
    subprocess.run(['gedit', file_path])
else:
    print("File creation cancelled.")  # The user cancelled the operation.
