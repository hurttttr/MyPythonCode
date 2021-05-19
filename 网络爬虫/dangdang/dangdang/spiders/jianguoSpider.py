import scrapy
from lxml import etree
from dangdang.items import DangdangItem

class JianguospiderSpider(scrapy.Spider):
    name = 'jianguoSpider'
    allowed_domains = [r'category.dangdang.com/cid4005712.html']
    start_urls = ['http://category.dangdang.com/cid4005712.html']

    def parse(self, response):
        lst = response.xpath('//ul[@class="bigimg cloth_shoplist"]/li')
        for i in lst:
            item = DangdangItem()
            item['name']=i.xpath('./p[@class="name"]/a/@title').extract()[0]
            item['price']=i.xpath('./p[@class="price"]/span/text()').extract()[0][1:]
            item['link'] = i.xpath('./p[@class="link"]/a/@href').extract()[0]
            item['comment'] = i.xpath('./p[@class="star"]/a/text()').extract()[0].replace('条评论','')
            yield item
