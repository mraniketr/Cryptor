import math
from  pyperclip import copy
from tkinter import *
from tkinter import messagebox

# transposition cipher
# ref - https://inventwithpython.com/hacking/chapter8.html
def tcenc(master,e1,e2):
    msg = e1.get()
    key = int(e2.get())
    cipher = encmsg(key, msg)
    copy(str(cipher ))
    l2 = Label(master, text=(cipher + '|'))
    l2.pack()
    messagebox.showinfo("Success", "Result is copied in the clipboard")



def encmsg(mkey, message):
    cipher = [''] * mkey
    for col in range(mkey):
        pos = col
        while pos < len(message):
            cipher[col] += message[pos]
            pos += mkey
    return ''.join(cipher)


# decprytion of transpositon cipher
def tcdec(master,e1,e2):
    myMessage = e1.get()
    myKey =int(e2.get())
    plaintext = decryptMessage(myKey, myMessage)
    copy(str(plaintext))
    l2 = Label(master, text=(plaintext))
    l2.pack()



def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = list(' ' * numOfColumns)
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)


