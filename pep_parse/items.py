import scrapy


class PepParseItem(scrapy.Item):
    # номер PEP
    number = scrapy.Field()
    # название PEP
    name = scrapy.Field()
    # статус, указанный на странице PEP
    status = scrapy.Field()
