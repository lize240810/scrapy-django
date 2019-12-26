# -*- coding: utf-8 -*-
import scrapy

from creditchina.models import NameItem


class CreditchinaSpider(scrapy.Spider):
    name = 'creditchina'
    allowed_domains = ['.gov.cn/']
    start_urls = ['http://https://www.creditchina.gov.cn//']

    def parse(self, response):
        print(NameItem)
