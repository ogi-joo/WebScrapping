from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
print("Unesi url:")
theUrl = input()
# Url je unet

# Otvara se novi fajl i upisuju se prve tabele, odnosno headeri
f = open("products.csv", "w+")
f.write("data-productname" + "," + "data-productprice" + "," + "popust(%)" + "\n")

# Otvaranje stranice i smestanje sadrzaja u thePage
theClient = uReq(theUrl)
thePage = theClient.read()
theClient.close()

# html parsiranje(?)
soupPage = soup(thePage, "html.parser")

# findAll komanda - pronalazi svaki div, sa class koja sadrzi ovo navedeno | trazimo div na stranici koji ce nam biti objekat
knjiga = soupPage.findAll("div", {"class": "wrapper-gridalt-view item product-item ease col-xs-6 col-sm-3 col-md-2 col-lg-2 gridalt-view"})

print(len(knjiga)) # Proverava se koliko je div-ova nasao

#za svaki div nadjen uzima: productname, price i popust
for x in knjiga:
    popust = x.div.div.div.findAll("div", {"class": "caption-discount"})
    f.write(x["data-productname"].replace(",", " ") + "," + x["data-productprice"].replace(".","").replace(",",".") + "," +  popust[0].text.strip() + "\n")

#zatvara se fajl
f.close