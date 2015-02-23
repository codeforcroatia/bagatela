from scrapy import Item, Field


class Procurement(Item):
    procurer = Field()
    title = Field()
    url = Field()
    publish_date = Field()
    closure_date = Field()

    def __init__(self, procurer, *args, **kwargs):
        super(Procurement, self).__init__(procurer=procurer, **kwargs)
