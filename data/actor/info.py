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
        cell = SS.find('div', class_='cell small-3 medium-2 large-2 movie-pic-box')
        img = cell.find('img')
        #print(info)
        if info != []:
            getinfo(info, img)
        else:
            break


def getinfo(info, img):
    print(f"title = {info.find('h2').text}")
    print(f"EN_title = {info.find('h6').text}")
    attributes = info.find_all('p')
    print(f"{attributes[2].text}")
    print(f"url = {img['src']}")
    print(f"intro = {attributes[0].text}")
    print(f"{attributes[1].text}")


def main():
    x = response.text
    gethref(x)


if __name__ == "__main__":
    main()

