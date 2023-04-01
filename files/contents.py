from tkinter import *
from PIL import Image,ImageTk

from createWindow import window



navbar = Frame(window, bg='yellow', height=50, width=1600)
     
logo = Label(navbar, text="MyNews", bg="Yellow")

categories=[Label(navbar, text="Sports"),
             Label(navbar, text="IT"),
               Label(navbar, text="Kriminālziņas"),
               Label(navbar, text="Veselība"),
               Label(navbar, text="Sabiedrība"),
               Label(navbar, text="Ēdiens")]

content = Frame(window, width=1600, height=1000)
article = Frame(content, width=1000, height=200, bg="white")
conet = Label(article, text="Šīs ir lielas ziņas, tests, tests")
    

