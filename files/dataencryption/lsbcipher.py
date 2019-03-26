import os
import pyperclip
from tkinter import messagebox

def createsi():
	os.system("start cmd")
	pyperclip.copy("steghide --embed -ef data.txt -cf final.jpg  -e none -Z")
	messagebox.showinfo("Attention", "paste the clipboard on the cmd")


def extractdata():
	os.system("start cmd")
	pyperclip.copy("steghide --extract -sf final.jpg -xf fdata.txt")
	messagebox.showinfo("Attention", "paste the clipboard on the cmd")