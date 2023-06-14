from tkinter import *
from PIL import Image, ImageTk

root = None
body = None
content = None
cWindow = None
global article1, article2, categories, toggleDropdown
article1 = 0
article2 = 1
toggleDropdown = False
dropdownIndex = None
categories = []
bCategories = []

 
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
    global root, content, article1, article2, categories, dropdown
    

    root = Tk()
    root.title("MyNews | Sākuma ekrāns")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    dropdown = Frame(root, width=700, height=700, bg="#205fc7")
    root.minsize(1280, 720)
    root.maxsize(1920, 1080)
    root.geometry('1280x720')
    root.configure(bg="white")

    from contents import navbar1,navbar2,slogan, logo, content, loadArticles, sub_categories, filterArticles, homeartLen, articles
    
    navbar1.pack(anchor=N, fill="both", pady=0, padx=0)
    navbar2.pack(anchor=N, fill="both", pady=0, padx=0)

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
                        print(index)
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 1:
                    toggleDropdown=True
                    dropdown.place(x=310, y=250)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        print(index)
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 2:
                    toggleDropdown=True
                    dropdown.place(x=445, y=250)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        print(index)
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 3:
                    toggleDropdown=True
                    dropdown.place(x=575, y=250)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        print(index)
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 4:
                    toggleDropdown=True
                    dropdown.place(x=730, y=250)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        print(index)
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 5:
                    toggleDropdown=True
                    dropdown.place(x=875, y=250)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        print(index)
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 6:
                    toggleDropdown=True
                    dropdown.place(x=1000, y=250)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        print(index)
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
        else:
            dropdownIndex = None
            for index, other_button in enumerate(categories):
                        print(index)
                        if index != cat:
                            other_button.config(state=NORMAL)
            for i in range(0,4):
                    sub_categories[cat][i].grid_forget()
            dropdown.place_forget()
            toggleDropdown=False
        


    categories=[Button(navbar2, text="Bizness", cursor="hand2", fg="white", bg="#2367d9", font=('Calibri', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(0)),
            Button(navbar2, text="Izklaide", cursor="hand2", fg="white", bg="#2367d9", font=('Calibri', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(1)),
            Button(navbar2, text="Vispārīgi", cursor="hand2", fg="white", bg="#2367d9", font=('Calibri', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(2)),
            Button(navbar2, text="Veselība", cursor="hand2", fg="white", bg="#2367d9", font=('Calibri', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(3)),
            Button(navbar2, text="Zinātne", cursor="hand2", fg="white", bg="#2367d9", font=('Calibri', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(4)),
            Button(navbar2, text="Sports", cursor="hand2", fg="white", bg="#2367d9", font=('Calibri', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(5)),
            Button(navbar2, text="Tehnoloģijas", cursor="hand2", fg="white", bg="#2367d9", font=('Calibri', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(6))]
    
    FilterBtn = Button(navbar2, cursor="hand2", text="Filtrēt", bg="#eee", font=('Calibri', 14), padx=25, activeforeground="#123670", activebackground="#dedfe0", command=lambda: filterArticles(dropdownIndex))
    FilterBtn.grid(column=9, row=0, pady=10, padx=10)

    navbar2.grid_columnconfigure(0, weight=1, uniform="categories")
    navbar2.grid_columnconfigure(len(categories)+2, weight=1, uniform="categories")
   
    counter = 1
    for category in categories:
        category.grid(column=counter + 1, row=0, pady=10, padx=10)
        navbar2.grid_columnconfigure(counter + 1, weight=1, uniform="categories")
        counter += 1 

    content.place(x=0, y=500)
    loadArticles(article1, article2)
    def nextArticles():
        global article1, article2
        if article1<=homeartLen-2 and article2<=homeartLen-1:
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

    nextBtn=Button(root, text=">", fg="white", cursor="hand2", bg="#2367d9", font=('Calibri', 36, 'bold'), pady= 30, padx=20, activeforeground="#123670", activebackground="#dedfe0", command=lambda: nextArticles())
    backBtn=Button(root, text="<", fg="white", cursor="hand2", bg="#2367d9", font=('Calibri', 36, 'bold'), pady= 30, padx=20, activeforeground="#123670", activebackground="#dedfe0", command=lambda: backArticles())
    backBtn.place(x=50, y=600)

    def check_winstate(event):
        if root.state() == 'zoomed':
            nextBtn.place(x=1780, y=500)
            backBtn.place(x=30, y=500)
        else:
            nextBtn.place(x=1160, y=400)
            backBtn.place(x=21, y=400)
    
    def openSavedList():
        nextBtn.place_forget()
        backBtn.place_forget()
        articles.pack_forget()

    root.bind('<Map>', check_winstate)



    center(root)
    root.mainloop()