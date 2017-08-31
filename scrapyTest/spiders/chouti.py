# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector,Selector
from scrapy.http.request import Request

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'   #必须要有
    allowed_domains = ['chouti.com']   #允许的域名。爬虫的时候可能发生url跳转
    start_urls = ['http://dig.chouti.com/']   #开始的url

    def parse(self, response):
        # print(response.text)   #返回的是字符串
        # print(response.content)    #
        # hxs=HtmlXPathSelector(response)  #
        # page_list=hxs.select('//div[@id="content-list"]//a[@class="show-content"]')
        #
        # print(page_list)

        # hxs=Selector(response=response)
        # page_list=hxs.xpath('//div[@id="content-list"]')   #返回的是一个列表
        # print(type(page_list[0]))    #<class 'scrapy.selector.unified.Selector'>
        url_list=[]

        hxs=Selector(response=response)
        page_list=hxs.xpath('//div[@id="content-list"]//div[@class="news-content"]')
        for item in page_list:
            res=item.xpath('//a[@class="show-content color-chag"]')

            url=res.xpath('./@href').extract_first()
            res_text=res.xpath('./text()').extract()  #extract()把Selector对象转换成标签字符串
            print(res_text)
            print(url)

        page_area=hxs.xpath('//div[@id="page-area"]')
        page_url=page_area.xpath('//a[re:test(@href,"/all/hot/recent/\d+")]/@href').extract()

        for i in page_url:
            url_list.append("http://dig.chouti.com"+i)

        current_page = page_area.xpath ('//span[@class="ct_pagepw"]/text()')



        if current_page:
            real_url="http://dig.chouti.com/all/hot/recent/"+str(current_page)
            url_list.append(real_url)

        for url in url_list:
            yield Request(url=url,callback=self.parse)








