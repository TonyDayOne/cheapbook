#!/usr/bin python3

from bs4 import BeautifulSoup
import urllib.request as ureq
import sqlite3, re

def set_list(img):
    file = open('book/hmhm1.html', 'w')

    ln = len(img)
    count = round(ln/100)

    k = 0
    t = 1
    print('Start >>>', end=" ")
    for i in img:
        k += 1
        if k % count == 0:
            print('.', end="")
        if k % 4 == 0:
            t += 1
            tt = str(t)
            a = '<a href="hmhm'+tt+'.html">Site '+tt+' >>></a>'
            file.write(a)
            file.close()
            file = open("book/hmhm"+tt+".html", 'w')
        if i['data-src'] == "":
            src = i['src']
        else:
            src = i['data-src']
        s = '<div style="margin: 10px;"><img src="' + src + '"></div>\n\n';
        file.write(s)

def get_html():
    file = open('html.html', 'r')
    html = file.read().encode('utf-8')
    file.close()
    return html

def parse(html):
    soup = BeautifulSoup(html, "html5lib")
    ul = soup.find('ul', class_="previewContainer")
    img = ul.find_all('img')
    return img

def main():
    set_list(parse(get_html()))

if __name__ == "__main__":
    main()
