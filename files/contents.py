from tkinter import *
from PIL import Image,ImageTk
import random

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
titles= []
articles = []
for i in range(0,5):
    print(0)
    articles.insert(i,(Frame(content, width=1000, height=300, bg="black")))
    titles.insert(i,(Label(articles[i], text=random.randint(1,100))))



    

