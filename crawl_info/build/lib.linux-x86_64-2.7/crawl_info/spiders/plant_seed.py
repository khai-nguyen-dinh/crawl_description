
import scrapy

from crawl_info.items import CrawlInfoItem


class Plant(scrapy.Spider):
    name = 'exportersindia'
    allowed_domains = ['http://www.exportersindia.com']
    start_urls = [
      'http://www.exportersindia.com/industry/agriculture.htm'
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
        temp = CrawlInfoItem()
        temp['description'] = response.xpath('//div[@class="taj mt7px"]/text()').extract_first()
        return temp