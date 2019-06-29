# -*- coding: utf-8 -*-
import scrapy


class AirportCodesSpider(scrapy.Spider):
    name = 'airport_codes'
    allowed_domains = ['www.world-airport-codes.com']
    start_urls = ['https://www.world-airport-codes.com/alphabetical/airport-name/a.html?page=1']

    def parse(self, response):
        data = []
        table = response.css('.stack2')
        row_selector = ".//tr[@class='light-row']|.//tr[@class='dark-row']"

        for row in table.xpath(row_selector):
            nama = row.xpath('./th/a/text()').extract_first()
            type = row.xpath('./td[1]/text()[2]').extract_first().strip()
            city = row.xpath('./td[2]/text()').extract_first()
            country = row.xpath('./td[3]/text()')extract_first()
            iata = row.xpath('./td[4]/text()')extract_first()
            icao = row.xpath('./td[5]/text()')extract_first()
            faa = row.xpath('./td[6]/text()')extract_first()

            data.append({
                "nama": nama,
                "type": type_,
                "city": city,
                "country": country,
                "iata": iata,
                "icao": icao,
                "faa": faa
            })


        return data

