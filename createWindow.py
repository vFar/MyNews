# Importē moduļus, lai varētu izveidot programmatūru
from tkinter import *
from PIL import Image, ImageTk
import os.path
import ctypes
import random
from datetime import datetime, timedelta
import os
import sys

#Funkcija domāta, lai palaistu programmu kā .exe failu ar ikonām
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#Galvenie mainīgie priekš loga izveides(widgets, logs)
root = None
body = None
content = None
cWindow = None
global article1, categories, toggleDropdown # Lai atlasītu mainīgos contents.py fails 
article1 = 0
toggleDropdown = False
dropdownIndex = None
categories = [] # Masīvs, lai pārraidītu kategorijas Front-End
bCategories = [] # Masīvs, lai kategorijas varētu izmantot Back-End
date_from = None
date_to = None
date_from_in=None
date_to_in=None

# Funkcija domāta, lai centrētu logu ekrāna vidū
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

#Galvenā programmatūras funkcija
def myNews():
    global root, content, article1, article2, categories, dropdown, reloadSavedList, date_from_in, date_to_in, result # globālie mainīgie, lai ar tiem varētu darboties ārpus funkcijas

    root = Tk() # Loga definēšana
    root.title("MyNews | NewsAPI")


    root.resizable(0, 0)
    root.minsize(1280, 720) # Pievieno minimālās un maksimālās vērtības logam
    root.maxsize(1920, 1080)
    root.geometry('1280x720')
    root.configure(bg="#eee") # Pievieno logam aizmugures krāsu

    dropdown = Frame(root, width=700, height=700, bg="#205fc7", highlightbackground="black", highlightthickness=1)

    from contents import navbar1,navbar2,slogan, logo, content, loadArticles, sub_categories, filterArticles, homeartLen, checkSavedTxt, open_link, deleteArticle, randomArticles, filterInterval
    # Importē dažādus mainīgos no contents.py faila

    article1 = random.randint(0, 99)# Kad programma tiek palaista artikulas mainīgais tiek veidots nejaušā secibā
    navbar1.pack(anchor=N, fill="both", pady=0, padx=0)
    navbar2.pack(anchor=N, fill="both", pady=0, padx=0)
    checkSavedTxt() # Pārbauda vai ir jau iepriekš veidots fails savedList.txt, ja nav, tad izveido
    logo.place(relx=0.5, rely=0.5, anchor='center')
    slogan.place(relx=0.5, rely=0.82, anchor='center')

    # Funkcija domāta, lai pārraidītu ekrānā dropdown logu tieši precīzi nospiestai kategorijas pogai
    def showDropdown(cat):
        global dropdown, toggleDropdown, dropdownIndex
        if toggleDropdown == False:
            dropdownIndex=cat
            match cat: # No nospiestās kategorijas indekss cat atbilstoši noliek dropdown logu
                case 0:
                    toggleDropdown=True
                    dropdown.place(x=155, y=250)# Dropdown logs tiek nolikts atbilstoši 0 indeksa kategorijai
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        if index != cat:
                            other_button.config(state=DISABLED)# Pārējās kategorijas pogas tiek iestatītas uz izslēgto stāvokli
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 1:
                    toggleDropdown=True
                    dropdown.place(x=310, y=250)# Dropdown logs tiek nolikts atbilstoši 1 indeksa kategorijai
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        if index != cat:
                            other_button.config(state=DISABLED)# Pārējās kategorijas pogas tiek iestatītas uz izslēgto stāvokli
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 2:
                    toggleDropdown=True
                    dropdown.place(x=445, y=250)# Dropdown logs tiek nolikts atbilstoši 2 indeksa kategorijai
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        if index != cat:
                            other_button.config(state=DISABLED)# Pārējās kategorijas pogas tiek iestatītas uz izslēgto stāvokli
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 3:
                    toggleDropdown=True
                    dropdown.place(x=575, y=250)# Dropdown logs tiek nolikts atbilstoši 3 indeksa kategorijai
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        if index != cat:
                            other_button.config(state=DISABLED)# Pārējās kategorijas pogas tiek iestatītas uz izslēgto stāvokli
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 4:
                    toggleDropdown=True
                    dropdown.place(x=730, y=250)# Dropdown logs tiek nolikts atbilstoši 4 indeksa kategorijai
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        if index != cat:
                            other_button.config(state=DISABLED)# Pārējās kategorijas pogas tiek iestatītas uz izslēgto stāvokli
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 5:
                    toggleDropdown=True
                    dropdown.place(x=875, y=250)# Dropdown logs tiek nolikts atbilstoši 5 indeksa kategorijai
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        if index != cat:
                            other_button.config(state=DISABLED)# Pārējās kategorijas pogas tiek iestatītas uz izslēgto stāvokli
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
                case 6:
                    toggleDropdown=True
                    dropdown.place(x=1000, y=250)# Dropdown logs tiek nolikts atbilstoši 6 indeksa kategorijai
                    dropdown.lift()
                    for index, other_button in enumerate(categories):
                        if index != cat:
                            other_button.config(state=DISABLED)# Pārējās kategorijas pogas tiek iestatītas uz izslēgto stāvokli
                    
                    for i in range(0,4):
                        sub_categories[cat][i].grid(column=0, row=i, pady=10, padx=5)
        else:
            dropdownIndex = None
            for index, other_button in enumerate(categories):
                            other_button.config(state=NORMAL)# Iestata kategorijas pogas uz ieslēgto stāvokli
            for i in range(0,4):
                    sub_categories[cat][i].grid_forget()
            dropdown.place_forget()
            toggleDropdown=False
        
    #Front-End kategoriju pogu masīvs
    categories=[Button(navbar2, padx=20, text="Bizness", cursor="hand2", fg="white", bg="#2367d9", font=('MS Sans Serif', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(0)),
            Button(navbar2, padx=20, text="Izklaide", cursor="hand2", fg="white", bg="#2367d9", font=('MS Sans Serif', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(1)),
            Button(navbar2, padx=20, text="Vispārīgi", cursor="hand2", fg="white", bg="#2367d9", font=('MS Sans Serif', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(2)),
            Button(navbar2, padx=20, text="Veselība", cursor="hand2", fg="white", bg="#2367d9", font=('MS Sans Serif', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(3)),
            Button(navbar2, padx=20, text="Zinātne", cursor="hand2", fg="white", bg="#2367d9", font=('MS Sans Serif', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(4)),
            Button(navbar2, padx=20, text="Sports", cursor="hand2", fg="white", bg="#2367d9", font=('MS Sans Serif', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(5)),
            Button(navbar2, padx=20, text="Tehnoloģijas", cursor="hand2", fg="white", bg="#2367d9", font=('MS Sans Serif', 14), activeforeground="#123670", activebackground="#dedfe0", command=lambda:showDropdown(6))]
    #Filtrēšanas pogas iestatīšana un ielikšana logā, kas palaiž funkciju filterArticles un paceļ pogas uz priekšu un atpakaļ virspusē
    FilterBtn = Button(navbar2, cursor="hand2", text="⚙️", bg="#eee", font=('MS Sans Serif', 14), padx=25, activeforeground="#123670", activebackground="#dedfe0", command=lambda: [filterArticles(dropdownIndex, date_from_in, date_to_in, result, categories,article1),  nextBtn.tkraise(), backBtn.tkraise(), RefreshArticleBtn.tkraise()])
    FilterBtn.grid(column=9, row=0, pady=10, padx=10)

    #Artikulu atsvaidzināšanas pogas iestatīšana un ielikšana logā, kas palaiž funkciju randomArticles un loadArticles, kā arī paceļ pogas uz priekšu un atpakaļ, pašu atsvaidzināšanas pogu virspusē
    RefreshArticleBtn=Button(root, cursor="hand2", text="↻", bg="#2671eb", fg='black', foreground='white', width=5, height=1, font=('MS Sans Serif', 16), command=lambda: [randomArticles(), loadArticles(random.randint(0,99)), nextBtn.tkraise(), backBtn.tkraise(), RefreshArticleBtn.tkraise()])
    RefreshArticleBtn.place(x=25, y=655)

    date_from = Label(root, text="Datums no:", font=('MS Sans Serif', 10, 'bold'))# Datums no ievades norādes teksta iestatīšana un ielikšana logā
    date_from.pack()
    date_from_in = Entry(root, font=('MS Sans Serif', 10), bg='#dedede')# Datums no ievades iestatīšana un ielikšana logā
    date_from_in.pack()

    date_to = Label(root, text="Datums līdz:", font=('MS Sans Serif', 10, 'bold'))# Datums līdz ievades norādes teksta iestatīšana un ielikšana logā
    date_to.pack()
    date_to_in = Entry(root, font=('MS Sans Serif', 10), bg='#dedede')# Datums līdz ievades iestatīšana un ielikšana logā
    date_to_in.pack()

    result = Label(root, text="", font=('MS Sans Serif', 14))# Datuma ievades paziņojuma lauks, kas norāda vai datums ievadīts korekti
    result.pack(pady=10)
   

    #Funkcijas nodrošina placeholder datuma ievades logos, lai lietotājs saprastu formātu 
    def datefromin(event):# Datums no ievadei ievieto placeholder
        date_from_in.config(state=NORMAL)
        date_from_in.delete(0, END)
    
    date_from_in.insert(0, 'YYYY-MM-DD')
    date_from_in.config(state=DISABLED)
    date_from_in.bind("<Button-1>", datefromin)

    def datetoin(event):# Datums līdz ievadei ievieto placeholder
        date_to_in.config(state=NORMAL)
        date_to_in.delete(0, END)
    
    date_to_in.insert(0, 'YYYY-MM-DD')
    date_to_in.config(state=DISABLED)
    date_to_in.bind("<Button-1>", datetoin)

    # Maina atribūtus widget navbar2
    navbar2.grid_columnconfigure(0, weight=1, uniform="categories")
    navbar2.grid_columnconfigure(len(categories)+2, weight=1, uniform="categories")
   
    counter = 1 #Ieliek kategorijas pogas iekš navbar2 ar cikla palīdzību
    for category in categories:
        category.grid(column=counter + 1, row=0, pady=10, padx=10)
        navbar2.grid_columnconfigure(counter + 1, weight=1, uniform="categories")
        counter += 1 

    #Saglabāšanas saraksta pogas iestatīšana un ielikšana logā, poga palaiž funkciju openSavedList, kas atver saglabāšanas sarakstu
    savedList=Button(navbar2, cursor="hand2", bg='#eee', text="📃", font=('MS Sans Serif', 20), height=1, width=5, command= lambda: openSavedList())
    savedList.grid(column=0, row=0, pady=10, padx=10)

    content.place(x=0, y=500)
    loadArticles(article1)#Palaiž funkciju loadArticles, lai pārraidītu ekrānā atlasītās artikulas

    #Funkcija nodrošina šķirstīt artikulas ar pogu nextBtn
    def nextArticles():
        global article1
        if article1<=homeartLen-1:
            if article1 == 99:# Ja mainīgais pārsniedz 99, tad tas tiek pārmainīts ar vērtību 0
                article1 = 0
            else:# Ja nepārsniedz, tad tas tiek plusots ar 1
                article1=article1+1
            loadArticles(article1)# Palaiž funkciju, lai pārraidītu artikulu ar jauno artikulas indeksu
        else:
            article1=0

    #Funkcija nodrošina šķirstīt artikulas ar pogu backBtn
    def backArticles():
        global article1
        if article1<=homeartLen-1:
            if article1 == 0:# Ja mainīgais ir 0, tad tas tiek pārmainīts ar vērtību 99
                article1 = 99
            else:# Ja nepārsniedz, tad tas tiek atņemts ar 1
                article1=article1-1

            loadArticles(article1)# Palaiž funkciju, lai pārraidītu artikulu ar jauno artikulas indeksu
        else:
            article1=99

    # Tiek definētas pogas nextBtn un backBtn un ieliktas logā, lai varētu palaist funkcijas nextArticles un backArticles
    nextBtn=Button(root, text=">", fg="white", cursor="hand2", bg="#2367d9", font=('MS Sans Serif', 36, 'bold'), pady= 30, padx=20, activeforeground="#123670", activebackground="#dedfe0", command=lambda: nextArticles())
    backBtn=Button(root, text="<", fg="white", cursor="hand2", bg="#2367d9", font=('MS Sans Serif', 36, 'bold'), pady= 30, padx=20, activeforeground="#123670", activebackground="#dedfe0", command=lambda: backArticles())
    nextBtn.place(x=1160, y=430)
    backBtn.place(x=21, y=430)

    #Funkcija nodrošina atvērt saglabāšanas sarakstu
    def openSavedList():
        global savedListBox, toggleDropdown, savedBG # Globālie mainīgie, lai varētu tām piekļūt ārpus funkcijas
        savedArr = checkSavedTxt()
        savedBG = Frame(root, bg="#205fc7")
        savedBG.place(x=0, y=0, relwidth=1, relheight=1)  # Noliek augšējā kreisajā stūrī, kas arī aizņem visu ekrānu

        canvas = Canvas(savedBG, bg="#205fc7")# Canvas widget tiek definēts, lai dotu iespēju ar peles skrullīti iet cauri saglabātām artikulām
        canvas.pack(side='left', fill='both', expand=True)
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))  # Atļauj iet cauri saglabātām artikulām ar peles skrullīti

        savedListBox = Frame(canvas, bg="#205fc7") # Konteineris, kurā atrodās visi konteineri, kas saglabātā artikulu informāciju
        savedListBox.pack(side='left', fill='both', expand=True)

        # Poga savedExit ļauj lietotājam iziet no saglabāšanas saraksta palaižot savedExit funkciju
        savedExit = Button(savedListBox, cursor="hand2", bg='red', text="🡨", font=('MS Sans Serif', 20), fg="white",
                        height=1, width=5, command=lambda: [savedBG.place_forget(), SavedExit(savedExit)])
        savedExit.place(x=26.5, y=7.8)

        if len(savedArr) == 0:  # Ja saglabāto artiukulu skaits ir tukšs, ekrānā izvada, ka nav saglabātu artikulu
            noSavedLabel = Label(savedListBox, text="Saraksts ir tukšs :(", font=('MS Sans Serif', 12, 'bold'), fg="white",
                                bg="#205fc7")
            noSavedLabel.pack(pady=50)

        if len(savedArr) > 4:  # Ja ir saglabāto artikulu masīvs pārsniedz 4 indeksus ieslēdzas scrollbar, kas atļauj lietotājam apskatīt saglabātās artikulas ar peles skrullīti
            v_scrollbar = Scrollbar(savedListBox, orient='vertical', command=canvas.yview)
            v_scrollbar.pack(side='right', fill='y')
            canvas.configure(yscrollcommand=v_scrollbar.set)
            canvas.create_window((0, 0), window=savedListBox, anchor='nw')
            savedListBox.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))


        for index, obj in enumerate(savedArr): # Šis ir cikls, kas izprintē ekrānā saglabātās artikulas ekrānā, ciklā tiek piešķirti mainīgie, konteineris box kurā atrodas vienas saglabātās artikulas informācija
            box = Frame(savedListBox, bg="#2369db", cursor="hand2", borderwidth=2, relief='raised',
                        width=500)
            box.pack(ipadx=100, ipady=20, padx=220, pady=15, fill=BOTH, expand=True)
            box.bind("<Button-1>", lambda e, url=savedArr[index][2]: open_link(url))
            title = Label(box, text=savedArr[index][0], justify="left", font=('MS Sans Serif', 14, 'underline'), wraplength=700, bg="#2369db", fg='white')
            desc = Label(box, text=savedArr[index][1], justify="left", font=('MS Sans Serif', 10), wraplength=700, bg="#2369db", fg='white')
            deleteBtn = Button(box, text="-", bg="red", fg="white", font=('MS Sans Serif', 16, 'bold'), height=1, width=2, command=lambda url=savedArr[index][2]: [deleteArticle(url), reloadSavedList()])
            deleteBtn.place(x=780, y=25)
            title.pack(anchor=NW, pady=10, padx=30)
            title.bind("<Button-1>", lambda e, url=savedArr[index][2]: open_link(url))
            desc.pack(anchor=W, padx=30)
            desc.bind("<Button-1>", lambda e, url=savedArr[index][2]: open_link(url))

        # Šī ir funkcija, kas pārlāde saglabāšanas sarakstu(plānots, lai atjauninātu sarakstu katru reizi, kad izdzēš artikulu no saglabāšanas saraksta)
        def reloadSavedList():
            savedList.grid(column=0, row=0, pady=10, padx=10)
            savedListBox.place_forget()
            savedBG.place_forget()
            openSavedList() # Aizver visus widgets un pārlādē saglabāšanas sarakstu ar funckiju openSavedList

        #Šī ir funkcija, kas nodrošina saglabāšanas saraksta aizvēršanu, tā noņem visus saglabāšanas saraksta widgets un ieliek ekrānā atpakaļ sākuma ekrāna widgets
        def SavedExit(savedExit):
            
            # Saglabāšanas saraksta widgets aizvēršana:
            savedExit.destroy()
            savedList.grid(column=0, row=0, pady=10, padx=10)
            savedListBox.place_forget()
            savedBG.place_forget()

            # Sākuma ekrāna widgets ielikšana ekrānā:
            nextBtn.place(x=1160, y=430)
            backBtn.place(x=21, y=430)
            navbar2.pack(anchor=N, fill="both", pady=0, padx=0)
            loadArticles(article1)
    
    center(root)# Funkcijas palaišana, lai iecentrētu programmatūru ekrāna vidū
    root.mainloop()# Šī funkcija spēj ciklēt jeb palaist pašu programmatūru