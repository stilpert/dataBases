import scrapy


class GuitarSpider(scrapy.Spider):
    name = "guitars"
    allowed_domains = ['hotline.ua']
    start_urls = [
        'https://hotline.ua/musical_instruments/elektrogitary/'
    ]

    def parse(self, response):
        print("______URL______", response.url)

        for next_page in response.xpath('//div[@class="item-info"]/p/a/@href').getall()[:20]:
            print("NEXT_PAGE", 'https://hotline.ua' + next_page)
            yield response.follow(next_page, self.parse_guitar)

    def parse_guitar(self, response):
        name = response.xpath('//div[@class="heading"]/h1/text()').get()
        desc = response.xpath('//div[@class="app-nav-scroll"]/div[@class="text"]/p/text()').get()
        price = response.xpath('//span[@class="price-lg pointer"]/span[@class="value"]/text()').get()
        image = response.xpath('//div[@class="zg-canvas-box-img"]/img/@src').get()

        print("DESC", desc)
        print("NAME", name)
        print("PRICE", price)
        print("IMAGE", image)

        yield {
            'img': image,
            'desc': desc,
            'name': name,
            'price': price,
            'url': response.url
        }


