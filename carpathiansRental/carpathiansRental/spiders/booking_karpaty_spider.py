import scrapy


class BookingKarpaty(scrapy.Spider):
    name = "booking_karpaty"
    allowed_domains = ['booking.karpaty.ua']
    start_urls = [
        # готелі Буковель
        'https://booking.karpaty.ua/uk/cities/539876186e656f114e440000?dr=true&ga=2#539876186e656f114e5d0000|539876186e656f114e440000',
        # гостинний двір
        'https://booking.karpaty.ua/uk/cities/539876186e656f114e440000?dr=true&ga=2#539876186e656f114e5b0000|539876186e656f114e440000',
        # приватна садиба
        'https://booking.karpaty.ua/uk/cities/539876186e656f114e440000?dr=true&ga=2#539876186e656f114e5a0000|539876186e656f114e440000',
        # готелі Славське
        'https://booking.karpaty.ua/uk/cities/539876186e656f114e540000?dr=true&ga=2#539876186e656f114e5d0000|539876186e656f114e540000',
        # гостинний двір
        'https://booking.karpaty.ua/uk/cities/539876186e656f114e540000?dr=true&ga=2#539876186e656f114e5b0000|539876186e656f114e540000',
        # приватна садиба
        'https://booking.karpaty.ua/uk/cities/539876186e656f114e540000?dr=true&ga=2#539876186e656f114e5a0000|539876186e656f114e540000',
        # Дргобрат
        'https://booking.karpaty.ua/uk/cities/54d1e8064b617207dab82a00?dr=true&ga=2#54d1e8064b617207dab82a00',
        # Ясіня
        'https://booking.karpaty.ua/uk/cities/539876186e656f114e4f0000?dr=true&ga=2#539876186e656f114e4f0000',
        # Пилипець
        'https://booking.karpaty.ua/uk/cities/55d48d2ac0557c6378000faa?dr=true&ga=2#539876186e656f114e5a0000|539876186e656f114e5d0000|55d48d2ac0557c6378000faa',
        # Яблуниця
        'https://booking.karpaty.ua/uk/cities/539876186e656f114e480000?dr=true&ga=2#539876186e656f114e5d0000|539876186e656f114e5b0000|539876186e656f114e5a0000|539876186e656f114e590000|539876186e656f114e480000',
    ]

    def parse(self, response):
        print("______URL______", response.url)
        for next_page in response.xpath('//ul[@class="list clearfix"]/li/a/@href').getall():
            print("NEXT_PAGE", next_page)
            yield response.follow(next_page, self.parse_hotel)

    def parse_hotel(self, response):
        price_per = response.xpath('//span[@class="ap-price__per"]/text()').get()
        if 'котедж' in price_per:
            print('Cottage')
            return
        price = int(response.xpath('//span[@class="ap-price__amount"]/text()').get().replace(" ", ""))
        if 'особа' in price_per:
            price *= 2
        name = response.xpath('//div[@class="ap-name"]/h1/text()').get()
        desc = response.xpath('//div[@class="container--text"]/p/text()').get()
        location = response.xpath('//div[@class="ap-address"]/p/text()').get()
        coords = response.xpath('//div[@class="location-coords"]/text()').get()
        (latitude, longitude) = coords.split(', ')
        latitude = float(latitude)
        longitude = float(longitude)
        # print("_____DATA:", name, price, latitude, longitude, location, desc)
        yield {
            'name': name,
            'price': price,
            'location': location,
            'latitude': latitude,
            'longitude': longitude,
            'desc': desc
        }


