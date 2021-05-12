import requests 
from lxml import etree

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

url = 'https://list.jd.com/list.html?cat=9987,653,655&page='

for i in range(1,3):
    new_url = url+ str(i*2-1)
    response = requests.get(new_url, headers=headers)
    html = response.content.decode('utf-8')
    element = etree.HTML(html)
    lst = element.xpath('//*[@class="p-img"]/a/img/@data-lazy-img')
    
    for j in range(len(lst)):
        filename = 'image/{}_{}.jpg'.format(i,j+1)
        img_url = 'https:'+lst[j]
        response  = requests.get(img_url, headers=headers)
        with open(filename,'wb') as f:
            f.write(response.content)