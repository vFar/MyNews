from tkinter import *
from PIL import Image,ImageTk
import MyNewsMain
import createWindow

def buttons():
     # Add Text
    window = MyNewsMain.window
    canvas1=createWindow.canvas1
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


