from tkinter import *
from PIL import Image, ImageTk

root = None
body = None
content = None
cWindow = None

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_x()
    win_width = width + frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def myNews():
    global root, content

    root = Tk()
    root.title("Tests")

    root.minsize(1280, 720)
    root.maxsize(1600, 5000)
    root.geometry('1280x720')
    root.configure(bg="white")

    from contents import navbar, logo, content, categories, articles, titles
    navbar.pack(anchor=N)
    logo.grid(column=0, row=0, pady=10, padx=50)

    distance = 0.05
    counter = 1
    for category in categories:
        if len(categories) == counter:
            category.grid(column=counter + 1, row=0, pady=10, padx=40, sticky=NE)
        else:
            category.grid(column=counter + 1, row=0, pady=10, padx=40)
        counter = counter + 1

    content.place(x=0, y=50)
    articles[0].pack(pady=100)
    titles[0].place(x=25, y=25)

    articles[1].pack(pady=50)
    titles[1].place(x=25, y=25)

    counter = 0
    for article in articles:
        article.pack(pady=50)
        titles[counter].place(x=25, y=25)
        counter = counter + 1


    center(root)
    root.mainloop()
