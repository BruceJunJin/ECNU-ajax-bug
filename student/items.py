# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StudentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    stuid = scrapy.Field()
    stuaccno = scrapy.Field()
    stuname = scrapy.Field()
    studept = scrapy.Field()
    stuphone = scrapy.Field()
    stuemail = scrapy.Field()
