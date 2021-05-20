import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from carpathiansRental.spiders.booking_karpaty_spider import BookingKarpaty
import threading


class BookingScrapperRunner(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.process = CrawlerProcess(get_project_settings())

    def run(self):
        self.process.crawl(BookingKarpaty)
        self.process.start()


if __name__ == '__main__':
    client = BookingScrapperRunner()
    client.start()
