import base64
from tkinter import *
import tkinter.messagebox
from pyperclip import copy
from tkinter import messagebox

# base64 encoding3
    # https://docs.python.org/2/library/base64.html

def b64enc(master,e1):
    msg = e1.get()
    encoded_data = base64.b64encode(msg.encode())
    copy(str(encoded_data,'utf-8'))
    l2 = Label(master, text=str(encoded_data,'utf-8'))
    l2.pack()
    messagebox.showinfo("Success", "Result is copied in the clipboard")

def b64dec(master,e1):
    msg=e1.get()
    decoded_data = base64.b64decode(msg)
    copy(str(decoded_data,'utf-8'))
    l2 = Label(master, text=str(decoded_data,'utf-8'))
    l2.pack()

