import scrapy


class CategorySpider(scrapy.Spider):
    name = "category"
    allowed_domains = ["www.ssense.com/en-us/"]
    categories = ['accessories', 'bags', 'clothing', 'shoes']
    start_urls = ["http://www.ssense.com/en-us/men/%s" % cat for cat in categories] + \
                 ["http://www.ssense.com/en-us/women/%s" % cat for cat in categories]

    def parse(self, response):
        # TODO: check callback
        # if not hxs.select('//get/site/logo'):
        #     yield Request(url=response.url, dont_filter=True)
        gender = response.url.split('/')[-2]
        cat = response.url.split('/')[-1]
        for selector in response.css('#category-list > li > ul > li > a ::text'):
            sub_cat = selector.extract().strip().lower().replace(' ','-').replace(' & ','-')
            yield {
                'sub_cat': sub_cat,
                'gender': gender,
            }

