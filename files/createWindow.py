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
    
    window.configure(bg="light blue")
    window.minsize(1280,720)
    window.maxsize(1600,900)
    # Add image file
    # Add image file
    window.geometry(f'{1600}x{900}+{1}+{1}')

    
    
    from contents import navbar, logo, conet, content, categories
    navbar.place(x=0, y=0)
    logo.place(x=15, y=15)

    distance=100
    counter=0
    for category in categories:
        category.place(x=distance, y = 15)
        distance=distance+100
        counter=counter+1
        

    content.place(x=0, y=50)
    conet.place(x=25, y=25)


    center(window)
    window.mainloop()
    