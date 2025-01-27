import requests
from bs4 import BeautifulSoup

url ='https://www.ptt.cc/bbs/NBA/index.html'
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 Edg/131.0.0.0'}
response = requests.get(url,headers=headers)

soup =BeautifulSoup(response.text,'html.parser')
articles = soup.find_all('div',class_='r-ent')
for a in articles: #a是articles縮寫
    title = a.find('div',class_='title') #a.find 找出articles裡面資料是div class=title
    if title and title.a:  #如果兩者同時存在
        title = title.a.text
    else:
        title = "沒有標題" #有時候只會有title存在 title.a不存在

    popular = a.find('div',class_='nrec')
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = 'N/A'

    date = a.find('div',class_='date')
    if date:
        date = date.text
    else:
        date = "N/A"
    print(f'標題:{title}  人氣:{popular}  日期:{date}')