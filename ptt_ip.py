import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
domin='http://api.ipstack.com/'
akey='?access_key=f25ddaceb5c4381e8368bdad5cb4e4c9'
urlheader='https://www.ptt.cc'
url='https://www.ptt.cc/bbs/Gossiping/index.html'
co={'over18':'1'}
thisday="{:2d}/{:0>2d}".format(datetime.now().month,datetime.now().day)

def get_page(url):
    resp=requests.get(url,cookies=co)
    soup=BeautifulSoup(resp.text,'html.parser')
    spantag=soup.find_all('div','r-ent')
    po_count=0
    for i in spantag:
       try:
           if i.find('div','date').text==thisday:
                po_count+=1
                resp2=requests.get(urlheader+i.a['href'],cookies=co)
                soup2=BeautifulSoup(resp2.text,'html.parser')
                # title=soup.find_all('span','article-meta-value')[2].text
                spantag=soup2.find('span','f2').text
                pattern = '\d+\.\d+\.\d+\.\d+'
                match = re.search(pattern, spantag)
                print(soup.find('div','btn-group btn-group-paging').find_all('a')[1]['href'])
                print(i.find('div','title').text)
                print(match.group())    
                # apiurl=domin+match.group()+akey
                # print(apiurl)
                # resp=requests.get(apiurl)
                # js=resp.json()
                # print(js["country_name"])
       except:
             if i.find('div','date').text==thisday:
                po_count+=1
                print('本文已被刪除')
            # if i.find('div','date').text==thisday:
            #     po_count+=1
        # print('----------------')
    if po_count>0:
        nextpage=urlheader+soup.find('div','btn-group btn-group-paging').find_all('a')[1]['href']
        get_page(nextpage)   
get_page(url)


