## update info from existing tables

import os
import random

def readHeaderslist(): 
    headerpath = os.path.join(os.path.dirname(os.getcwd()),'data/headers.txt')
    with open(headerpath,'r') as h:
        headers = h.readlines()
        h.close()
    print('Headers are read. There are '+str(len(headers))+' headers usable.')
    return(headers)

def randomHeaders(headers):
    selected = random.sample(headers,1)[0].strip()
    newHeaders = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection':'close',
        'Host':'book.douban.com',
        'User-Agent':selected,
        'Referer': 'https://book.douban.com/',
        'Upgrade-Insecure-Requests':'1'
# 'Connection':'keep-alive'
# 'Accept-Encoding':'gzip, deflate, br', ## br is not acceptable.
    }
    return(newHeaders)

def updateLinkSet(booklinkset):
    try:
        linksetpath = os.path.join(os.path.dirname(os.getcwd()),'data/BookLinkSet.txt')
        b = open(linksetpath,'r')
        booklinkset = b.readlines()
        b.close()
        booklinkset = set([i.split('?')[0] for i in booklinkset])
        print('Book Link set is updated. There are already '+str(len(booklinkset))+' books recorded.')
        return(booklinkset)
    except:
        return(set())
