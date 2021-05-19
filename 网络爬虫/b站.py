import requests
import json
import matplotlib.pyplot as plt

url = ' https://api.bilibili.com/x/space/arc/search?mid=12434430&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'
headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

response = requests.get(url, headers=headers)
content = response.content.decode('utf8')
data = json.loads(content) 
lst = data['data']['list']['vlist']

bvid = []
play=[]

for i in lst:
    bvid.append(i['bvid'])
    play.append(i['play']) 

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.bar(tuple(bvid[:10]), play[:10])
plt.title('视频播放量')

plt.show()

