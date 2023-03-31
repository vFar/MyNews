from tkinter import *
from PIL import Image,ImageTk

window = None
body = None
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
    window.geometry(f'{1600}x{900}+{1}+{1}')

    body = Frame(window,bg="blue", width = 1600,
                    height = 900)
    body.grid_propagate(False)
    
    body.grid(columnspan=15, rowspan=5)
    
    # Display image
    
    from contents import navbar, logo
    navbar.grid(row=0,columnspan=15, sticky=N)
    logo.grid(row=0, column=0, sticky=NW)
    center(window)
    window.mainloop()
    