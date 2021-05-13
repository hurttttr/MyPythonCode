import requests
import json

url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend'
headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
res = []
for i in range(1,4):
    data = {
        'page_start' : i*20
    }
    response = requests.get(url, headers=headers,data=data)
    content = response.content.decode()
    lst = json.loads(content)['subjects']
    res+=lst

with open('meiju.josn','w',encoding='utf-8') as f:
    for i in res:
        f.write(json.dumps(i,ensure_ascii=False,indent=4))
        f.write('\n')