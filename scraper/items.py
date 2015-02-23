from scrapy import Item, Field


class Procurement(Item):
    procurer = Field()
    title = Field()
    url = Field()
    published_date = Field()
    closing_date = Field()

    def __init__(self, procurer, *args, **kwargs):
        super(Procurement, self).__init__(procurer=procurer, **kwargs)
