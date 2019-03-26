import os
import pyperclip


def createsi():
	os.system("start cmd")
	pyperclip.copy("steghide --embed -ef data.txt -cf final.jpg  -e none -Z")

def extractdata():
	os.system("start cmd")
	pyperclip.copy("steghide --extract -sf final.jpg -xf fdata.txt")
