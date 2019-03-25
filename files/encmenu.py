from tkinter import *
from files.msgencryption.files2.reversecipher import *
from functools import partial


def create_enc():
    window=Toplevel()
    window.title("Encryption")
    window.geometry("200x300+270+50")

    e1 = Entry(window, bd=5)
    e1.pack()

    b1f=partial(revc,window,e1)
    l1 = Label(window, text="Text Encryption Algorithm's")
    b1 = Button(window, text="Reverse Cipher",command=b1f)
    b2 = Button(window,text="Transposition Cipher")
    b3= Button(window, text ="base64 cipher")
    b4 = Button(window, text="File Encryption")
    b5 = Button(window, text="LSB Encryption")


    l1.pack()

    #e1.pack()

    b2.pack(fill=X,padx=20)
    b3.pack(fill=X,padx=20)
    b1.pack(fill=X,padx=20)
    b4.pack(fill=X,padx=20)
    b5.pack(fill=X,padx=20)



