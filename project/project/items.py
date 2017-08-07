# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader


class Category(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    seoKeyword = scrapy.Field()
    gender = scrapy.Field()


class Product(scrapy.Item):
    id = scrapy.Field()