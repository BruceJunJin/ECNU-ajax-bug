# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

class StudentPipeline(object):

    conn = None
    cur = None

    def open_spider(self, spider):
        self.conn = psycopg2.connect(database="students", user="postgres", password="orchid", host="localhost", port="5433")
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cur.execute("INSERT INTO public.stuinfo (stuid,stuaccno,stuname,studept,stuphone,stuemail) \
              VALUES ('%s', '%s', '%s', '%s', '%s', '%s' )" % (item['stuid'], item['stuaccno'], item['stuname'], item['studept'], item['stuphone'], item['stuemail']))
            self.conn.commit()
        except Exception, e:
            print(str(e))
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.conn.close()

