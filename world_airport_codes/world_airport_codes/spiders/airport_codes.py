# -*- coding: utf-8 -*-
import scrapy


class AirportCodesSpider(scrapy.Spider):
    name = 'airport_codes'
    allowed_domains = ['www.world-airport-codes.com']
    start_urls = ['https://www.world-airport-codes.com/alphabetical/airport-name/a.html?page=1'']

    def parse(self, response):
        data = []

        data.append({'nama': 'CGK'})
        data.append({'nama': 'SUB'})
