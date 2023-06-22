# Importē moduļus, lai varētu izveidot programmatūru
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from datetime import timedelta
from PIL import Image,ImageTk
import random, webbrowser
import os.path
from newsapi import NewsApiClient
from tempfile import NamedTemporaryFile
import shutil
import os
import sys

#Funkcija domāta, lai palaistu programmu kā .exe failu ar ikonām
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

apikey = "f9e757ccd2bc4d07b56cd2a79f4509cc"# API atslēga, kas atļauj programmatūrai darboties ar NewsAPI 
#!!!ŠĪ IR BEZMAKSAS ATSLĒGA, TĀDĒĻ TIKAI VAR IK PĒC 24H IZMANTOT 100 PIEPRASĪJUMUS!!!
newsapi = NewsApiClient(api_key = apikey)# Šī ir mainīgā deklarēšana, lai varētu izvilkt artikulu informāciju no NewsAPI

from createWindow import root, dropdown, toggleDropdown,categories, date_from, date_to, article1 #No createWindow importē vajadzīgos mainīgos/funkcijas
global savedArr, homeart, homeartLen # Globālie mainīgie, lai pie tiem varētu piekļūt jeb kurš fails

#Tiek deklarēti tukši mainīgie, lai tos varētu atlasīt funkcijas
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
titles= []
articles = []
descriptions=[]
urls=[]
bCategories=["business", "entertainment", "general", "health", "science", "sports", "technology"] # Back-End kategoriju masīvs, lai ar tām varētu darboties NewsAPI
navbar1 = Frame(root, bg='#2671eb', height=200, width=1920)# Navbar1 deklarēšana, kurā atrodas MyNews logo
navbar2 = Frame(root, bg='#205fc7', height=50, width=1920)# Navbar2 deklarēšana, kurā atradīsies kategoriju pogas
logo = Label(navbar1, text="M   y   N   e   w   s", font=('MS Sans Serif', 28, 'bold'), bg='#174796', fg='white', pady=15, padx=200)
slogan = Label(navbar1, text="Tiec informēts ar MyNews!", font=('MS Sans Serif', 14), bg='#205fc7', fg='#fcfcfc', pady=9, padx=120)

#Funkcija pārbauda vai iepriekš ir jau izveidots saglabāšanas saraksta fails
def checkSavedTxt():
    global savedArr
    savedArr = []
    file_path = resource_path('savedList.txt')

    if not os.path.exists(file_path):# Ja neeksistē fails, tad to izveido
        with open(file_path, 'w') as file:
            print(f"Fails: {file_path} tika izveidots.")
            file.write("")

    else:# Ja fails eksistē, tad to nolasa un ieliek saglābāšanas saraksta masīvā
        print(f"Fails: {file_path} jau eksistē.")
        with open(file_path, 'r') as file:
            for line in file:# Cikls nolasa katru rindiņu un ieliek atbilstošo informāciju masīvā
                parts = line.strip().split('|')
                if len(parts) == 3:
                    title = parts[0].strip()
                    desc = parts[1].strip()
                    url = parts[2].strip()
                    savedArr.append([title, desc, url])
    return savedArr

#Šī funkcija nodrošina artikulu filtrēšanu
def filterArticles(dpIndex, date_from_in, date_to_in, result, categories, article1):
    article1=random.randint(0,99)
    for i, button in enumerate(categories):# Šis cikls liek visām kategorijas pogām ieslēgties tālakai darbībai
            button.configure(state=NORMAL)

    filterInterval(date_from_in, date_to_in, result) # Palaiž funkciju filterInterval, lai noskaidrotu vai lietotājs ir ievadījis intervāla informāciju

    date_from_in.delete(0,'end')# Datums no ievades lauka attīrīšana
    date_to_in.delete(0,'end')# Datums līdz ievades lauka attīrīšana
    toggleDropdown = False
    dropdown.place_forget()#Noņem dropdown widget no ekrāna

    # Deklarē tukšus mainīgos, lai ar tiem varētu darboties ciklos
    selected = []
    sub_cat = []
    catLen = 0

    if dpIndex != None: # Ja nodotās kategorijas dropdown indekss nēeksistē, tad veic tālāku filtrēšanas darbību
        
        #Pievieno visus checkbutton vērtības iekš selected masīva
        selected.append(var1.get())
        selected.append(var2.get())
        selected.append(var3.get())
        selected.append(var4.get())

        for i in range(0,4):# Cikls, kas ieliek atbilstošo sub-kategoriju sub_cat masīvā, ja selected[indekss] ir 1
           if selected[i] == 1:
              sub_cat.append(bSub_categories[dpIndex][i])
        #Pārmaina un deklarē vērtības
        catLen = len(sub_cat)# sub_cat masīva garums
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)

        if (date_from==None and date_to==None):# Pārbauda vai lietotājs ir pievienojis laika intervālu, ja lietotājs nav, tad laika intervāls automātiski ir mēneša laikā (NewsAPI spēj tikai atlasīt ziņas mēneša laikā)
            current_date = datetime.now().date()
            fromDat = current_date - timedelta(days=30)# 1 mēneša atlasīšana
            toDat = current_date # Šīdiena
            # No datetime uz string YYYY-MM-DD formātā
            noDat = fromDat.strftime('%Y-%m-%d')
            lidzDat = toDat.strftime('%Y-%m-%d')
        else: # Ja ir iestatīts, tad atbilstoši pārmaina vērtības tālākai darbībai
            noDat=date_from
            lidzDat=date_to

        match catLen: # Šeit ar switch palīdzību nodrošina, ja sub_cat masīva garums ir 1, tad ievada tikai vienu vērtību no sub_cat masīva tālākai atlasīšanas darbībai, ja masīva garums ir 2, tad ievada divas vērtības no masīva, u.t.t
          case 1:# Ja sub_cat garums  ir 1, tad nolasa artikulas tikai vienu sub_cat vērtību
              data = newsapi.get_everything(q=sub_cat[0], # Šī funkcija nolasa ziņas no NewsAPI
                                  from_param=noDat,
                                  to=lidzDat,
                                  language='en',
                                  sort_by='relevancy')
              homeart = data['articles'] # Šis masīvs tiek deklarēts, lai ievietotu artikulas no NewsAPI saņemtās informācijas

              #Šie trīs cikli ir domāti, lai noņemtu visus iepriekšējo artikulu informāciju
              for article in articles:
                article.pack_forget()
              for title in titles:
                title.place_forget()
              for description in descriptions:
                description.place_forget()
              
              # Šis cikls pievieno visu atlasīto artikulu informāciju četros masīvos
              for i, article in enumerate(homeart):
                urls.insert(i, article["url"])#Pievieno URL, lai varētu artikulus atvērt pārlūkā
                articles.insert(i, (Label(root, width=1000, height=250, bg="#205fc7", cursor="hand2")))
                articles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url)) # Pievieno iespēju atvērt artikulu pārlūkprogrammā spiežot peles klikšķi
                titles.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 14, "underline"), bg="#205fc7", fg="white", text=article["title"])))
                titles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))# Pievieno iespēju atvērt artikulu pārlūkprogrammā spiežot peles klikšķi
                descriptions.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 13), bg="#205fc7", fg="white", text=article["description"])))

            # Palaiž funkciju, lai varētu ielādēt jaunās artikulas uz ekrāna
              loadArticles(article1) 

          case 2:# Ja sub_cat garums  ir 2, tad nolasa artikulas divas sub_cat vērtības
              data = newsapi.get_everything(q=sub_cat[0]+" "+sub_cat[1], # Šī funkcija nolasa ziņas no NewsAPI
                                  from_param=noDat,
                                  to=lidzDat,
                                  language='en',
                                  sort_by='relevancy')
              homeart = data['articles'] # Šis masīvs tiek deklarēts, lai ievietotu artikulas no NewsAPI saņemtās informācijas

             #Šie trīs cikli ir domāti, lai noņemtu visus iepriekšējo artikulu informāciju
              for article in articles:
                article.pack_forget()
              for title in titles:
                title.place_forget()
              for description in descriptions:
                description.place_forget()
              
            # Šis cikls pievieno visu atlasīto artikulu informāciju četros masīvos
              for i, article in enumerate(homeart):
                urls.insert(i, article["url"])#Pievieno URL, lai varētu artikulus atvērt pārlūkā
                articles.insert(i, (Label(root, width=1000, height=250, bg="#205fc7", cursor="hand2")))
                articles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))# Pievieno iespēju atvērt artikulu pārlūkprogrammā spiežot peles klikšķi
                titles.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 14, "underline"), bg="#205fc7", fg="white", text=article["title"])))
                titles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))# Pievieno iespēju atvērt artikulu pārlūkprogrammā spiežot peles klikšķi
                descriptions.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 13), bg="#205fc7", fg="white", text=article["description"])))

            # Palaiž funkciju, lai varētu ielādēt jaunās artikulas uz ekrāna
              loadArticles(article1) 

          case 3:# Ja sub_cat garums  ir 3, tad nolasa artikulas trīs sub_cat vērtības
              data = newsapi.get_everything(q=sub_cat[0]+" "+sub_cat[1]+" "+sub_cat[2],# Šī funkcija nolasa ziņas no NewsAPI
                                  from_param=noDat,
                                  to=from_date,
                                  language='en',
                                  sort_by='relevancy')
              homeart = data['articles']# Šis masīvs tiek deklarēts, lai ievietotu artikulas no NewsAPI saņemtās informācijas

            #Šie trīs cikli ir domāti, lai noņemtu visus iepriekšējo artikulu informāciju
              for article in articles:
                article.pack_forget()
              for title in titles:
                title.place_forget()
              for description in descriptions:
                description.place_forget()
              
             # Šis cikls pievieno visu atlasīto artikulu informāciju četros masīvos
              for i, article in enumerate(homeart):
                urls.insert(i, article["url"])#Pievieno URL, lai varētu artikulus atvērt pārlūkā
                articles.insert(i, (Label(root, width=1000, height=250, bg="#205fc7", cursor="hand2")))
                articles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))# Pievieno iespēju atvērt artikulu pārlūkprogrammā spiežot peles klikšķi
                titles.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 14, "underline"), bg="#205fc7", fg="white", text=article["title"])))
                titles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))# Pievieno iespēju atvērt artikulu pārlūkprogrammā spiežot peles klikšķi
                descriptions.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 13), bg="#205fc7", fg="white", text=article["description"])))

            # Palaiž funkciju, lai varētu ielādēt jaunās artikulas uz ekrāna
              loadArticles(article1) 

          case 4:# Ja sub_cat garums  ir 4, tad nolasa artikulas četras sub_cat vērtības
              data = newsapi.get_everything(q=sub_cat[0]+" "+sub_cat[1]+" "+sub_cat[2]+" "+sub_cat[3],# Šī funkcija nolasa ziņas no NewsAPI
                                  from_param=noDat,
                                  to=lidzDat,
                                  language='en',
                                  sort_by='relevancy')
              homeart = data['articles']# Šis masīvs tiek deklarēts, lai ievietotu artikulas no NewsAPI saņemtās informācijas

            #Šie trīs cikli ir domāti, lai noņemtu visus iepriekšējo artikulu informāciju
              for article in articles:
                article.pack_forget()
              for title in titles:
                title.place_forget()
              for description in descriptions:
                description.place_forget()
              
            # Šis cikls pievieno visu atlasīto artikulu informāciju četros masīvos
              for i, article in enumerate(homeart):
                urls.insert(i, article["url"])#Pievieno URL, lai varētu artikulus atvērt pārlūkā
                articles.insert(i, (Label(root, width=1000, height=250, bg="#205fc7", cursor="hand2")))
                articles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))# Pievieno iespēju atvērt artikulu pārlūkprogrammā spiežot peles klikšķi
                titles.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 14, "underline"), bg="#205fc7", fg="white", text=article["title"])))
                titles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))# Pievieno iespēju atvērt artikulu pārlūkprogrammā spiežot peles klikšķi
                descriptions.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 13), bg="#205fc7", fg="white", text=article["description"])))

           # Palaiž funkciju, lai varētu ielādēt jaunās artikulas uz ekrāna
              loadArticles(article1)
              return article1
            
#Funkcija nodrošina vai lietotājs ir ievadījis laika intervālu, atbilstoši situācijai norāda paziņojumu            
def filterInterval(date_from_in, date_to_in, result):
    global date_from, date_to # Globālie mainīgie, lai ar tiem varētu darboties ārpus funkcijas

    date_from = date_from_in.get()# Iegūst Entry widget vērtību un ieliek to vērtībās
    date_to = date_to_in.get()# Iegūst Entry widget vērtību un ieliek to vērtībās

    #Šeit notiek pārbaude vai ievades lauks ir bijis tukšs, ja ir bijis tukšs, tad deklarē intervālu mēneša intervālā no šodienas
    if(((date_from=="YYYY-MM-DD" and date_to=="YYYY-MM-DD") or (date_from=="YYYY-MM-DD" or date_to=="YYYY-MM-DD")) or ((date_from=="" and date_to=="") or (date_from=="" or date_to==""))):
        result.config(text="Tiek pārraidīts mēneša intervāls")
        date_from=None
        date_to=None
        return date_from, date_to
    
    try:# Pārbauda vai ir pareizs datuma formāts ar try catch principu
      date_from_obj = datetime.strptime(date_from, "%Y-%m-%d")# Deklarē datuma ievadi, kā date mainīgo
      date_to_obj = datetime.strptime(date_to, "%Y-%m-%d")

    except ValueError:# Nepareizā formāta situācija
      result.config(text="Datuma formāts ir nekorekts!", relief='raised')
      date_from=None
      date_to=None
      return date_from, date_to

      # Iegūst šodienas datumu un aprēķina mazāko iespējamo datumu (mēneša intervāls)
    current_date = datetime.now()
    min_date = current_date - timedelta(days=30)

    if date_from_obj > current_date: # Ja datums no ir vēlāks nekā šodiena, tad izvada paziņojumu, ka datums nedrīkst būt nākotnē
        result.config(text="Datums nedrīkst būt nākotnē!", relief='raised')
        date_from=None
        date_to=None
        return
    elif date_to_obj > current_date:# Ja datums līdz ir vēlāks nekā šodiena, tad izvada paziņojumu, ka datums nedrīkst būt nākotnē
        result.config(text="Datums nedrīkst būt nākotnē!", relief='raised')
        date_from=None
        date_to=None
        return
    elif date_from_obj > date_to_obj:# Ja datums no ir lielāks nekā datums līdz, tad izvada paziņojumu, ka 'datums no' nedrīkst būt vēlāks nekā 'Datums līdz'
        result.config(text="'Datums no' nedrīkst būt vēlāks nekā 'Datums līdz'!", relief='raised')
        date_from=None
        date_to=None
        return
    elif date_from_obj < min_date:# Ja datums neiekļaujas 30 dienu intervālā, tad izvada paziņojumu, ka datumam jāiekļaujas 30 dienās
        result.config(text="Datumam jāiekļaujas 30 dienās!", relief='raised')
        date_from=None
        date_to=None
        return
    else:
      result.config(text=date_from+"  -  "+date_to, relief='raised')

# Funkcija nodrošina saglabāt artikulu saglabāšanas sarakstā
def saveArticle(title, desc, url):
    savedArr = checkSavedTxt() # Nolasa vai saglabāšanas saraksta fails eksistē un nolasa visas vērtības un atbilstoši ieliek mainīgajā savedArr

    for index, row in enumerate(savedArr): #Cikls pārbauda vai netiek saglabāts dublikāts, ja URL jau eksistē failā, neļauj saglabāt un izmet kļūdu
        if row[2] == url:
            messagebox.showerror("Kļūda!", "Dublikātus saglabāt nav iespējams :(")
            return
    
    with open(resource_path("savedList.txt"), "a") as file: # Ja nav atrasti dublikāti, ieraksta saglabāšanas saraksta failā vēlamo artikulu
        file.write(title + " | " + desc + " | " + url + "\n")
        
#Funkcija nodrošina izdzēst saglabāto artikulu no saglabāšanas saraksta
def deleteArticle(delUrl):
    # Izveido atsevišķu failu
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        with open(resource_path("savedList.txt"), "r") as fp:
            for line in fp:
                # Pārbauda vai līnijā pastāv jau tāds URL
                if delUrl not in line:
                    temp_file.write(line)

    # Pārmaina oriģinālo failu un atsevišķo failu
    shutil.move(temp_file.name, resource_path("savedList.txt"))
  
  #Funkcija nodrošina ielādēt artikulas uz ekrāna
def loadArticles(article1):
  for  i, article in enumerate(homeart):
    articles[i].pack_forget() #Cikls noņem no ekrāna iepriekšējo artikulu

  # Ievieto nākošās vai jaunās artikulas informaciju ekrānā
  saveBtn1 = Button(root, text="💾", fg="black", bg="white", font=('MS Sans Serif', 16), width=20, height=1, command=lambda: saveArticle(titles[article1].cget("text"), descriptions[article1].cget("text"), urls[article1]))
  articles[article1].pack(pady=10)
  titles[article1].place(x=160, y=40)
  descriptions[article1].place(x=160, y=85)
  saveBtn1.place(x=550, y=655)

#Deklarē dažādus mainīgos
content = Frame(root, width=1920, height=1000, padx=1920, bg="#eee")# Konteineris, kas uztur visus widgets
# 2D masīvs, kas uztur visas sub-kategorijas Front-End, lai tos varētu ekrāna redzēt un ieķeksēt tālākai filtrēšanai
sub_categories=[[Checkbutton(dropdown, text="Finanses", variable=var1), Checkbutton(dropdown, text="Marketings", variable=var2), Checkbutton(dropdown, text="Menedžments",variable=var3), Checkbutton(dropdown, text="E-komercija", variable=var4)],
                [Checkbutton(dropdown, text="Filmas", variable=var1), Checkbutton(dropdown, text="Mūzika", variable=var2), Checkbutton(dropdown, text="Notikumi", variable=var3), Checkbutton(dropdown, text="Spēles", variable=var4)],
                [Checkbutton(dropdown, text="Laikapstākļi", variable=var1), Checkbutton(dropdown, text="Politika", variable=var2), Checkbutton(dropdown, text="Dzīvesstils", variable=var3), Checkbutton(dropdown, text="Izglītība", variable=var4)],
                [Checkbutton(dropdown, text="Fitness", variable=var1), Checkbutton(dropdown, text="Mentālā veselība", variable=var2), Checkbutton(dropdown, text="Uzturs", variable=var3), Checkbutton(dropdown, text="Attīstība", variable=var4)],
                [Checkbutton(dropdown, text="Fizika", variable=var1), Checkbutton(dropdown, text="Astronomija", variable=var2), Checkbutton(dropdown, text="Bioloģija", variable=var3), Checkbutton(dropdown, text="Medicīna", variable=var4)],
                [Checkbutton(dropdown, text="Futbols", variable=var1), Checkbutton(dropdown, text="Basketbols", variable=var2), Checkbutton(dropdown, text="Golfs", variable=var3), Checkbutton(dropdown, text="Izlase", variable=var4)],
                [Checkbutton(dropdown, text="AI", variable=var1), Checkbutton(dropdown, text="Kiberdrošība", variable=var2), Checkbutton(dropdown, text="Spēļu tehnoloģija", variable=var3), Checkbutton(dropdown, text="VR", variable=var4)]]
# 2D masīvs, kas uztur visas sub-kategorijas Back-End, lai ar tiem varētu darboties filtrēšanā ar MyNews
bSub_categories=[["Finance", "Marketing", "Management", "E-commerce"],
                ["Movie", "Music", "Event", "Gaming"],
                ["Weather", "Politics", "Lifestyle", "Education"],
                ["Fitness", "Mental health", "Nutrition", "Development"],
                ["Physics", "Astronomy", "Biology", "Medicine science"],
                ["Football", "Basketball", "Golf", "Team"],
                ["Artificial intelligence", "Cybersecurity", "Gaming technology", "Virtual reality"]]

#Šī funkcija nodrošina atvērt URL pārlūkprogramma ar webbrowser moduļa palīdzību
def open_link(url):
    webbrowser.open_new(url)

#Šeit tiek deklarēti mainīgie, kurā atrodas mēneša intervāla informācija
current_date = datetime.now().date()
from_date = current_date - timedelta(days=30)
to_date = current_date

# Pārveido date objektus uz string YYYY-MM-DD formātā
from_param = from_date.strftime('%Y-%m-%d')
to = to_date.strftime('%Y-%m-%d')

#Funkcija nodrošina artikulu atlasīšanu nejaušā secībā
def randomArticles():
    global homeart, homeartLen
    catRan=random.randint(0, 6)# Izveido nejaušu skaitli [0;6], atbilstoši 7 kategorijām

    #Šie trīs cikli ir domāti, lai noņemtu visus iepriekšējo artikulu informāciju
    for article in articles:
        article.pack_forget()
    for title in titles:
        title.place_forget()
    for description in descriptions:
        description.place_forget()

    # Šī funkcija nolasa ziņas no NewsAPI, taču keyword ir nejaušs indekss no 7 kategorijā
    homeData = newsapi.get_everything(
        q=bCategories[catRan],
        from_param=from_param,
        to=to,
        language='en',
        sort_by='relevancy'
    )

    homeart = homeData['articles'] # Ieliek masīvā tikko atlasīto artikulu informāciju no NewsAPI
    homeartLen=homeData['totalResults'] # Nolasa atlasīto artikulu skaitu

    for  i, article in enumerate(homeart):# Cikls nodrošina jauno artikulu ievietošanu četros masīvos
        urls.insert(i,article["url"])#Pievieno URL, lai varētu artikulus atvērt pārlūkā
        articles.insert(i,(Label(root, width=1000, height=250, bg="#205fc7", cursor="hand2")))
        articles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))# Pievieno iespēju atvērt artikulu pārlūkprogrammā spiežot peles klikšķi
        titles.insert(i,(Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 14, "underline"), bg="#205fc7", fg="white",text=article["title"])))
        titles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))# Pievieno iespēju atvērt artikulu pārlūkprogrammā spiežot peles klikšķi
        descriptions.insert(i,(Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 13), bg="#205fc7", fg="white", text=article["description"])))

randomArticles()# Palaiž funkciju randomArticles, kad programmatūra tiek startēta