import scrapy
import time
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class KarpatyInfo(scrapy.Spider):
    name = "karpaty_info"
    allowed_domains = ['www.karpaty.info']
    start_urls = [
        # Буковель
        'https://www.karpaty.info/ua/recreation/residence/?region=2&region1=15&res_type=0&price_select=1-1000000&res_places_cott=&food=0&ski_distance=0&keyword=&results_order=obj_price&results_order_dir=1&search_page=0&search_form_on_start_page=0&srch_acco=1#searchresults_one',
        # Славське
        # 'https://www.karpaty.info/ua/recreation/residence/?region=1&region1=94&res_type=0&price_select=1-1000000&res_places_cott=&food=0&ski_distance=0&keyword=&results_order=obj_price&results_order_dir=1&search_page=0&search_form_on_start_page=0&srch_acco=1#searchresults_one',
        # # Дргобрат
        # 'https://www.karpaty.info/ua/recreation/residence/?region=3&region1=168&res_type=0&price_select=1-1000000&res_places_cott=&food=0&ski_distance=0&keyword=&results_order=obj_price&results_order_dir=1&search_page=0&search_form_on_start_page=0&srch_acco=1#searchresults_one',
        # # Ясіня
        # 'https://www.karpaty.info/ua/recreation/residence/?region=3&region1=100&res_type=0&price_select=1-1000000&res_places_cott=&food=0&ski_distance=0&keyword=&results_order=obj_price&results_order_dir=1&search_page=0&search_form_on_start_page=0&srch_acco=1#searchresults_one',
        # # Пилипець
        # 'https://www.karpaty.info/ua/recreation/residence/?region=3&region1=113&res_type=0&price_select=1-1000000&res_places_cott=&food=0&ski_distance=0&keyword=&results_order=obj_price&results_order_dir=1&search_page=0&search_form_on_start_page=0&srch_acco=1#searchresults_one',
        # # Яблуниця
        # 'https://www.karpaty.info/ua/recreation/residence/?region=2&region1=14&res_type=0&price_select=1-1000000&res_places_cott=&food=0&ski_distance=0&keyword=&results_order=obj_price&results_order_dir=1&search_page=0&search_form_on_start_page=0&srch_acco=1#searchresults_one',
    ]

    def parse(self, response):
        print("______URL______", response.url)
        for next_page in response.xpath('//ul[@class="pagination"]/li/a/@href').getall():
            print("NEXT_PAGE", next_page)
            yield response.follow(next_page, self.parse_page)

    def parse_page(self, response):
        print("PAGE")
        for next_page in response.xpath('//ul[@class="objlist-ul clearfix"]/li/a/@href').getall():
            print("HOTEL_PAGE", next_page)
            yield response.follow(next_page, self.parse_hotel)

    def parse_hotel(self, response):
        price_table = response.xpath('//table').get()
        if not price_table:
            return
        prices_string = " ".join(BeautifulSoup(price_table).get_text().split())
        prices = [int(s) for s in prices_string.split() if s.isdigit()]
        if not len(prices):
            return
        price = min(i for i in prices if i >= 50)
        name = response.xpath('//div[@class="ki-tested ki-tested-ua"]/h2/text()').get()
        location_block = response.xpath('//div[@class="uheader-content"]').getall()[0]
        location = " ".join(BeautifulSoup(location_block).get_text().split())
        desc_block = response.xpath('//div[@class="uheader-content"]').getall()[1]
        desc = " ".join(BeautifulSoup(desc_block).get_text().split())
        coords = response.xpath('//div[@class="ki_coords_DD"]/text()').get()
        (latitude, longitude) = coords.split()
        latitude = float(latitude)
        longitude = float(longitude)
        # print("_____DATA:", name, price, location, latitude, longitude, desc)
        time.sleep(0.5)
        yield {
            'name': name,
            'price': price,
            'location': location,
            'latitude': latitude,
            'longitude': longitude,
            'desc': desc
        }


