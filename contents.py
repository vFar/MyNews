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

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

apikey = "8451a189a10f47e3a7b4f02d6624be3f"
newsapi = NewsApiClient(api_key = apikey)

from createWindow import root, dropdown, toggleDropdown,categories, date_from, date_to
global articles, savedArr, homeart, homeartLen
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
titles= []
articles = []
descriptions=[]
urls=[]
bCategories=["business", "entertainment", "general", "health", "science", "sports", "technology"]
navbar1 = Frame(root, bg='#2671eb', height=200, width=1920)
navbar2 = Frame(root, bg='#205fc7', height=50, width=1920)

logo = Label(navbar1, text="M   y   N   e   w   s", font=('MS Sans Serif', 28, 'bold'), bg='#174796', fg='white', pady=15, padx=200)
slogan = Label(navbar1, text="Tiec informēts ar MyNews!", font=('MS Sans Serif', 14), bg='#205fc7', fg='#fcfcfc', pady=9, padx=120)




def checkSavedTxt():
    global savedArr
    savedArr = []
    file_path = resource_path('savedList.txt')

    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            print(f"The file {file_path} was created.")
            file.write("tituls | apraksts | url\n")

    else:
        print(f"The file {file_path} already exists.")
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 3:
                    title = parts[0].strip()
                    desc = parts[1].strip()
                    url = parts[2].strip()
                    savedArr.append([title, desc, url])
    return savedArr



def filterArticles(dpIndex, date_from_in, date_to_in, result):
    for index, other_button in enumerate(categories):
                        if index != 0:
                            other_button.config(state=NORMAL)
    filterInterval(date_from_in, date_to_in, result)
    date_from_in.delete(0,'end')
    date_to_in.delete(0,'end')
    toggleDropdown = False
    dropdown.place_forget()
    selected = []
    sub_cat = []
    catLen = 0
    if dpIndex != None:
        selected.append(var1.get())
        selected.append(var2.get())
        selected.append(var3.get())
        selected.append(var4.get())
        for i in range(0,4):
           if selected[i] == 1:
              sub_cat.append(bSub_categories[dpIndex][i])
        print(catLen, "harr")
        catLen = len(sub_cat)
        print(catLen)
        print(len(sub_cat))
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        print(from_date, " ", to_date)
        if (date_from==None and date_to==None):
            print("Datums nav")
            current_date = datetime.now().date()
            fromDat = current_date - timedelta(days=28)
            toDat = current_date
            noDat = fromDat.strftime('%Y-%m-%d')
            lidzDat = toDat.strftime('%Y-%m-%d')
        else:
            noDat=date_from
            lidzDat=date_to
            print(noDat, " ", lidzDat)
        match catLen:
        
          case 1:
              print(bCategories[dpIndex])  
              data = newsapi.get_everything(q=sub_cat[0],
                                  from_param=noDat,
                                  to=lidzDat,
                                  language='en',
                                  sort_by='relevancy')
              homeart = data['articles']

            # Clear existing articles, titles, and descriptions
              for article in articles:
                article.pack_forget()
              for title in titles:
                title.place_forget()
              for description in descriptions:
                description.place_forget()
              
            # Create new articles, titles, and descriptions based on the updated data
              for i, article in enumerate(homeart):
                urls.insert(i, article["url"])
                articles.insert(i, (Label(root, width=1000, height=250, bg="#205fc7", cursor="hand2")))
                articles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))
                titles.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 14, "underline"), bg="#205fc7", fg="white", text=article["title"])))
                titles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))
                descriptions.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 13), bg="#205fc7", fg="white", text=article["description"])))

            # Load and display the updated articles
              loadArticles(random.randint(0,99)) 

          case 2:
              print(bCategories[dpIndex])  
              data = newsapi.get_everything(q=sub_cat[0]+" "+sub_cat[1],
                                  from_param=noDat,
                                  to=lidzDat,
                                  language='en',
                                  sort_by='relevancy')
              homeart = data['articles']
              print(homeart)

            # Clear existing articles, titles, and descriptions
              for article in articles:
                article.pack_forget()
              for title in titles:
                title.place_forget()
              for description in descriptions:
                description.place_forget()
              
            # Create new articles, titles, and descriptions based on the updated data
              for i, article in enumerate(homeart):
                urls.insert(i, article["url"])
                articles.insert(i, (Label(root, width=1000, height=250, bg="#205fc7", cursor="hand2")))
                articles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))
                titles.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 14, "underline"), bg="#205fc7", fg="white", text=article["title"])))
                titles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))
                descriptions.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 13), bg="#205fc7", fg="white", text=article["description"])))

            # Load and display the updated articles
              loadArticles(random.randint(0,99)) 
          case 3:
              print(bCategories[dpIndex])  
              data = newsapi.get_everything(q=sub_cat[0]+" "+sub_cat[1]+" "+sub_cat[2],
                                  from_param=noDat,
                                  to=from_date,
                                  language='en',
                                  sort_by='relevancy')
              homeart = data['articles']
              print(homeart)

            # Clear existing articles, titles, and descriptions
              for article in articles:
                article.pack_forget()
              for title in titles:
                title.place_forget()
              for description in descriptions:
                description.place_forget()
              
            # Create new articles, titles, and descriptions based on the updated data
              for i, article in enumerate(homeart):
                urls.insert(i, article["url"])
                articles.insert(i, (Label(root, width=1000, height=250, bg="#205fc7", cursor="hand2")))
                articles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))
                titles.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 14, "underline"), bg="#205fc7", fg="white", text=article["title"])))
                titles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))
                descriptions.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 13), bg="#205fc7", fg="white", text=article["description"])))

            # Load and display the updated articles
              loadArticles(random.randint(0,99)) 

          case 4:
              print(bCategories[dpIndex])  
              data = newsapi.get_everything(q=sub_cat[0]+" "+sub_cat[1]+" "+sub_cat[2]+" "+sub_cat[3],
                                  from_param=noDat,
                                  to=lidzDat,
                                  language='en',
                                  sort_by='relevancy')
              homeart = data['articles']
              print(homeart)

            # Clear existing articles, titles, and descriptions
              for article in articles:
                article.pack_forget()
              for title in titles:
                title.place_forget()
              for description in descriptions:
                description.place_forget()
              
            # Create new articles, titles, and descriptions based on the updated data
              for i, article in enumerate(homeart):
                urls.insert(i, article["url"])
                articles.insert(i, (Label(root, width=1000, height=250, bg="#205fc7", cursor="hand2")))
                articles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))
                titles.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 14, "underline"), bg="#205fc7", fg="white", text=article["title"])))
                titles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))
                descriptions.insert(i, (Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 13), bg="#205fc7", fg="white", text=article["description"])))

            # Load and display the updated articles
              loadArticles(random.randint(0,99)) 
            

    
def filterInterval(date_from_in, date_to_in, result):
    global date_from, date_to

    date_from = date_from_in.get()
    date_to = date_to_in.get()
    print(date_from," uwu", date_to)
    if(((date_from=="YYYY-MM-DD" and date_to=="YYYY-MM-DD") or (date_from=="YYYY-MM-DD" or date_to=="YYYY-MM-DD")) or ((date_from=="" and date_to=="") or (date_from=="" or date_to==""))):
        result.config(text="Tiek pārraidīts mēneša intervāls")
        date_from=None
        date_to=None
        return date_from, date_to
    try:
      date_from_obj = datetime.strptime(date_from, "%Y-%m-%d")
      date_to_obj = datetime.strptime(date_to, "%Y-%m-%d")

    except ValueError:

      result.config(text=fromDat.strftime('%Y-%m-%d')+"  -  "+toDat.strftime('%Y-%m-%d'), relief='raised')
      date_from=None
      date_to=None

      # Calculate the difference in days
    date_diff = (date_to_obj - date_from_obj).days
    current_date = datetime.now()
    min_date = current_date - timedelta(days=30)

    if date_from_obj > current_date:
        result.config(text="Datums nedrīkst būt nākotnē!", relief='raised')
        date_from=None
        date_to=None
        return
    elif date_to_obj > current_date:
        result.config(text="Datums nedrīkst būt nākotnē!", relief='raised')
        date_from=None
        date_to=None
        return
    elif date_from_obj > date_to_obj:
        result.config(text="Datuma formāts ir nekorekts!", relief='raised')
        date_from=None
        date_to=None
        return
    elif date_from_obj < min_date:
        result.config(text="Datumam jāiekļaujas 30 dienās!", relief='raised')
        date_from=None
        date_to=None
        return
    else:
          result.config(text=date_from+"  -  "+date_to, relief='raised')

def saveArticle(title, desc, url):
    savedArr = checkSavedTxt()
    print(title)
    for index, row in enumerate(savedArr):
        if row[2] == url:
            messagebox.showerror("Kļūda!", "Dublikātus saglabāt nav iespējams :(")
            return
    
    with open(resource_path("savedList.txt"), "a") as file:
        file.write(title + " | " + desc + " | " + url + "\n")
        


def deleteArticle(delUrl):
    print(delUrl," dele")
    # Create a temporary file
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        with open(resource_path("savedList.txt"), "r") as fp:
            for line in fp:
                # Check if the line contains the given URL
                if delUrl not in line:
                    temp_file.write(line)

    # Replace the original file with the temporary file
    shutil.move(temp_file.name, resource_path("savedList.txt"))
  



def loadArticles(article1):

  for  i, article in enumerate(homeart):
    articles[i].pack_forget()
  print(titles[article1].cget("text"))
  saveBtn1 = Button(root, text="💾", fg="black", bg="white", font=('MS Sans Serif', 16), width=20, height=1, command=lambda: saveArticle(titles[article1].cget("text"), descriptions[article1].cget("text"), urls[article1]))

  articles[article1].pack(pady=10)
  titles[article1].place(x=160, y=40)
  descriptions[article1].place(x=160, y=85)
  
  saveBtn1.place(x=550, y=655)

  print(article1)

         

content = Frame(root, width=1920, height=1000, padx=1920, bg="#eee")
sub_categories=[[Checkbutton(dropdown, text="Finanses", variable=var1), Checkbutton(dropdown, text="Marketings", variable=var2), Checkbutton(dropdown, text="Menedžments",variable=var3), Checkbutton(dropdown, text="E-komercija", variable=var4)],
                [Checkbutton(dropdown, text="Filmas", variable=var1), Checkbutton(dropdown, text="Mūzika", variable=var2), Checkbutton(dropdown, text="Notikumi", variable=var3), Checkbutton(dropdown, text="Spēles", variable=var4)],
                [Checkbutton(dropdown, text="Laikapstākļi", variable=var1), Checkbutton(dropdown, text="Politika", variable=var2), Checkbutton(dropdown, text="Dzīvesstils", variable=var3), Checkbutton(dropdown, text="Izglītība", variable=var4)],
                [Checkbutton(dropdown, text="Fitness", variable=var1), Checkbutton(dropdown, text="Mentālā veselība", variable=var2), Checkbutton(dropdown, text="Uzturs", variable=var3), Checkbutton(dropdown, text="Attīstība", variable=var4)],
                [Checkbutton(dropdown, text="Fizika", variable=var1), Checkbutton(dropdown, text="Astronomija", variable=var2), Checkbutton(dropdown, text="Bioloģija", variable=var3), Checkbutton(dropdown, text="Medicīna", variable=var4)],
                 [Checkbutton(dropdown, text="Futbols", variable=var1), Checkbutton(dropdown, text="Basketbols", variable=var2), Checkbutton(dropdown, text="Golfs", variable=var3), Checkbutton(dropdown, text="Izlase", variable=var4)],
                [Checkbutton(dropdown, text="AI", variable=var1), Checkbutton(dropdown, text="Kiberdrošība", variable=var2), Checkbutton(dropdown, text="Spēļu tehnoloģija", variable=var3), Checkbutton(dropdown, text="VR", variable=var4)]]
bSub_categories=[["Finance", "Marketing", "Management", "E-commerce"],
                ["Movie", "Music", "Event", "Gaming"],
                ["Weather", "Politics", "Lifestyle", "Education"],
                ["Fitness", "Mental health", "Nutrition", "Development"],
                ["Physics", "Astronomy", "Biology", "Medicine science"],
                ["Football", "Basketball", "Golf", "Team"],
                ["Artificial intelligence", "Cybersecurity", "Gaming technology", "Virtual reality"]]


def open_link(url):
    webbrowser.open_new(url)

current_date = datetime.now().date()
from_date = current_date - timedelta(days=28)
to_date = current_date

# Convert the date objects to strings in the required format
from_param = from_date.strftime('%Y-%m-%d')
to = to_date.strftime('%Y-%m-%d')

catRan=random.randint(0, 6)


def randomArticles():
    for article in articles:
        article.pack_forget()
    for title in titles:
        title.place_forget()
    for description in descriptions:
        description.place_forget()

    global homeart, homeartLen
    # Make the API request with the updated date range
    homeData = newsapi.get_everything(
        q=bCategories[catRan],
        from_param=from_param,
        to=to,
        language='en',
        sort_by='relevancy'
    )

    homeart = homeData['articles']
    homeartLen=homeData['totalResults']


    for  i, article in enumerate(homeart):
        urls.insert(i,article["url"])
        articles.insert(i,(Label(root, width=1000, height=250, bg="#205fc7", cursor="hand2")))
        articles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))
        titles.insert(i,(Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 14, "underline"), bg="#205fc7", fg="white",text=article["title"])))
        titles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))
        descriptions.insert(i,(Label(articles[i], justify="left", wraplength=970, font=('MS Sans Serif', 13), bg="#205fc7", fg="white", text=article["description"])))
randomArticles()
    

  