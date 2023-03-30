from tkinter import *
from PIL import Image,ImageTk
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
    
def createWindowTk():
    window = Tk()
    window.title("Tests")
    # Add image file
    # Add image file
    bg = PhotoImage(file = "images/redblack.png")
    window.geometry(f'{1280}x{720}+{1}+{1}')
    # Create Canvas
    canvas1 = Canvas( window, width = 1280,
                    height = 720)
    
    canvas1.pack(fill= "both", expand = False)
    
    # Display image
    canvas1.create_image( 0, 0, image = bg, 
                        anchor = "nw")
    
    # Add Text
    canvas1.create_text( 200, 250, text = "Welcome", fill="white")
    
    # Create Buttons
    button1 = Button( window, text = "Exit")
    button3 = Button( window, text = "Start")
    button2 = Button( window, text = "Reset")
    
    # Display Buttons
    button1_canvas = canvas1.create_window( 100, 10, 
                                        anchor = "nw",
                                        window = button1)
    
    button2_canvas = canvas1.create_window( 100, 40,
                                        anchor = "nw",
                                        window = button2)
    
    button3_canvas = canvas1.create_window( 100, 70, anchor = "nw",
                                        window = button3)

    center(window)
    window.mainloop()