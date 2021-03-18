import requests as rq
import sys
import codecs
from bs4 import BeautifulSoup

# python stdout default encodes ansi, change to utf-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

url = "https://www.ambassador.com.tw/home/MovieList?Type=1"
response = rq.get(url)

def getweek(url):
    month = int(url[-5] + url[-4])
    day = int(url[-2] + url[-1])
    week = []
    for i in range(7):
        if month == 1 and day+i > 31:
            week.append(str(month+1).zfill(2) + '/' + str(day+i-30).zfill(2))
        # Feb. need to fix every year
        elif month == 2 and day+i > 28:
            week.append(str(month+1).zfill(2) + '/' + str(day+i-30).zfill(2))
        elif month == 3 and day+i > 31:
            week.append(str(month+1).zfill(2) + '/' + str(day+i-30).zfill(2))
        elif month == 4 and day+i > 30:
            week.append(str(month+1).zfill(2) + '/' + str(day+i-30).zfill(2))
        elif month == 5 and day+i > 31:
            week.append(str(month+1).zfill(2) + '/' + str(day+i-31).zfill(2))
        elif month == 6 and day+i > 30:
            week.append(str(month+1).zfill(2) + '/' + str(day+i-30).zfill(2))
        elif month == 7 and day+i > 31:
            week.append(str(month+1).zfill(2) + '/' + str(day+i-31).zfill(2))
        elif month == 8 and day+i > 31:
            week.append(str(month+1).zfill(2) + '/' + str(day+i-31).zfill(2))
        elif month == 9 and day+i > 30:
            week.append(str(month+1).zfill(2) + '/' + str(day+i-30).zfill(2))
        elif month == 10 and day+i > 31:
            week.append(str(month+1).zfill(2) + '/' + str(day+i-30).zfill(2))
        elif month == 11 and day+i > 30:
            week.append(str(month+1).zfill(2) + '/' + str(day+i-30).zfill(2))
        elif month == 12 and day+i > 31:
            week.append(str(month+1).zfill(2) + '/' + str(day+i-30).zfill(2))
        else:
            week.append(str(month).zfill(2) + '/' + str(day+i).zfill(2))
    return week

def gethref(dom):
    soup = BeautifulSoup(dom, features="html.parser")
    moviehref = soup.find_all("h6")
    for H in moviehref:
        nexturl = H.find('a').get('href')
        homeurl = "https://www.ambassador.com.tw"
        url = homeurl+nexturl
        week = getweek(url)
        #print(week)
        # remove last 5 words from url
        url = url[:-5]
        for day in week:
            #print(url + day)
            response = rq.get(url+day)
            x = response.text
            SS = BeautifulSoup(x, features="html.parser")
            theater = SS.find_all('div', class_='theater-box')
            getmovie(SS, theater, day)


def getmovie(SS, theater, day):
    for T in theater:
        times = T.find_all('h6')
        tings = T.find_all('span', "float-left info")
        for time, ting in zip(times, tings):
            print(f"title = {SS.find('title').text}")
            print(f"date = {day}")
            print(f"theater = {T.find('a').text}")
            print(f"time = {time.text}")
            print(f"ting = {ting.text}")
            print("")
    #print("-------------------------------------------------------------------------\n")


def main():
    x = response.text
    gethref(x)


if __name__ == "__main__":
    main()

