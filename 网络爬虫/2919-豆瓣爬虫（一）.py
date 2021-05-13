import requests
import re
import json
from lxml import etree

url = 'https://movie.douban.com/chart'
res = []
pat = '(\d+)?人评价'
headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

response = requests.get(url, headers=headers)
html = response.content.decode()
element = etree.HTML(html)
lst = element.xpath('//*[@class="item"]')

for  i in lst:
    item = {}
    tmp = i.xpath('./td/a/@title')[0]
    item['title'] = tmp#标题
    tmp = i.xpath('./td/a/@href')[0]
    item['href']=tmp#链接
    tmp = i.xpath('.//div[@class="star clearfix"]/span[2]/text()')[0]
    item['rating_nums']=tmp
    tmp = i.xpath('.//div[@class="star clearfix"]/span[3]/text()')[0]
    tmp = re.findall(pat,tmp)[0]
    item['comment']=tmp
    res.append(item)

with open('douban.json', 'w',encoding='utf8') as f:
    for i in res:
        f.write(json.dumps(i,ensure_ascii=False,indent=4))
        f.write('\n')
