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

# def parse(self, response):
#     l = ItemLoader(item=Category(), response=response)
#     l.add_xpath('name', '//div[@class="product_name"]')
#     l.add_xpath('name', '//div[@class="product_title"]')
#     l.add_xpath('price', '//p[@id="price"]')
#     l.add_css('stock', 'p#stock]')
#     l.add_value('last_updated', 'today') # you can also use literal values
#     return l.load_item()