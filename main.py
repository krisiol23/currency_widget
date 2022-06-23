from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


class Program:
    tab = []
    def __init__(self):
        pass

    def euroScrap():

        uClient = uReq("https://internetowykantor.pl/kurs-euro/")
        page_html = uClient.read()
        uClient.close()

        page_soup = soup(page_html, "html.parser")
        euro = page_soup.findAll("span", {"data-rates-direction": "forex"})
        

        for i in euro:
            euro = i.text
        
        print("Euro:")
        print(euro +" " + "złoty")

    def dolarScrap():
        uClient = uReq("https://internetowykantor.pl/kurs-dolara/")
        page_html = uClient.read()
        uClient.close()

        page_soup = soup(page_html, "html.parser")
        dolar = page_soup.findAll("span", {"data-rates-direction": "forex"})

        for i in dolar:
            dolar = i.text
        
        print("Dolar:")
        print(dolar + " " + "złoty")

if __name__ == "__main__":
    try:
        Program.euroScrap()
        Program.dolarScrap()
    except:
        print("ERROR. CHECK YOUR INTERNET CONNECTION")
