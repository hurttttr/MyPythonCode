# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class DangdangPipeline:
    def __init__(self):
        self.file = open('data.json', 'w', encoding='utf-8')
        pass

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False,indent=4) + "\n"
        self.file.write(line)
        return item

    def open_spider(self, spider):
        pass
    def close_spider(self, spider):
        self.file.close()
        pass
