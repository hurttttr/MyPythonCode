import requests
from lxml import etree
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
url = 'https://www.qiushibaike.com/8hr/page/'
res = []
for i in range(1,3):
    new_url = url + str(i)
    response = requests.get(url, headers=headers)
    html = response.content.decode()

    element = etree.HTML(html)
    lst = element.xpath('//li[contains(@id, "qiushi_tag")]')
    for j in lst:
        item = {}
        tmp = j.xpath('.//*[@class="recmd-name"]/text()')[0]
        item['author'] = tmp#作者
        tmp = j.xpath('.//*[@class="recmd-content"]/text()')[0]
        item['title'] = tmp#标题
        tmp = j.xpath('.//*[@class="recmd-num"]/span[1]/text()')[0]
        item['funny_number'] = tmp#好笑数
        tmp = j.xpath('.//*[@class="recmd-num"]/span[4]/text()')
        tmp = tmp[0] if tmp else None
        item['comment'] = tmp#评论数
        tmp = j.xpath('./a/img/@src')[0]
        tmp = 'https:'+tmp
        item['img'] = tmp
        res.append(item)

with open('qiushi.json', 'w',encoding='utf-8') as f:
    for i in res:
        f.write(json.dumps(i,ensure_ascii=False,indent=4))
        f.write('\n')

