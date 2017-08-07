import scrapy


class CategorySpiderHelper(scrapy.Spider):
    """
    +- 4 main categories (shoes,bags....)
        +- 1st level categories
            +-- 2nd level categories (some have some don't)

    this spider is to get all first level subcategories and output a json file, with which we can make
    calls to get all categories.
    """
    name = "categoryhelper"
    allowed_domains = ["www.ssense.com/en-us/"]
    categories = ['accessories', 'bags', 'clothing', 'shoes']
    start_urls = ["http://www.ssense.com/en-us/men/%s" % cat for cat in categories] + \
                 ["http://www.ssense.com/en-us/women/%s" % cat for cat in categories]

    def parse(self, response):
        gender = response.url.split('/')[-2]
        for selector in response.css('#category-list > li > ul > li > a ::text'):
            sub_cat = selector.extract().strip().lower().replace(' & ','-').replace(' ','-')
            yield {
                'sub_cat': sub_cat,
                'gender': gender,
            }
