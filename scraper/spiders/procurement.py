import itertools
import operator
import scrapy

from bagatela.models import get_procurers
from scraper.items import Procurement

class ProcurementSpider(scrapy.Spider):
    name = 'procurement'

    def __init__(self):
        self.procurers = get_procurers()
        self.procurement_page_index = dict(
            (procurer.data['procurementPageUrl'], procurer)
                for procurer in self.procurers)

        self.start_urls = (procurer.data['procurementPageUrl']
            for procurer in self.procurers)

    def parse(self, response):
        procurer = self.procurement_page_index[response.url].data
        selectors = procurer['selectors']

        data = (map(operator.methodcaller('strip'), response.css(selectors[k]).extract()) for k, v in selectors.iteritems())
        keys = procurer['selectors'].keys()

        return map(lambda d: Procurement(procurer, **dict(zip(keys, d))), itertools.izip(*data));
