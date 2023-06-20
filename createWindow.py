from tkinter import *
from PIL import Image, ImageTk
import os.path
import ctypes
import random
from datetime import datetime, timedelta
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = None
body = None
content = None
cWindow = None
global article1, categories, toggleDropdown
article1 = random.randint(0,99)
toggleDropdown = False
dropdownIndex = None
categories = []
bCategories = []
toggleSaved=False
date_from = None
date_to = None


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
    global root, content, article1, article2, categories, dropdown, reloadSavedList, date_from_in, date_to_in, result
    savedArr=[]

    root = Tk()
    root.title("MyNews | NewsAPI")

    root.iconbitmap(default=resource_path("news.ico"))
    root.resizable(0, 0)



    dropdown = Frame(root, width=700, height=700, bg="#205fc7", highlightbackground="black", highlightthickness=1)
    root.minsize(1280, 720)
    root.maxsize(1920, 1080)
    root.geometry('1280x720')
    root.configure(bg="#eee")

    from contents import navbar1,navbar2,slogan, logo, content, loadArticles, sub_categories, filterArticles, homeartLen, articles, checkSavedTxt, open_link, deleteArticle, randomArticles, filterInterval
    
    article1 = random.randint(0, 99)

    navbar1.pack(anchor=N, fill="both", pady=0, padx=0)
    navbar2.pack(anchor=N, fill="both", pady=0, padx=0)
    savedArr=checkSavedTxt()
    logo.place(relx=0.5, rely=0.5, anchor='center')
    slogan.place(relx=0.5, rely=0.82, anchor='center')
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

    FilterBtn = Button(navbar2, cursor="hand2", text="⚙️", bg="#eee", font=('MS Sans Serif', 14), padx=25, activeforeground="#123670", activebackground="#dedfe0", command=lambda: [filterArticles(dropdownIndex),  nextBtn.tkraise(), backBtn.tkraise()])
    FilterBtn.grid(column=9, row=0, pady=10, padx=10)

    RefreshArticleBtn=Button(root, cursor="hand2", text="↻", bg="#2671eb", fg='black', foreground='white', width=5, height=1, font=('MS Sans Serif', 16), command=lambda: [randomArticles(), loadArticles(random.randint(0,99)), nextBtn.tkraise(), backBtn.tkraise()])
    RefreshArticleBtn.place(x=25, y=655)
    calendarBox=Frame(root, bg="black")
    calendarBox.place(x=800, y=655)
    date_from = Label(calendarBox, text="Date From:")
    date_from.grid(column=0, row=0)
    date_from_in = Entry(calendarBox)
    date_from_in.grid(column=1, row=0)

    date_to = Label(calendarBox, text="Date To:")
    date_to.grid(column=0, row=1)
    date_to_in = Entry(calendarBox)
    date_to_in.grid(column=1, row=1)

    def datefromin(event):
        date_from_in.config(state=NORMAL)
        date_from_in.delete(0, END)
    
    date_from_in.insert(0, 'YYYY-MM-DD')
    date_from_in.config(state=DISABLED)
    date_from_in.bind("<Button-1>", datefromin)

    def datetoin(event):
        date_to_in.config(state=NORMAL)
        date_to_in.delete(0, END)
    
    date_to_in.insert(0, 'YYYY-MM-DD')
    date_to_in.config(state=DISABLED)
    date_to_in.bind("<Button-1>", datetoin)






# Create a button to trigger the date range validation
    submit_button = Button(calendarBox, text="Submit", command= lambda: filterInterval(date_from_in, date_to_in, result))
    submit_button.grid(column=2, row=1)

# Create a label to display the result
    result = Label(calendarBox, text="")
    result.grid(column=3, row=0)


    navbar2.grid_columnconfigure(0, weight=1, uniform="categories")
    navbar2.grid_columnconfigure(len(categories)+2, weight=1, uniform="categories")
   
    counter = 1
    for category in categories:
        category.grid(column=counter + 1, row=0, pady=10, padx=10)
        navbar2.grid_columnconfigure(counter + 1, weight=1, uniform="categories")
        counter += 1 

    savedList=Button(navbar2, cursor="hand2", bg='#eee', text="📃", font=('MS Sans Serif', 20), height=1, width=5, command= lambda: openSavedList())
    savedList.grid(column=0, row=0, pady=10, padx=10)

    content.place(x=0, y=500)
    loadArticles(article1)
    def nextArticles():
        global article1
        if article1<=homeartLen-1:
            if article1 == 99:
                article1 = 0
            else:
                article1=article1+1

            loadArticles(article1)
        else:
            article1=0

    def backArticles():
        global article1
        if article1<=homeartLen-1:
            if article1 == 0:
                article1 = 99
            else:
                article1=article1-1

            loadArticles(article1)
        else:
            article1=99

    nextBtn=Button(root, text=">", fg="white", cursor="hand2", bg="#2367d9", font=('MS Sans Serif', 36, 'bold'), pady= 30, padx=20, activeforeground="#123670", activebackground="#dedfe0", command=lambda: nextArticles())
    backBtn=Button(root, text="<", fg="white", cursor="hand2", bg="#2367d9", font=('MS Sans Serif', 36, 'bold'), pady= 30, padx=20, activeforeground="#123670", activebackground="#dedfe0", command=lambda: backArticles())

    nextBtn.place(x=1160, y=400)
    backBtn.place(x=21, y=400)

    
    
    def openSavedList():
        global savedListBox, toggleDropdown, savedBG
        toggleSaved = True
        savedArr = checkSavedTxt()
        savedBG = Frame(root, bg="#205fc7")
        savedBG.place(x=0, y=0, relwidth=1, relheight=1)  # Place at top-left and fill the entire screen

        canvas = Canvas(savedBG, bg="#205fc7")
        canvas.pack(side='left', fill='both', expand=True)
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))  # Enable scrolling with mouse wheel

        savedListBox = Frame(canvas, bg="#205fc7")
        savedListBox.pack(side='left', fill='both', expand=True)

        savedExit = Button(savedListBox, cursor="hand2", bg='red', text="🡨", font=('MS Sans Serif', 20), fg="white",
                        height=1, width=5, command=lambda: [savedBG.place_forget(), SavedExit(savedExit)])
        savedExit.place(x=26.5, y=7.8)

        if len(savedArr) == 0:  # No saved entries
            noSavedLabel = Label(savedListBox, text="No saved entries", font=('MS Sans Serif', 12), fg="white",
                                bg="#205fc7")
            noSavedLabel.pack(pady=50)

        if len(savedArr) > 5:  # Enable scrollbar only if there are saved entries
            v_scrollbar = Scrollbar(savedListBox, orient='vertical', command=canvas.yview)
            v_scrollbar.pack(side='right', fill='y')

            canvas.configure(yscrollcommand=v_scrollbar.set)
            canvas.create_window((0, 0), window=savedListBox, anchor='nw')

            savedListBox.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))


        for index, obj in enumerate(savedArr):
            box = Frame(savedListBox, bg="#205fc7", highlightbackground="black", highlightthickness=2, cursor="hand2",
                        width=500)
            box.pack(ipadx=100, ipady=20, padx=220, pady=15, fill=BOTH, expand=True)
            box.bind("<Button-1>", lambda e, url=savedArr[index][2]: open_link(url))
            title = Label(box, text=savedArr[index][0], justify="left", font=('MS Sans Serif', 12), fg="white",
                        bg="#205fc7")
            desc = Label(box, text=savedArr[index][1], justify="left", font=('MS Sans Serif', 10), fg="white",
                        bg="#205fc7", wraplength=700)
            deleteBtn = Button(box, text="🗑️", bg="red", fg="black",
                            command=lambda url=savedArr[index][2]: [deleteArticle(url), reloadSavedList()])
            print(savedArr[index][2], " save")
            deleteBtn.place(x=700, y=25)
            title.pack(anchor=NW)
            title.bind("<Button-1>", lambda e, url=savedArr[index][2]: open_link(url))
            desc.pack(anchor=W)
            desc.bind("<Button-1>", lambda e, url=savedArr[index][2]: open_link(url))

        def reloadSavedList():
            savedList.grid(column=0, row=0, pady=10, padx=10)
            savedListBox.place_forget()
            savedBG.place_forget()
            openSavedList()

        def SavedExit(savedExit):
            savedExit.destroy()
            savedList.grid(column=0, row=0, pady=10, padx=10)
            savedListBox.place_forget()
            savedBG.place_forget()

            nextBtn.place(x=1160, y=400)
            backBtn.place(x=21, y=400)

            navbar2.pack(anchor=N, fill="both", pady=0, padx=0)
            loadArticles(article1)



    center(root)
    root.mainloop()