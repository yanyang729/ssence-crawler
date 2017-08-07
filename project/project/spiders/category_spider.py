import scrapy
from scrapy.http import Request
import json
from ..items import Category


class CategorySpider(scrapy.Spider):
    name = "allcategory"
    allowed_domains = ["ssense.com/en-us/"]
    categories = ['accessories', 'bags', 'clothing', 'shoes']
    start_urls = ["http://www.ssense.com/en-us/men/%s" % cat for cat in categories] + \
                 ["http://www.ssense.com/en-us/women/%s" % cat for cat in categories]

    def parse(self, response):
        """
        +- 4 main categories (shoes,bags....)
            +- 1st level categories
                +-- 2nd level categories (some have some don't)

        this step is to get all first level subcategories.
        """
        gender = response.url.split('/')[-2]
        for selector in response.css('#category-list > li > ul > li > a ::text'):
            sub_cat = selector.extract().strip().lower().replace(' & ', '-').replace(' ', '-')
            json_url = "http://www.ssense.com/en-us/%s/%s.json" % (gender, sub_cat)
            yield Request(json_url, callback=self.parse_json, dont_filter=True)

    def parse_json(self, response):
        json_response = json.loads(response.body_as_unicode())
        all_cat = []
        seoKeyword = response.url.split('/')[-1].split('.')[0]
        gender = response.url.split('/')[-2]
        # search for 1st level subcats if they have children also yield.
        for main_cat in json_response['facets']['categories']:
            if main_cat['children']:
                for sub_cat in main_cat['children']:
                    if sub_cat['seoKeyword'] == seoKeyword:
                        cat = Category(id=sub_cat['id'], name=sub_cat['name'], seoKeyword=sub_cat['seoKeyword'],gender=gender)
                        all_cat.append(cat)
                        if sub_cat['children']:
                            for sub2_cat in sub_cat['children']:
                                cat = Category(id=sub2_cat['id'], name=sub2_cat['name'], seoKeyword=sub2_cat['seoKeyword'],gender=gender)
                                all_cat.append(cat)
        for cat in all_cat:
            yield cat






