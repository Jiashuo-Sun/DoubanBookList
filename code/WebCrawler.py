from bs4 import BeautifulSoup
import os
import random
import re 
import requests
import json
import time
from datetime import datetime

from bookupdate import *
from bookclean import *


def writeBookinfo(url,headers,n):
    try:
        print('Try to get html from the book which will be recorded...')
        bookhtml = requests.get(url, headers = randomHeaders(headers), timeout = 8)
        print("Request Successful for the "+str(n)+'-th book!')
        bookinfo = BeautifulSoup(bookhtml.content, features="html5lib")
    except:
        print('Wrong!!') 
        return(False)   

    try:
        result = bookinfo.find('script', {'type':'application/ld+json'})
        result = json.loads(result.text.strip())
    except:
        return(False)
    try:
        bookName = result['name']
    except:
        bookName = ''
    try:	    
        bookAuthor = result['author'][0]['name']
    except:
        bookAuthor = ''
    try:
        bookIsbn = result['isbn']
    except:
        bookIsbn = ''
    try:
        bookUrl = result['url']
        if bookUrl != url:
            print(bookUrl + '<--->' + url)
    except:
        bookUrl = url  
    try:
        voteNum = bookinfo.find('span',{'property':'v:votes'})
        voteNum = voteNum.text.strip()
    except:
        voteNum = ''    
    try:
        voteAvg = bookinfo.find('strong',{'property':'v:average'})
        voteAvg = voteAvg.text.strip()
    except:
        voteAvg = ''
    
    booklistpath = os.path.join(os.path.dirname(os.getcwd()),'data/BookInfoSet.csv')   
    
    with open(booklistpath, mode = 'a') as f:
        f.write(bookIsbn+',')
        f.write('"'+bookName+'"'+',')
        f.write('"'+bookAuthor+'"'+',')
        f.write(voteAvg+',')
        f.write(voteNum+',')
        f.write(bookUrl+',')
        f.write(str(datetime.date(datetime.today()))+'\n')
        f.close()
        print("This is the " + str(n)+ "-th book recorded this time! Book Info is written into file! Take a short break!")
    return(True)         


def main():

    headers = readHeaderslist()
    booklinkset = updateLinkSet(set())

    if len(booklinkset) == 0:
        url = 'https://book.douban.com/'
    else:
        url = random.sample(booklinkset,1)[0]

    loop = 0
    n = 1
    error = 0
    totalRequest = 0

    print("Start Time: "+ str(datetime.today()))

    while True:
        try:
            print('Try to get html from the link of book link set...')
            html = requests.get(url, headers = randomHeaders(headers), timeout = 8)
            if html.ok: print("Request Success for the " + str(loop) + "-th time!")
            loop += 1
            totalRequest += 1

            page = BeautifulSoup(html.content, features="html5lib")
            urllist = page.findAll('a',{'href':re.compile("https://book.douban.com/subject/[0-9]*")})
            print('Find '+ str(len(urllist))+' books.')
            for link in urllist:
                booklink = cleanlink(link['href'])
                if booklink not in booklinkset:
                    result = writeBookinfo(booklink, headers,n)
                    if result: 
                        n += 1
                        totalRequest += 1
                        booklinkset.add(booklink)
                        linksetpath = os.path.join(os.path.dirname(os.getcwd()),'data/BookLinkSet.txt')
                        with open(linksetpath,'a') as a:
                            a.write(booklink+'?\n')
                            a.close()
                        time.sleep(random.randint(5,10))
            url = random.sample(booklinkset,1)[0]
            time.sleep(random.randint(3,5))
        except:
            error += 1
            print("Stop Time: " + str(datetime.today()))
            print('The total requests are '+str(totalRequest))
            if error > 1: break
            url = random.sample(booklinkset,1)[0]
            time.sleep(random.randint(1,3))

if __name__ == '__main__':
    main()
