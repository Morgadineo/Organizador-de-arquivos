# Imports
import shutil
import os
from pathlib import Path
from tkinter import *
from tkinter.filedialog import askdirectory


# Functions
def get_path():
    global path
    path = askdirectory()
    path = Path(path)
    text_label.configure(text=f'Path: {path}', fg='')
    return path


def organize():
    files = path.iterdir()
    for file in files:
        file_name, file_extension = os.path.splitext(file)
        if file_extension != '':
            if (path / Path(file_extension.upper())).exists():
                shutil.move(file, Path(path / file_extension.upper()))

            if not (path / Path(file_extension.upper())).exists():
                Path(path / file_extension.upper()).mkdir()
                shutil.move(file, Path(path / file_extension.upper()))
        elif file_extension == '':
            pass

# Window
root = Tk()
root.title('File organizer')
root.configure(bg='#515151')

# Items
text_label = Label(root, text='Click there to select the file -->', bg='#969696')

path_button = Button(root, text='There', command=get_path, width=20, bg='#969696')
organize_button = Button(root, text='Organizer', command=organize, bg='#969696')

# Grid
text_label.grid(row=0, column=0, padx=10, pady=10)

path_button.grid(row=0, column=1, padx=10, pady=10)
organize_button.grid(row=1, column=0, columnspan=2, padx=20)

# Mainloop
root.mainloop()
