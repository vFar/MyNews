from tkinter import *
from tkinter import messagebox
import datetime
from PIL import Image,ImageTk
import random, webbrowser
import os.path
from newsapi import NewsApiClient
apikey = "8451a189a10f47e3a7b4f02d6624be3f"
newsapi = NewsApiClient(api_key = apikey)

from createWindow import root, dropdown, toggleDropdown,categories
global articles, savedArr
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

bCategories=["business", "entertainment", "general", "health", "science", "sports", "technology"]
navbar1 = Frame(root, bg='#2671eb', height=200, width=1920)
navbar2 = Frame(root, bg='#205fc7', height=50, width=1920)

logo = Label(navbar1, text="M   y   N   e   w   s", font=('Calibri', 28, 'bold'), bg='#174796', fg='white', pady=15, padx=200)
slogan = Label(navbar1, text="Tiec informēts ar MyNews!", font=('Calibri', 14, 'italic'), bg='#205fc7', fg='#fcfcfc', pady=10, padx=120)


def checkSavedTxt():
    global savedArr
    savedArr = []
    file_path = 'files/savedList.txt'

    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            print(f"The file {file_path} was created.")

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



def filterArticles(dpIndex):
    for index, other_button in enumerate(categories):
                        if index != 0:
                            other_button.config(state=NORMAL)

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
        print(selected)
        for i in range(0,4):
           if selected[i] == 1:
              sub_cat.append(bSub_categories[dpIndex][i])
        
        catLen = len(sub_cat)
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        match catLen:
        
          case 1:
              print(bCategories[dpIndex])  
              data = newsapi.get_everything(q=sub_cat[0],
                               category=bCategories[dpIndex],
                               from_param='2023-03-15',
                               to='2023-04-05',
                               language='en',
                               sort_by='relevancy')
              articles = data['articles']
              for x, y in enumerate(articles):
                  print(f'{x}  {y["title"]}')
        print(len(sub_cat))      
    else:
        print("Error")
    
def saveArticle(title, desc, url):
    newSave=title," | ",desc," | ",url
    for index, row in enumerate(savedArr):
        if (savedArr[index][2]!=url):
            with open("savedList.txt", "a") as file:
                file.write(newSave + "\n")
        else:
            messagebox.showerror("Error", "Article is already duplicated.")


def loadArticles(article1, article2):
  print(f"{article1} load")

  for  i, article in enumerate(homeart):
    articles[i].pack_forget()

  saveBtn1 = Button(articles[article1], text="save", fg="black", bg="white", command=lambda: saveArticle(homeart[article1]['title'], homeart[article1]['description'], homeart[article1]['url']))
  saveBtn2 = Button(articles[article2], text="save", fg="black", bg="white", command=lambda: saveArticle(homeart[article1]['title'], homeart[article1]['description'], homeart[article1]['url']))

  articles[article1].pack(pady=84)
  titles[article1].place(x=25, y=25)
  descriptions[article1].place(x=25, y=70)
  saveBtn1.place(x=900, y=150)


  articles[article2].pack(pady=30)
  titles[article2].place(x=25, y=25)
  descriptions[article2].place(x=25, y=70)
  saveBtn2.place(x=900, y=150)
         

content = Frame(root, width=1920, height=1000, padx=1920, bg="white")
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
titles= []
articles = []
descriptions=[]
urls=[]

def open_link(url):
    webbrowser.open_new(url)

current_date = datetime.date.today()
from_date = current_date - datetime.timedelta(days=28)
to_date = current_date

# Convert the date objects to strings in the required format
from_param = from_date.strftime('%Y-%m-%d')
to = to_date.strftime('%Y-%m-%d')

catRan=random.randint(0, 6)
print(catRan," cum")

# Make the API request with the updated date range
homeData = newsapi.get_everything(
    q=bCategories[catRan],
    sources='bbc-news, the-verge',
    from_param=from_param,
    to=to,
    language='en',
    sort_by='relevancy'
)

homeart = homeData['articles']
homeartLen=homeData['totalResults']
print(homeartLen)


for  i, article in enumerate(homeart):
    urls.insert(i,article["url"])
    articles.insert(i,(Label(root, width=1000, height=250, bg="#205fc7", cursor="hand2")))
    articles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))
    titles.insert(i,(Label(articles[i], justify="left", wraplength=970, font=('Calibri', 14, "underline"), bg="#205fc7", fg="white",text=article["title"])))
    titles[i].bind("<Button-1>", lambda e, url=urls[i]: open_link(url))
    descriptions.insert(i,(Label(articles[i], justify="left", wraplength=970, font=('Calibri', 13), bg="#205fc7", fg="white", text=article["description"])))
    

  