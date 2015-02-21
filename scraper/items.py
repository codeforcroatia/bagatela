from scrapy import Item, Field

class Procurement(Item):
    title = Field()
    url = Field()
    published_date = Field()
    closing_date = Field()
