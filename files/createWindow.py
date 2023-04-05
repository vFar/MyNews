from tkinter import *
from PIL import Image, ImageTk

root = None
body = None
content = None
cWindow = None
global article1, article2
article1 = 0
article2 = 1
 
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
    global root, content, article1, article2
    

    root = Tk()
    root.title("Tests")

    root.minsize(1280, 720)
    root.maxsize(1600, 900)
    root.geometry('1280x720')
    root.configure(bg="white")

    from contents import navbar, logo, content, categories, articles, titles, loadArticles
    navbar.pack(anchor=N, fill="both")
    logo.grid(column=0, row=0, pady=10, padx=50)

    counter = 1
    for category in categories:
        if len(categories) == counter:
            category.grid(column=counter + 1, row=0, pady=10, padx=40, sticky=NE)
        else:
            category.grid(column=counter + 1, row=0, pady=10, padx=40)
        counter = counter + 1

    content.place(x=0, y=50)
    loadArticles(article1, article2)

    def nextArticles():
        global article1, article2
        if article1<=12 and article2<=13:
            article1=article1+2
            article2=article2+2
            print(f"{article1} next")
            loadArticles(article1, article2)
        else:
            article1=0
            article2=1

    def backArticles():
        global article1, article2
        if article1 >= 1 and article2 >=2:

            article1=article1-2
            article2=article2-2
            print(f"{article1} next")
            loadArticles(article1, article2)
        else:
            print("cannot back")

    nextBtn=Button(root, text="Nākošais", command=lambda: nextArticles())
    nextBtn.place(x=1200, y=600)

    backBtn=Button(root, text="Iepriekšējais", command=lambda: backArticles())
    backBtn.place(x=50, y=600)




    center(root)
    root.mainloop()

    print(article1)
