from tkinter import *
from PIL import Image, ImageTk
import os.path
import ctypes
import random

root = None
body = None
content = None
cWindow = None
global article1, categories, toggleDropdown
article1 = 0
toggleDropdown = False
dropdownIndex = None
categories = []
bCategories = []
toggleSaved=False


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
    global root, content, article1, article2, categories, dropdown, reloadSavedList
    savedArr=[]

    root = Tk()
    root.title("MyNews | NewsAPI")

    #root.img = PhotoImage(file='images/news.png')
    #root.iconphoto ( False, root.img)

    root.iconbitmap(root, "images/news.ico")

    root.resizable(0, 0)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    dropdown = Frame(root, width=700, height=700, bg="#205fc7")
    root.minsize(1280, 720)
    root.maxsize(1920, 1080)
    root.geometry('1280x720')
    root.configure(bg="white")

    from contents import navbar1,navbar2,slogan, logo, content, loadArticles, sub_categories, filterArticles, homeartLen, articles, checkSavedTxt, open_link, deleteArticle
    
    article1 = random.randint(0, 99)

    navbar1.pack(anchor=N, fill="both", pady=0, padx=0)
    navbar2.pack(anchor=N, fill="both", pady=0, padx=0)
    savedArr=checkSavedTxt()
    logo.place(relx=0.5, rely=0.5, anchor='center')
    slogan.place(relx=0.5, rely=0.81, anchor='center')

    def showDropdown(cat):
        global dropdown, toggleDropdown, dropdownIndex
        if toggleDropdown == False:
            dropdownIndex=cat
            match cat:
                case 0:
                    toggleDropdown=True
                    dropdown.place(x=155, y=250)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 1:
                    toggleDropdown=True
                    dropdown.place(x=310, y=250)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 2:
                    toggleDropdown=True
                    dropdown.place(x=445, y=250)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 3:
                    toggleDropdown=True
                    dropdown.place(x=575, y=250)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 4:
                    toggleDropdown=True
                    dropdown.place(x=730, y=250)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 5:
                    toggleDropdown=True
                    dropdown.place(x=875, y=250)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 6:
                    toggleDropdown=True
                    dropdown.place(x=1000, y=250)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
        else:
            dropdownIndex = None
            for index, other_button in enumerate(categories):
                        if index != cat:
                            other_button.config(state=NORMAL)
            for i in range(0,4):
                    sub_categories[cat][i].grid_forget()
            dropdown.place_forget()
            toggleDropdown=False
        


    categories=[Button(navbar2, padx=20, text="Bizness", cursor="hand2", fg="white", bg="#2367d9", font=('MS Sans Serif', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(0)),
            Button(navbar2, padx=20, text="Izklaide", cursor="hand2", fg="white", bg="#2367d9", font=('MS Sans Serif', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(1)),
            Button(navbar2, padx=20, text="Vispārīgi", cursor="hand2", fg="white", bg="#2367d9", font=('MS Sans Serif', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(2)),
            Button(navbar2, padx=20, text="Veselība", cursor="hand2", fg="white", bg="#2367d9", font=('MS Sans Serif', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(3)),
            Button(navbar2, padx=20, text="Zinātne", cursor="hand2", fg="white", bg="#2367d9", font=('MS Sans Serif', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(4)),
            Button(navbar2, padx=20, text="Sports", cursor="hand2", fg="white", bg="#2367d9", font=('MS Sans Serif', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(5)),
            Button(navbar2, padx=20, text="Tehnoloģijas", cursor="hand2", fg="white", bg="#2367d9", font=('MS Sans Serif', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(6))]
    
    FilterBtn = Button(navbar2, cursor="hand2", text="Filtrēt", bg="#eee", font=('MS Sans Serif', 14), padx=25, activeforeground="#123670", activebackground="#dedfe0", command=lambda: filterArticles(dropdownIndex, article1))
    FilterBtn.grid(column=9, row=0, pady=10, padx=10)

    navbar2.grid_columnconfigure(0, weight=1, uniform="categories")
    navbar2.grid_columnconfigure(len(categories)+2, weight=1, uniform="categories")
   
    counter = 1
    for category in categories:
        category.grid(column=counter + 1, row=0, pady=10, padx=10)
        navbar2.grid_columnconfigure(counter + 1, weight=1, uniform="categories")
        counter += 1 

    savedList=Button(navbar2, cursor="hand2", bg='white', text="📃", font=('MS Sans Serif', 20), height=1, width=5, command= lambda: openSavedList())
    savedList.grid(column=0, row=0, pady=10, padx=10)

    content.place(x=0, y=500)
    loadArticles(article1)
    def nextArticles():
        global article1
        if article1<=homeartLen-2:
            if article1 == 100:
                article1 = 0
            else:
                article1=random.randint(0,99)

            loadArticles(article1)
        else:
            article1=0

    def backArticles():
        global article1
        if article1 >= 1:

            article1=random.randint(0,99)
            loadArticles(article1)

    nextBtn=Button(root, text=">", fg="white", cursor="hand2", bg="#2367d9", font=('MS Sans Serif', 36, 'bold'), pady= 30, padx=20, activeforeground="#123670", activebackground="#dedfe0", command=lambda: nextArticles())
    backBtn=Button(root, text="<", fg="white", cursor="hand2", bg="#2367d9", font=('MS Sans Serif', 36, 'bold'), pady= 30, padx=20, activeforeground="#123670", activebackground="#dedfe0", command=lambda: backArticles())
    backBtn.place(x=50, y=600)

    nextBtn.place(x=1160, y=400)
    backBtn.place(x=21, y=400)

    
    
    def openSavedList():
        global savedListBox, toggleDropdown
        toggleSaved=True
        savedArr=checkSavedTxt()
        savedListBox=Frame(root, width=1000, height=720, bg="#205fc7", border=2)
        savedListBox.place(x=0, y=200)
        savedList.grid_forget()
        savedExit=Button(savedListBox, cursor="hand2", bg='red', text="🡨", font=('MS Sans Serif', 20), fg="white", height=1, width=5, command= lambda: [savedExit.destroy(),savedList.grid(column=0, row=0, pady= 10, padx=10), savedListBox.place_forget()])
        savedExit.place(x=28, y=8)

        articles[article1].pack_forget()
        nextBtn.place_forget()
        backBtn.place_forget()
        navbar2.pack_forget()

        for index, obj in enumerate(savedArr):
            box=Frame(savedListBox, bg="#205fc7", highlightbackground="black", highlightthickness=2, cursor="hand2", padx=100)
            box.pack(anchor=N)
            box.bind("<Button-1>", lambda e, url=savedArr[index][2]: open_link(url))
            title=Label(box, text=savedArr[index][0], fg="white", bg="#205fc7")
            desc=Label(box, text=savedArr[index][1], fg="white", bg="#205fc7")
            deleteBtn=Button(box, text="🗑️", bg="red", fg="black", command=lambda: [deleteArticle(savedArr[index][2]) , reloadSavedList()])
            deleteBtn.place(x=1, y=1)
            title.pack(anchor=NW)
            title.bind("<Button-1>", lambda e, url=savedArr[index][2]: open_link(url))
            desc.pack(anchor=W)
            desc.bind("<Button-1>", lambda e, url=savedArr[index][2]: open_link(url))
        
    def reloadSavedList():
        savedList.grid(column=0, row=0, pady= 10, padx=10)
        savedListBox.place_forget()
        openSavedList()


    center(root)
    root.mainloop()