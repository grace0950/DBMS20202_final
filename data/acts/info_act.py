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
    moviehref = soup.find_all("h6")
    for H in moviehref:
        #print(f"H = {H}")
        #print(H.find('a').get('href'))
        nexturl = H.find('a').get('href')
        homeurl = "https://www.ambassador.com.tw"
        url = homeurl+nexturl
        response = rq.get(url)
        x = response.text
        SS = BeautifulSoup(x, features="html.parser")
        info = SS.find('div', class_='movie-info-box')
        #print(info)
        if info != []:
            getinfo(info)
        else:
            break


def getinfo(info):
    attributes = info.find_all('p')
    actors = attributes[1].text.split(",")
    for A in actors:
        print(f"title = {info.find('h2').text}")
        print(A)
    print("-------------------------------------------------------------------------")


def main():
    x = response.text
    gethref(x)


if __name__ == "__main__":
    main()

