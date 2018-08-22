# -*- coding: utf-8 -*-
import scrapy
from  quotetutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': ''.join(quote.css('div.tags a.tag::text').extract()),
            }

        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)