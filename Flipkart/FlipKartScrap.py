import requests
import pandas as pd
from bs4 import BeautifulSoup
product_name = []
price = []
description = []
ratings = []

""" for i in range(2,10):
    url="https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page="+str(i)
    r=requests.get(url)

    soup=BeautifulSoup(r.text,"lxml")

    nextpage=soup.find("a",class_="_1LKTO3").get("href")
    complete_nextpage="https://www.flipkart.com"+nextpage
    print(complete_nextpage)     """

# We will be extracting data from  10 pages only hence given 2 to 10
for j in range(2, 10):
 url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page=" + str(j)
 r = requests.get(url)

 soup = BeautifulSoup(r.text, "lxml")

 # Extracting Product names
 pr_name = soup.find_all("div", class_="_4rR01T")

 for i in pr_name:
    name = i.text
    product_name.append(name)

 # Extracting Product prices
 pr_price = soup.find_all("div", class_="_30jeq3 _1_WHN1")

 for i in pr_price:
    prices = i.text
    price.append(prices)

 # Extracting description
 pr_desc = soup.find_all("ul", class_="_1xgFaf")

 for i in pr_desc:
    desc = i.text
    description.append(desc)

 # Extracting ratings
 pr_rate = soup.find_all("span", class_="_1lRcqv")

 for i in pr_rate:
    rating = i.text
    ratings.append(rating)

df = pd.DataFrame({"Product Name": product_name, "Prices": price,
                  "Description": description, "Ratings": ratings})

print(df)

df.to_csv("D:/WebScraping/Flipkart/FlipKart webscrap.csv")