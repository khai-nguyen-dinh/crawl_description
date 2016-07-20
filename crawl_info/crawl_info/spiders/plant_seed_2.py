
import scrapy

from crawl_info.items import CrawlInfoItem
from scrapy.exceptions import CloseSpider

class Plant(scrapy.Spider):
    index = 0
    name = 'exportersindia_2'
    allowed_domains = ['http://www.exportersindia.com']
    start_urls = [
      'http://www.exportersindia.com/industry/fashion-apparel.htm'
    ]


    def parse(self, response):
        for url in response.xpath('//p[@class="b hig mb2px"]/a/@href').extract():
            request = scrapy.Request(url, callback=self.parse_categories,dont_filter=True)
            yield request

    def parse_categories(self, response):
        for url in response.xpath('//li[@class="w115px"]/a/@href').extract():
            request = scrapy.Request(url, callback=self.parse_data,dont_filter=True)
            yield request

    def parse_data(self, response):
        if self.index == 1000:
            raise CloseSpider("SHUT DOWN EVERYTHING!")
        self.index += 1
        temp = CrawlInfoItem()
        temp['id'] = 2
        temp['description'] = response.xpath('//div[@class="taj mt7px"]/text()').extract_first()
        return temp
