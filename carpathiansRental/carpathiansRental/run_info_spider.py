import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from carpathiansRental.spiders.karpaty_info_spider import KarpatyInfo
import threading


class InfoScrapperRunner(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.process = CrawlerProcess(get_project_settings())

    def run(self):
        self.process.crawl(KarpatyInfo)
        self.process.start()


if __name__ == '__main__':
    client = InfoScrapperRunner()
    client.start()
