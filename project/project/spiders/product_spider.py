import scrapy
import json
from ..items import Product, ProuctDetail, Image, Inventory
from scrapy.http import Request

class CategorySpider(scrapy.Spider):
    TOTAL_MEN_PAGE = 101
    TOTAL_WOMEN_PAGE = 104
    name = "product"
    allowed_domains = ["www.ssense.com/en-us/"]

    start_urls = ["http://www.ssense.com/en-us/men.json?page=%s" % (str(i+1)) for i in range(TOTAL_MEN_PAGE)] + \
                 ["http://www.ssense.com/en-us/women.json?page=%s" % (str(i+1)) for i in range(TOTAL_WOMEN_PAGE)]
    # # for test use
    # start_urls = ["http://www.ssense.com/en-us/men.json"]

    def parse(self, response):
        json_response = json.loads(response.body_as_unicode())
        products = json_response['products']
        for prod in products:
            product = Product(id=prod['id'], categoryid=prod['categoryId'], name=prod['name'], brand=prod['brand'],
                              url=prod['url'], price=prod['price']['regular'], sku=prod['sku'])
            yield product

            # go to product detail site
            product_url = 'http://www.ssense.com/en-us' + prod['url'] + '.json'
            yield Request(product_url, callback=self.parse_detail, dont_filter=True)


    def parse_detail(self,response):
        json_response = json.loads(response.body_as_unicode())
        product = json_response['product']

        productid = product['id']
        description = product['description']
        yield ProuctDetail(id=productid, description=description)

        for url in product['images']:
            url = url.replace('/__IMAGE_PARAMS__','')
            yield Image(url=url, productid=productid)

        dict_sizes = product['sizes']
        for key in dict_sizes:
            sku = dict_sizes[key]['sku']
            name = dict_sizes[key]['name']
            instock = dict_sizes[key]['inStock']
            yield Inventory(sku=sku, productid=productid, name=name, instock=instock)







