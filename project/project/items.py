# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Category(scrapy.Item):
    id = scrapy.Field() # PK
    name = scrapy.Field()
    seoKeyword = scrapy.Field()
    gender = scrapy.Field()


class Product(scrapy.Item):
    id = scrapy.Field() # PK
    categoryid = scrapy.Field()
    name = scrapy.Field()
    brand = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    sku = scrapy.Field()


class ProuctDetail(scrapy.Item):
    id = scrapy.Field() # PK
    description = scrapy.Field()


class Image(scrapy.Item):
    url = scrapy.Field() # PK
    productid = scrapy.Field()


class Inventory(scrapy.Item):
    sku = scrapy.Field() # PK
    productid = scrapy.Field()
    name = scrapy.Field()
    instock = scrapy.Field()
