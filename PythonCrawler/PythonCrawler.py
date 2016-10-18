#encoding=utf8
import requests
from bs4 import BeautifulSoup
import re,time
import os,json
import base64 
from Crypto.Cipher import AES
from pprint import pprint 

Default_Header = {
    'Referer':'http://music.163.com/',
    'Host':'music.163.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate'
    }

BASE_URL = 'http://music.163.com'

_session = requests.session()
_session.headers.update(Default_Header)

def getPage(pageIndex):
    pageUrl = 'http://music.163.com/discover/playlist/?order=hot&cat=È«²¿&limit=35&offset='+pageIndex
    soup = BeautifulSoup(_session.get(pageUrl).content)
    songList = soup.findAll('a',attrs = {'class':'tit f-thide s-fc0'})
    for i in songList:
        print(i['href'])
        getPlayList(i['href'])


