import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
url = 'https://www.qiushibaike.com/text/page/'
for i in range(1,14):
    new_url = url + str(i)
    response = requests.get(url, headers=headers)
    html = response.content.decode()

    element = etree.HTML(html)
    lst = element.xpath('//*[@class="content"]/span')
    for j in range(len(lst)):
        print('第'+str(i)+'页，第'+ str(j+1)+'个段子')
        x = lst[j].xpath('string(.)')
        content = x.replace('\n','')
        print(content)