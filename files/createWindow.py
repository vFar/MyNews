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
    root.title("Tests")
    dropdown=Frame(root, width=700, height=700, bg="purple")
    root.minsize(1280, 720)
    root.maxsize(1600, 900)
    root.geometry('1280x720')
    root.configure(bg="white")

    from contents import navbar, logo, content, loadArticles, sub_categories, filterArticles, homeartLen
    

    def showDropdown(cat):
        global dropdown, toggleDropdown, dropdownIndex
        if toggleDropdown == False:
            dropdownIndex=cat
            match cat:
                case 0:
                    toggleDropdown=True
                    dropdown.place(x=50, y=60)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        print(index)
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=i, row=0, pady=10, padx=5)
                case 1:
                    toggleDropdown=True
                    dropdown.place(x=100, y=60)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        print(index)
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=i, row=0, pady=10, padx=5)
                case 2:
                    toggleDropdown=True
                    dropdown.place(x=100, y=60)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        print(index)
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=i, row=0, pady=10, padx=5)
                case 3:
                    toggleDropdown=True
                    dropdown.place(x=100, y=60)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        print(index)
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=i, row=0, pady=10, padx=5)
                case 4:
                    toggleDropdown=True
                    dropdown.place(x=100, y=60)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        print(index)
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=i, row=0, pady=10, padx=5)
                case 5:
                    toggleDropdown=True
                    dropdown.place(x=100, y=60)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        print(index)
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=i, row=0, pady=10, padx=5)
                case 6:
                    toggleDropdown=True
                    dropdown.place(x=100, y=60)
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        print(index)
                        if index != cat:
                            other_button.config(state=DISABLED)
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=i, row=0, pady=10, padx=5)
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
        print(dropdownIndex)

    navbar.pack(anchor=N, fill="both")
    logo.grid(column=0, row=0, pady=10, padx=50)

    categories=[Button(navbar, text="Bizness", bg="yellow", font=("black"), command=lambda:showDropdown(0)),
             Button(navbar, text="Izklaide", bg="yellow", font=("black"), command=lambda:showDropdown(1)),
               Button(navbar, text="Vispārīgi", bg="yellow", font=("black"), command=lambda:showDropdown(2)),
               Button(navbar, text="Veselība", bg="yellow", font=("black"), command=lambda:showDropdown(3)),
               Button(navbar, text="Zinātne", bg="yellow", font=("black"), command=lambda:showDropdown(4)),
               Button(navbar, text="Sports", bg="yellow", font=("black"), command=lambda:showDropdown(5)),
              Button(navbar, text="Tehnoloģijas", bg="yellow", font=("black"), command=lambda:showDropdown(6))]
    
   
    counter = 1
    for category in categories:
        if len(categories) == counter:
            category.grid(column=counter + 1, row=0, pady=10, padx=40, sticky=NE)
        else:
            category.grid(column=counter + 1, row=0, pady=10, padx=40)
        counter = counter + 1

    content.place(x=0, y=50)
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

    nextBtn=Button(root, text="Nākošais", command=lambda: nextArticles())
    nextBtn.place(x=1200, y=600)

    backBtn=Button(root, text="Iepriekšējais", command=lambda: backArticles())
    backBtn.place(x=50, y=600)

    filterBtn = Button(root, text="Filtrēt", bg="red", command=lambda: filterArticles(dropdownIndex))
    filterBtn.place(x=1200, y=40)




    center(root)
    root.mainloop()

    print(article1)
