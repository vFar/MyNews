from tkinter import *
from PIL import Image,ImageTk

from createWindow import window, body



navbar = Frame(window, bg='yellow', height=50, width=1600)
     
logo = Label(navbar, text="MyNews", bg="Yellow")

categories=[Label(navbar, text="Sports", bg="blue", padx=20), Label(navbar, text="IT", bg="red", padx=20), Label(navbar, text="Kriminālziņas", bg="black", padx=20)]

content = Frame(window, width=1600, height=900, bg="blue")
conet = Label(content, text="ziņa")
    

