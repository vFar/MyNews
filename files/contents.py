from tkinter import *
from PIL import Image,ImageTk
import random

from createWindow import root



navbar = Frame(root, bg='yellow', height=50, width=1600)
     
logo = Label(navbar, text="MyNews", bg="Yellow")

categories=[Label(navbar, text="Sports", bg="yellow", font=("black")),
             Label(navbar, text="IT", bg="yellow", font=("black")),
               Label(navbar, text="Kriminālziņas", bg="yellow", font=("black")),
               Label(navbar, text="Veselība", bg="yellow", font=("black")),
               Label(navbar, text="Sabiedrība", bg="yellow", font=("black")),
               Label(navbar, text="Ēdiens", bg="yellow", font=("black"))]
content = Frame(root, width=1280, height=1000, padx=1600, bg="white")
titles= []
articles = []
for i in range(0,5):
    print(0)
    articles.insert(i,(Frame(root, width=1000, height=300, bg="black")))
    titles.insert(i,(Label(articles[i], text=i)))



    

