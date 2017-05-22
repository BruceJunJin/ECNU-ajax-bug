# -*- coding: utf-8 -*-
import scrapy
import json
from student.items import StudentItem

class StuspiderSpider(scrapy.Spider):
    name = "stuspider"
    start_urls = ['http://202.120.82.2:8081/']

    def start_requests(self):
        return [scrapy.FormRequest(url="http://202.120.82.2:8081/ClientWeb/pro/ajax/login.aspx", formdata={
            "act": "login",
            "id": "stuid",
            "pwd": "passwd",
        }, meta={
            "proxy": "http://127.0.0.1:8118"
        }, callback=self.parse_login)]

    def parse_login(self, response):
        return scrapy.Request(url="http://www.7mingzi.com/cn-xing/", callback=self.parse_xing)

    def parse_xing(self, response):
        items = response.xpath("/html/body/div/div/div[1]/blockquote[1]/ul/li/a/text()")
        for i in items.extract():
            yield scrapy.Request(url="http://202.120.82.2:8081/ClientWeb/pro/ajax/account.aspx?act=get_acc_name&name=%s" % (i),
                                 meta={
                                     "proxy": "http://127.0.0.1:8118"
                                 }, callback=self.parse)

    def parse(self, response):
        try:
            dt = json.loads(response.body)
            if dt['ret'] >= 1:
                for i in dt['data']:
                    item = StudentItem()
                    item['stuid'] = i['id']
                    item['stuname'] = i['name']
                    item['stuaccno'] = i['accno']
                    item['studept'] = i['dept']
                    item['stuphone'] = i['phone']
                    item['stuemail'] = i['email']
                    yield item
        except:
            pass
