# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from lxml import etree as et
import unicodedata


class KorrespondentPipeline:

    def open_spider(self, spider):
        self.file = open('data.xml', 'w')
        self.tree = et.Element('data')

    def close_spider(self, spider):
        self.file.write(et.tostring(self.tree, pretty_print=True, encoding='utf8').decode("utf-8"))
        self.file.close()

    def process_item(self, item, spider):
        print("______Pipeline______", item)
        page = et.Element('page')
        page.set('url', item['url'])
        for text in item['text']:
            text = " ".join(text.split())
            text = "".join(ch for ch in text if unicodedata.category(ch)[0] != "C")
            if text:
                fragment = et.Element('fragment')
                fragment.text = text;
                fragment.set('type', 'text')
                page.append(fragment)
        for img in item['img']:
            fragment = et.Element('fragment')
            fragment.set('type', 'image')
            fragment.text = img
            page.append(fragment)

        self.tree.append(page)

        return item

