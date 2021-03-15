import scrapy
from scrapy.exceptions import CloseSpider
import re


class PressSpider(scrapy.Spider):
    name = "press"
    allowed_domains = ['korrespondent.net']
    start_urls = [
        'https://korrespondent.net/'
    ]
    custom_settings = {
        'DEPTH_LIMIT': 2
    }

    N = 20  # number of pages
    count = 0

    def parse(self, response):
        # limit the number of pages
        if self.count >= self.N:
            raise CloseSpider(f"Scarped {self.N} items. Eject!")
        self.count += 1

        print("__________URL__________", response.url)
        print("NUMBER_OF_TEXT_ELEMENTS", response.xpath('count(//p/text() | //a/text() | //div/text())').get())

        yield {
            'img': response.xpath('//img/@src').getall(),
            'text': response.xpath('//p/text() | //a/text() | //div/text()').getall(),
            'url': response.url
        }
        for next_page in response.xpath('//a/@href').getall():
            yield response.follow(next_page, self.parse)

    def __remove_html_tags__(self, text):
        html_tags = re.compile('<.*?>')
        return re.sub(html_tags, '', text)
