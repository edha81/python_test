import requests
from bs4 import BeautifulSoup
import pandas as pd

url ='https://www.ptt.cc/bbs/NBA/index.html'
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 Edg/131.0.0.0'}
response = requests.get(url,headers=headers)

data_list = [] #新增一個list

soup =BeautifulSoup(response.text,'html.parser')
articles = soup.find_all('div',class_='r-ent')
for a in articles: #a是articles縮寫
    data = {} #新增一個字典
    title = a.find('div',class_='title') #a.find 找出articles裡面資料是div class=title
    if title and title.a:  #如果兩者同時存在
        title = title.a.text
    else:
        title = "沒有標題" #有時候只會有title存在 title.a不存在
    data["標題"] = title #將title存到data標題中

    popular = a.find('div',class_='nrec')
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = 'N/A'
    data["人氣"] = popular #將popular存到data人氣中

    date = a.find('div',class_='date')
    if date:
        date = date.text
    else:
        date = "N/A"
    data["日期"] = date #將date存到data日期中
    data_list.append(data)#將字典中的資料存到data_list

df = pd.DataFrame(data_list) #將data_list列表轉換成pd的dataframe
df.to_excel('ptt_nba.xlsx',index=False,engine='openpyxl') #第一個參數檔名 第二個參數true的話前面會有識別碼001 002 003 第三個參數較適合處理excel xlsx的引擎

