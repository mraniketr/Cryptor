from tkinter import *
from tkinter import filedialog
import os
from files.dataencryption.lsbcipher import *

def selection():
    root = Tk()

    #image selection
    root.filename =filedialog.askopenfilename()
    new_file = os.path.join(os.getcwd(), "final.jpg")
    os.rename(root.filename,new_file)

    #data selection
    root.filename =filedialog.askopenfilename()
    new_file = os.path.join(os.getcwd(), "data.txt")
    os.rename(root.filename,new_file)

    createsi()
    mainloop()
