import requests
import re
from lxml import etree

pat = '<a href="(.*?)" title'
url = 'https://zh.m.wikisource.org/zh/%E5%94%90%E8%A9%A9%E4%B8%89%E7%99%BE%E9%A6%96'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
}


response = requests.get(url, headers=headers)
html = response.content.decode()
element = etree.HTML(html)
lst = element.xpath('//*[@id="mw-content-text"]/div/section')
# lst = re.compile(pat, re.S).findall(html)
print(lst)
for i in lst[2:]:
    t = i.xpath('./ol/li/a/@href')
    print(t)
