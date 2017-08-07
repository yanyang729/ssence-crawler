import scrapy
import json
import os
from ..items import Category


class CategorySpider(scrapy.Spider):
    """
    get all categories.
    """
    # check if I already have the 1st level category data dump on hand.
    DUMP_PATH = './utils/subcategories.json'
    if os.path.exists(DUMP_PATH):
        with open(DUMP_PATH,'rb') as f:
            dump = json.load(f)
    else:
        raise ValueError('Run spider categoryghelper first')

    name = 'allcategory'
    allowed_domains = ["www.ssense.com/en-us/"]
    start_urls = []
    for dict in dump:
        url = 'http://www.ssense.com/en-us/%s/%s.json' % (dict['gender'], dict['sub_cat'])
        start_urls.append(url)

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        all_cat = []
        seoKeyword = response.url.split('/')[-1].split('.')[0]
        # search for 1st level subcats if they have children also yield.
        for main_cat in jsonresponse['facets']['categories']:
            if main_cat['children']:
                for sub_cat in main_cat['children']:
                    if sub_cat['seoKeyword'] == seoKeyword:
                        cat = Category(id=sub_cat['id'], name=sub_cat['name'], seoKeyword=sub_cat['seoKeyword'])
                        all_cat.append(cat)
                        if sub_cat['children']:
                            for sub2_cat in sub_cat['children']:
                                cat = Category(id=sub2_cat['id'], name=sub2_cat['name'], seoKeyword=sub2_cat['seoKeyword'])
                                all_cat.append(cat)
        for cat in all_cat:
            yield cat






