import requests
import json
import math
API_KEY = '28e090ea'
OMDB_URL = 'http://www.omdbapi.com/?apikey=' + API_KEY
keywords='Iron Man'
movies_id=list()
query = '+'.join(keywords.split())  # e.g., "Iron Man" -> Iron+Man
url = OMDB_URL + '&s=' + query
data = json.loads(requests.get(url).text) #json.loads	将已编码的 JSON 字符串解码为 Python 对象
count=0
for item in data['Search']:
    # print(item['imdbID'])
    total=int(data['totalResults']) #找尋幾部電影
    num_page=math.floor(total/10)+1
for i in range(1,num_page): #一頁只有10 找下一頁的page
        # print(i)
    url = OMDB_URL + '&s=' + query + '&page=' + str(i)
    data = json.loads(requests.get(url).text)
    for item2 in data['Search']:
        movies_id.append(item2['imdbID'])
print('有關鋼鐵人電影共',len(movies_id),'部') #算出幾部電影


#先抓取每一個Id 然後串成新的url 再取抓前兩筆電影資訊
movies=list()
for id in movies_id:
    url1 = OMDB_URL + '&i=' + str(id)
    data1 = json.loads(requests.get(url1).text)
    movies.append(data1)
# for m in movies[:2]:
    # print(m)

#算出每部電影平均評分
#如果該電影的 'imdbRating' 欄位不是 'N/A' 則轉換其值為 float 並放入 ratings 內
# ratings = [float(m['imdbRating'])  for m in movies if m['imdbRating'] != 'N/A']
# print('平均評分:', sum(ratings)/len(ratings))
#簡單算出電影平均評分寫法
ratings=[]
for m in movies:
    if m['imdbRating'] != 'N/A':
        ratings.append(float(m['imdbRating']))
print('平均評分:', sum(ratings)/len(ratings))



