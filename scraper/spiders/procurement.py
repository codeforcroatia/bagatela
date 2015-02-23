import scrapy
import pprint

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

        results = [Procurement(procurer, title=e.extract()) for e in response.css(selectors['title'])]

        return results
