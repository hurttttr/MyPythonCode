import scrapy
from dangdang.items import DangdangItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Myspider2Spider(CrawlSpider):
    name = 'myspider2'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4005627.html']

    rules = (
        Rule(LinkExtractor(allow=r'pg\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        lst = response.xpath('//ul[@class="bigimg cloth_shoplist"]/li')
        for i in lst:
            item = DangdangItem()
            item['name']=i.xpath('./p[@class="name"]/a/@title').extract()[0]
            item['price']=i.xpath('./p[@class="price"]/span/text()').extract()[0][1:]
            item['link'] = i.xpath('./p[@class="link"]/a/@href').extract()[0]
            item['comment'] = i.xpath('./p[@class="star"]/a/text()').extract()[0].replace('条评论','')
            yield item
