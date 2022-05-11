import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime



urlheadr='https://www.ptt.cc'
url='https://www.ptt.cc/bbs/Beauty/index.html'
co={'over18':'1'}
thisday="{:2d}/{:0>2d}".format(datetime.now().month,datetime.now().day)

def get_page(url):
    resp=requests.get(url,cookies=co)
    soup=BeautifulSoup(resp.text,'html.parser')

    
    

    
    divtag=soup.find_all('div','r-ent')
    # print(divtag)
    imglist=[]
    r=0 #計算有沒有文章
    for i in divtag:
        try:
            if i.find('div','date').text==thisday: #如果是今天才抓取
                r+=1
                # print(i.find('div','title').text)
                title=i.find('div','title').text.strip()+'/' #抓取標題
                print(title)
                # 建檔案取名標題
                if not os.path.exists(title):
                    os.mkdir(title)
                imglist.append(urlheadr+i.a['href']) #抓取文章裡面圖片的url
                
                # print(imglist)
                for i in imglist:
                    resp=requests.get(i,cookies=co)
                    soup=BeautifulSoup(resp.text,'html.parser')
                    links = soup.find(id='main-content').find_all('a')
                    img_urls=[]
                    for link in links: #用正規表示式抓取圖片
                        if re.match(r'^https?://(i.)?(m.)?imgur.com', link['href']):
                            img_urls.append(link['href'])
                            # print(img_urls)
                            count=0               
                            
                    for img in img_urls: #把圖片抓下來存起來 
                        img1=requests.get(img)
                        with open(title+str(count)+'.jpg','wb') as fobj:
                            fobj.write(img1.content)
                            count+=1
        except:
              if i.find('div','date').text==thisday:
                r+=1
                print('本文已被刪除')
                    
                    

                
                
                
                

    if r>0: #往前一頁抓取
        nextpage=urlheadr+soup.find('div','btn-group btn-group-paging').find_all('a')[1]['href']
        get_page(nextpage) 
        
get_page(url)
        
        


