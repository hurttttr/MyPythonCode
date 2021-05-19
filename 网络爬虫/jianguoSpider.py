import scrapy


class JianguospiderSpider(scrapy.Spider):
    name = 'jianguoSpider'
    allowed_domains = ['http://category.dangdang.com/cid4005712.html']
    start_urls = ['http://http://category.dangdang.com/cid4005712.html/']

    def parse(self, response):
        pass
