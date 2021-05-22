# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# import json
from itemadapter import ItemAdapter
import pymysql

class DangdangPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            database='mydatabase',
            charset='utf8'
        )
        pass

    def process_item(self, item, spider):
        tmp=dict(item)
        try:
            with self.conn.cursor() as cursor:
                sql = 'insert into spider(name,price,link,comment) values(%s, %s, %s, %s)'
                cursor.execute(sql, (tmp['name'],tmp['price'],tmp['link'],tmp['comment']))
                self.conn.commit()
        except pymysql.DatabaseError:
            self.conn.rollback()
        return item
        
    def __del__(self):
        pass

    def open_spider(self, spider):
        pass
    def close_spider(self, spider):
        self.conn.close()
        pass
