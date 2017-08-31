# -*- coding: utf-8 -*-
import scrapy


class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://xiaohuar.com/']

    def parse(self, response):
        pass
