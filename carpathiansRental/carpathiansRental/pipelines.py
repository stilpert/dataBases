import math
import pymongo
from pymongo.errors import DuplicateKeyError


def calc_distance(ltd, lng, ltd_c, lng_c):
    return math.sqrt(pow(ltd_c - ltd, 2) + pow(lng_c - lng, 2))


def get_resort_and_distance(ltd, lng):
    print('LTD______________LNG', ltd, lng)
    resort = ''
    distance = None
    if 48.34 < ltd < 48.37 and 24.4 <= lng < 24.5:
        resort = 'Bukovel'
        distance = calc_distance(ltd, lng, resort_centers['Bukovel'][0], resort_centers['Bukovel'][1])
    elif 48.24 < ltd < 48.275 and 24.237 < lng < 24.4:
        resort = 'Dragobrat'
        distance = calc_distance(ltd, lng, resort_centers['Dragobrat'][0], resort_centers['Dragobrat'][1])
    elif 48.29 < ltd < 48.32 and 24.44 < lng < 24.51:
        resort = 'Yablunytsya'
        distance = calc_distance(ltd, lng, resort_centers['Yablunytsya'][0], resort_centers['Yablunytsya'][1])
    elif 48.65 < ltd < 48.75 and 23.27 < lng < 23.328:
        resort = 'Pylypets'
        distance = calc_distance(ltd, lng, resort_centers['Pylypets'][0], resort_centers['Pylypets'][1])
    elif 48.79 < ltd < 48.93 and 23.40 < lng < 23.47:
        resort = 'Slavske'
        distance = calc_distance(ltd, lng, resort_centers['Slavske'][0], resort_centers['Slavske'][1])
    return resort, distance


resort_centers = {
    'Bukovel': [48.35826, 24.40846],
    'Dragobrat': [48.24957, 24.24956],
    'Yablunytsya': [48.31447, 24.48858],
    'Slavske': [48.79964, 23.44442],
    'Pylypets': [48.64943, 23.2901],
}


class CarpathiansRentalPipeline:

    def __init__(self):
        self.my_client = pymongo.MongoClient("mongodb://localhost:43000/")
        self.mydb = self.my_client["karpatydb"]
        self.hotels = self.mydb["hotels"]
        self.count = 0

    def open_spider(self, spider):
        print("___PIPLiNE WORKS___")
        print(self.mydb.list_collection_names())

    def close_spider(self, spider):
        print("___COUNT PAGES________", self.count)
        self.my_client.close()

    def process_item(self, item, spider):
        if not item:
            return
        (resort, distance) = get_resort_and_distance(item['latitude'], item['longitude'])
        print("____RESORT_____", resort, distance)
        if 40000 > item['price'] > 0 and distance and item['name']:
            print("_____DATA_____:", item['name'], item['price'], distance, resort)
            item["resort"] = resort
            item['distance'] = distance
            try:
                self.hotels.insert_one(item)
                self.count += 1
            except DuplicateKeyError:
                print("The same hotel is already exist!")

        return item


