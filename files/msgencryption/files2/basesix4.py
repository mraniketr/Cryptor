import base64
from tkinter import *
import tkinter.messagebox

# base64 encoding3
    # https://docs.python.org/2/library/base64.html

def b64enc(master,e1):
    msg = e1.get()
    encoded_data = base64.b64encode(msg.encode())
    l2 = Label(master, text=encoded_data)
    l2.pack()


def dec(msg):
    decoded_data = base64.b64decode(msg)
    return decoded_data
