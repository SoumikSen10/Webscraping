import requests
from bs4 import BeautifulSoup
import itertools

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
r=requests.get(url)
#print(r)

soup=BeautifulSoup(r.text,"lxml") #lxml is data format and r.text to get the text 
#print(soup)

""" boxes=soup.find_all("div",class_ ="col-sm-4 col-lg-4 col-md-4")
print(boxes)
print(len(boxes)) """

names=soup.find_all("a",class_="title")
prices=soup.find_all("h4",class_="pull-right price")  

for i,j in zip(names,prices):
    print(i.text," ",j.text)
