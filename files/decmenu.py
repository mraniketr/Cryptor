from tkinter import *
from files.msgencryption.reversecipher import *
from functools import partial
from files.msgencryption.basesix4 import *
from files.msgencryption.transpostion import *
from files.dataencryption.fileselector import *
from files.dataencryption.dataHIDE import *




def create_dec():
    window=Toplevel()
    window.title("Decryption")
    window.geometry("200x300+270+50")

    e1 = Entry(window, bd=5)
    e1.pack()

    e2 = Entry(window, bd=1)
    e2.pack()

    b1f=partial(revc,window,e1)
    b2f=partial(b64dec, window, e1)
    b3f=partial(tcdec,window,e1,e2)
    b4f=partial(fuzip)
    b5f=partial(extractdata)


    l1 = Label(window, text="Text Decryption Algorithm's")
    b1 = Button(window, text="Reverse Cipher",command=b1f)
    b2 = Button(window,text="Transposition Cipher",command=b3f)
    b3= Button(window, text ="base64 cipher", command=b2f)
    b4 = Button(window, text="File Encryption",command=b4f)
    b5 = Button(window, text="LSB Encryption",command=b5f)


    l1.pack()

    b2.pack(fill=X,padx=20)
    b3.pack(fill=X,padx=20)
    b1.pack(fill=X,padx=20)
    b4.pack(fill=X,padx=20)
    b5.pack(fill=X,padx=20)



