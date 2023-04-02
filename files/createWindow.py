from tkinter import *
from PIL import Image,ImageTk

window = None
body = None
content = None
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()
    
def myNews():
    window = Tk()
    window.title("Tests")
    
    
    window.minsize(1280,720)
    window.maxsize(1600,900)
    # Add image file
    # Add image file
    window.geometry('1600x900')
    window.configure(bg="black")
    
    
    from contents import navbar, logo, content, categories, articles, titles
    navbar.place(x=0, y=0)
    logo.place(x=5, y=15)

    distance=70
    counter=0
    for category in categories:
        if len(category.cget("text")) <=7:
            distance=distance+70
            category.place(x=distance, y = 15)
        elif len(category.cget("text")) >=8:
            distance=distance+80
            category.place(x=distance, y = 15)
            
    content.place(x=0, y=50)
    articles[0].place(relx=0.5, rely=0.15, anchor=CENTER)
    titles[0].place(x=25, y=25)

    articles[1].place(relx=0.5, rely=0.7, anchor=CENTER)
    titles[1].place(x=25, y=25)

    """for article in articles:
        article.place(relx=0.5, rely=0.2+0.1, anchor=CENTER)
        titles[counter].place(x=25, y=25)
        counter=counter+1"""
   

    center(window)
    window.mainloop()
    