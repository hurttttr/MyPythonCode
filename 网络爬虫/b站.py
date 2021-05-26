import requests
import json
import time
import matplotlib.pyplot as plt

url = ' https://api.bilibili.com/x/space/arc/search?mid=12434430&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp' # pn代表页数
headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

response = requests.get(url, headers=headers)
content = response.content.decode('utf8')
data = json.loads(content) 
lst = data['data']['list']['vlist']
lst1 = data['data']['list']['tlist']

bvid = [] # bv号
play=[] # 播放量
created = {} 

# 数据处理
for i in lst:
    bvid.append(i['bvid'])
    play.append(i['play']) 
    creat_time = time.localtime(i['created'])
    month = creat_time.tm_mon
    day = creat_time.tm_mday
    t = '{}.{}'.format(month, day)
    created[t] = created.get(t,0)+1

day = [] # 日期
num = [] #作品数

for i in created:
    day.append(i)
    num.append(created[i])

title = [] # 分类标题 
count = [] # 数量
for i in lst1:
    title.append(lst1[i]['name'])
    count.append(lst1[i]['count'])
    
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5) # 自动调整子图间距

fig = plt.figure(1)
ax1 = plt.subplot(2,2,1) # 创建一个2*2的子图，并编辑第一块
plt.plot(bvid[:10], play[:10]) # 折线图
plt.xticks(bvid[:10],bvid[:10],rotation=30)
plt.title('视频播放量')
ax2 = plt.subplot(2,2,2) # 创建一个2*2的子图，并编辑第二块
plt.bar(day[:10], num[:10]) # 柱状图
plt.xticks(day[:10],day[:10],rotation=30)
plt.title('每日投稿数')
ax3 = plt.subplot(2,2,4) # 创建一个2*2的子图，并编辑第四块
plt.pie(count,
    labels=title,
    autopct = '%3.2f%%', #数值保留固定小数位
    shadow = False, #无阴影设置
    startangle =90, #逆时针起始角度设置
    pctdistance = 0.6#数值距圆心半径倍数距离
) # 饼图
plt.title('作品分布')

plt.show()
