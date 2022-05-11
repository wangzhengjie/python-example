import requests
from bs4 import BeautifulSoup
import urllib.parse
import csv
url='https://feebee.com.tw/s/?q='
query='筆電'
#要讓網頁知道是瀏覽器去抓取的
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}
q=urllib.parse.quote(query) #編解碼 轉乘unicode
# print(q)
page=requests.get(url+q,headers=headers)
soup=BeautifulSoup(page.text,'html.parser')
spantag=soup.find_all('span','pure-u items_container')
items=[]
for i in spantag:
    # items.append(i.a['title']))
    item=[i.a['title'],i.a['data-price'] ,i.a['data-store']   ]
    items.append(item)
# for item in items:
#     print(item)

#寫入檔案 #newline預設是有\n會換行 會多一個空白 
a=['品項', '價格', '商家']
with open('feebee.csv','w',encoding="utf-8",newline='') as fobj:
    writer=csv.writer(fobj)
    writer.writerow(a)
    for item in items:
        print(item)
        writer.writerow(item)



# https://feebee.com.tw/s/?q=%E7%AD%86%E9%9B%BB