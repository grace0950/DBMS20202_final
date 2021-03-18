import requests as rq
import sys
import codecs
from bs4 import BeautifulSoup

# python stdout default encodes ansi, change to utf-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

url = "https://www.ambassador.com.tw/home/MovieList?Type=1"
response = rq.get(url)

def gethref(dom):
    soup = BeautifulSoup(dom, features="html.parser")
    cell = soup.find_all('div', class_='cell')
    for C in cell:
        img = C.find("img")
        print(f"{C.find('h6').text},{img['src']}")

def main():
    x = response.text
    gethref(x)


if __name__ == "__main__":
    main()

