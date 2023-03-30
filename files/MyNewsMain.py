from tkinter import *
from PIL import Image,ImageTk

from createWindow import center, createWindowTk
from contents import buttons

window =createWindowTk()
buttons()
center(window)
window.mainloop()
