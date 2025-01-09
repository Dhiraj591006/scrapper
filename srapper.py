# python -m pip install requests
# => get data drom web (html, json, xml)
# python -m pip install beautifulsoup3
# => parse html

# install git
# create repository in github

# go to git bash 
# git config --global user.name "Dhiraj591006"
#  git config --global user.gmail "dhirajdiwwana0031@gmail.com"


# git init 
# # git status => if you want to check what are the status of file
# git diff => if you want to check what are the changes
# git add .
# git commit -m "your message"
# git push origin => update the code 
# copy paste git from code

##################################
# 1. change the code
# 2. git add .
# 3. git commit -m "your message"
# 4. git push origin



import json

import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/"



def scrape_books(url):
    response = requests.get(url)
    print(response.status_code)
    if response.status_code !=200:
        print("Error")
        return
    
    #set encodind explicitly to handel special characters
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    all_books = []
    for book in books: 
        title = book.h3.a["title"] 
        price_text = book.find("p", class_="price_color").text
        currency = price_text[0]
        price = price_text[1:]
        formatted_book = {
            "title": title,
            "currency": currency,
            "price": price

        }                     
        all_books.append(formatted_book)


    return all_books 



scrape_books(URL)




books = scrape_books(URL)
with open("book.json", "w") as f:
    json.dump(books, f, indent=2)