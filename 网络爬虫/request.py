import requests
from lxml import etree

url = 'http://category.dangdang.com/cid4005712.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
response = requests.get(url, headers=headers)
html = response.content.decode('gbk')
element = etree.HTML(html)
lst = element.xpath('//ul[@class="bigimg cloth_shoplist"]/li')
for i in lst:
    tmp=i.xpath('./p[@class="name"]/a/@title')[0]
    print (tmp)

