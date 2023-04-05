from tkinter import *
from PIL import Image,ImageTk
import random

from createWindow import root

navbar = Frame(root, bg='yellow', height=50, width=1600)
     
logo = Label(navbar, text="MyNews", bg="Yellow")

categories=[Button(navbar, text="Bizness", bg="yellow", font=("black")),
             Button(navbar, text="Izklaide", bg="yellow", font=("black")),
               Button(navbar, text="Vispārīgi", bg="yellow", font=("black")),
               Button(navbar, text="Veselība", bg="yellow", font=("black")),
               Button(navbar, text="Zinātne", bg="yellow", font=("black")),
               Button(navbar, text="Sports", bg="yellow", font=("black")),
              Button(navbar, text="Tehnoloģijas", bg="yellow", font=("black"))]
content = Frame(root, width=1280, height=1000, padx=1600, bg="white")

titles= []
articles = []
for i in range(0,15):
    print(0)
    articles.insert(i,(Frame(root, width=1000, height=250, bg="black")))
    titles.insert(i,(Label(articles[i], text=i)))
dropdown=Frame(root, width=300, height=300, bg="black")

Fsub_categories=[[Checkbutton(dropdown, text="Futbols"), Checkbutton(dropdown, text="Basketbols"), Checkbutton(dropdown, text="Golfs")],
                [Checkbutton(dropdown, text="Python"), Checkbutton(dropdown, text="Tkinter"), Checkbutton(dropdown, text="MySQL")],
                [Checkbutton(dropdown, text="Negadījumi"), Checkbutton(dropdown, text="Slepkavības"), Checkbutton(dropdown, text="Zādzības")],
                [Checkbutton(dropdown, text="Python"), Checkbutton(dropdown, text="Tkinter"), Checkbutton(dropdown, text="MySQL")],
                [Checkbutton(dropdown, text="Python"), Checkbutton(dropdown, text="Tkinter"), Checkbutton(dropdown, text="MySQL")],
                [Checkbutton(dropdown, text="Python"), Checkbutton(dropdown, text="Tkinter"), Checkbutton(dropdown, text="MySQL")]]

Bsub_categories = [[Checkbutton(dropdown, text="Football"), Checkbutton(dropdown, text="Basketbols"), Checkbutton(dropdown, text="Golfs")],
                [Checkbutton(dropdown, text="Python"), Checkbutton(dropdown, text="Tkinter"), Checkbutton(dropdown, text="MySQL")],
                [Checkbutton(dropdown, text="Negadījumi"), Checkbutton(dropdown, text="Slepkavības"), Checkbutton(dropdown, text="Slikti")],
                [Checkbutton(dropdown, text="Python"), Checkbutton(dropdown, text="Tkinter"), Checkbutton(dropdown, text="MySQL")],
                [Checkbutton(dropdown, text="Python"), Checkbutton(dropdown, text="Tkinter"), Checkbutton(dropdown, text="MySQL")],
                [Checkbutton(dropdown, text="Python"), Checkbutton(dropdown, text="Tkinter"), Checkbutton(dropdown, text="MySQL")]]

                







def loadArticles(article1, article2):
  print(f"{article1} load")

  for i in range(0, 15):
    articles[i].pack_forget()

  articles[article1].pack(pady=30)
  titles[article1].place(x=25, y=25)

  articles[article2].pack(pady=30)
  titles[article2].place(x=25, y=25)
  