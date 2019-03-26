from tkinter import *
from files.msgencryption.reversecipher import *
from functools import partial
from files.msgencryption.basesix4 import *
from files.msgencryption.transpostion import *
from files.dataencryption.fileselector import *
from files.dataencryption.dataHIDE import *


def create_enc():
    window=Toplevel()
    window.title("Encryption")
    window.geometry("300x160+270+50")

    e1 = Entry(window, bd=5)
    e2 = Entry(window, bd=1)

    b1f=partial(revc,window,e1)
    b2f=partial(b64enc, window, e1)
    b3f=partial(tcenc,window,e1,e2)
    b4f=partial(fzip)
    b5f=partial(selection)


    l1 = Label(window, text="Text Encryption Algorithm's")
    l2=Label(window,text="Result = ")
    b1 = Button(window, text="Reverse Cipher",command=b1f)
    b2 = Button(window,text="Transposition Cipher",command=b3f)
    b3= Button(window, text ="base64 cipher", command=b2f)
    b4 = Button(window, text="File Encryption",command=b4f)
    b5 = Button(window, text="LSB Encryption",command=b5f)

    l1.grid(row=0, column=0)
    e1.grid(row=1, column=0, columnspan=2)
    b1.grid(row=2, column=0)
    b3.grid(row=2, column=1)
    e2.grid(row=3, column=0)
    b2.grid(row=3, column=1)
    b4.grid(row=5, column=0)
    b5.grid(row=5, column=1)
    l2.grid(row=8,column=0)

