import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4005627.html']

    def parse(self, response):
        item = DangdangItem()
        item['name']=response.xpath('//*[@class="pic"]/@title').extract()
        item['price']=response.xpath('//*[@class="price_n"]/text()').extract()
        item['link'] = response.xpath('//*[@class="pic"]/@href').extract()
        item['comment'] = response.xpath('//*[@dd_name="单品评论"]/text()').extract()
        yield item

        for i in range(2,5):
            url = 'http://category.dangdang.com/pg{}-cid4005627.html'.format(i)
            yield Request(url,callback=self.parse)
