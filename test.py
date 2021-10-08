from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

tab = []
class Program:
    def __init__(self):
        self.dolar = ""
        self.euro = ""
        #print(self.dolar)

    def euroScrap():

        uClient = uReq("https://internetowykantor.pl/kurs-euro/")
        page_html = uClient.read()
        uClient.close()

        page_soup = soup(page_html, "html.parser")
        euro = page_soup.findAll("span", {"class": "kurs kurs_sredni bem-single-rate-box__item-rate"})
        

        for i in euro:
            euro = i.text
        #tab.append(euro)
        print("Euro:")
        print(euro +" " + "złoty")

    def dolarScrap():
        uClient = uReq("https://internetowykantor.pl/kurs-dolara/")
        page_html = uClient.read()
        uClient.close()

        page_soup = soup(page_html, "html.parser")
        dolar = page_soup.findAll("span", {"class": "kurs kurs_sredni bem-single-rate-box__item-rate"})

        for i in dolar:
            dolar = i.text
        #tab.append(dolar)
        print("Dolar:")
        print(dolar + " " + "złoty")

if __name__ == "__main__":
    try:
        Program.euroScrap()
        Program.dolarScrap()
    except:
        print("ERROR. CHECK YOUR INTERNET CONNECTION")
