from tkinter import *
import tkinter.messagebox
from pyperclip import copy
from tkinter import messagebox

def revc(master,e1):
    message=e1.get()
    crev=''
    i=len(message)-1
    while i>=0:
        crev=crev+message[i]
        i=i-1
    copy(crev)
    l2=Label(master,text=crev)
    l2.grid(row=8,column=1)

    messagebox.showinfo("Success", "Result is copied in the clipboard")



