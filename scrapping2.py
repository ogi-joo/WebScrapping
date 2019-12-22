from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

given_URL = "https://www.gigatron.rs/laptop_racunari"
this_Client = uReq(given_URL)
take_Page = this_Client.read()
this_Client.close()

this_Page = soup(take_Page, "html.parser")

item = this_Page.findAll("li", {"class": "item"})
print(len(item[0]))

for x in item:
    productName = x.h4.a.text.strip()
    productPrice = x.findAll("h4", {"class": "final-price"})
    productName = productName.replace("+ POKLON Tri proizvoda", "").replace("+ POKLON tri proizvoda", "").replace("ili desktop rač.", "")
    print(productName.ljust(130, " ") + ", " + productPrice[0].text.strip())