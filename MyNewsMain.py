from tkinter import *
from PIL import Image,ImageTk

window = Tk()

window.title("Tests")
window.geometry('1280x720')
# Add image file
  
# Add image file
bg = PhotoImage(file = "images/redblack.png")
res = resizeImage(bg, 1280, 720)
background= ImageTk.PhotoImage(res)
  
# Create Canvas
canvas1 = Canvas( window, width = 1280,
                 height = 720)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
  
# Add Text
canvas1.create_text( 200, 250, text = "Welcome")
  
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
window.mainloop()
