#-*- coding:utf8 -*-
#coding=utf-8
__author__ = 'XC'
import pymongo
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
        }
raw_cookies='_dacevid3=34b7c308.ddfc.5959.2e64.4520f6150b01; __gads=ID=4b1ba663a438c39d:T=1504785341:S=ALNI_MagOIiMyEsiNENY5mXlKOJG7Ar2kg; _HUPUSSOID=24e93c2c-6641-4b8e-aaa6-d3943921f6fb; _CLT=b0c2a05996d8b48b354e1fa4ddfc1fef; u=26799734|6Zi/5qOu57qz5bCP6ICB6JmO|e53c|4f7c7a478391b1de3626856ef4154550|8391b1de3626856e|6Zi/5qOu57qz5bCP6ICB6JmO; us=74843329f3ef30ea6c7bd7911dbdc94d36c9680409fdb0e29fb6e2659c08f860aff34458dfda287ec5101afd4cb6588ef048cb754c11429bfbc3a1e4bf1b669b; cn_2815e201bfe10o53c980_dplus=%7B%22distinct_id%22%3A%20%2215fb8e80ec8635-0b0cc32d3-6815147c-1aeaa0-15fb8e80ec9b49%22%2C%22sp%22%3A%20%7B%22%24uid%22%3A%20%2234b7c308.ddfc.5959.2e64.4520f6150b01%22%2C%22%24recent_outside_referrer%22%3A%20%22%24direct%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201510635777%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201510635777%7D%2C%22initial_view_time%22%3A%20%221510630942%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referrer_domain%22%3A%20%22%24direct%22%7D; UM_distinctid=15fb8e80ec8635-0b0cc32d3-6815147c-1aeaa0-15fb8e80ec9b49; __dacevid3=0x7903a9f262f3c2c0; lastvisit=85529%091512543954%09%2Fpost.php%3Ffid%3D1048; _fmdata=8F8D66889BE63FD5CABB8C694CDFFB35A968FC91A6E1924A431FEBB4699065B301C02534DD26A289A7E9E13D9D0EDAE27891C3B26D08FA7F; ua=43217861; __dacevst=e51b0fb8.5018fea3|1512633439482; _cnzz_CV30020080=buzi_cookie%7C34b7c308.ddfc.5959.2e64.4520f6150b01%7C-1; Hm_lvt_39fc58a7ab8a311f2f6ca4dc1222a96e=1512609715,1512614850,1512625121,1512631633; Hm_lpvt_39fc58a7ab8a311f2f6ca4dc1222a96e=1512631640'
cookies={}
for line in raw_cookies.split(';'):
    key,value=line.split('=',1)#1代表只分一次，得到两个数据
    cookies[key]=value
#print cookies

url = 'https://bbs.hupu.com{}-postdate-{}'.format('/cavaliers', str(20))
wb_data = requests.get(url,headers=headers,cookies=cookies)
soup = BeautifulSoup(wb_data.text, 'lxml')
print soup
