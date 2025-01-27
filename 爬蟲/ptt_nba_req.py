import requests
url ='https://www.ptt.cc/bbs/NBA/index.html'
header = {'User-Agent:':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 Edg/131.0.0.0'}
response = requests.get(url,headers=header)
print(response.text)

if response.status_code == 200:
    with open('output.html','w',encoding='utf-8') as f:   
        f.write(response.text)
    print('資料成功寫入ˇ')
else:
    print('網址有誤')
