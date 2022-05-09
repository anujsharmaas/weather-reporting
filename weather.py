import requests
from bs4 import BeautifulSoup
place=input("enter the name of place:")
search=f"weather in{place}"
url=f"https://www.google.com/search?q={search}"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
update=soup.find("div",class_="BNeawe").text
print(f"{search}now is {update}")