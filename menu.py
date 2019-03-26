from tkinter import *
from files.decmenu import *
from files.encmenu import *


root =Tk()
root.title("CRYPTER 1.0")
root.geometry("200x300")


l1=Label(root,text="Welcome to Crypter 1.0")


b1=Button(root,text="ENCRYPT",command=create_enc)
b2=Button(root,text="DECRYPT",command=create_dec)

l1.pack()
b1.pack(fill=X,padx=20)
b2.pack(fill=X,padx=20)

mainloop()