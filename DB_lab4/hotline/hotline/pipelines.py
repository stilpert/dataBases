from lxml import etree as et


class HotlinePipeline:

    def open_spider(self, spider):
        self.file = open('guitars.xml', 'w')
        self.tree = et.Element('guitars')

    def close_spider(self, spider):
        self.file.write(et.tostring(self.tree, pretty_print=True, encoding='utf8', xml_declaration=True).decode("utf-8"))
        self.file.close()

    def process_item(self, item, spider):
        print("Pipeline")
        guitar = et.Element('guitar')
        guitar.set('url', item['url'])

        name = et.Element('name')
        name.text = " ".join(item['name'].split())
        guitar.append(name)

        if item['desc']:
            desc = et.Element('description')
            desc.text = " ".join(item['desc'].split())
            guitar.append(desc)

        price = et.Element('price')
        price.text = " ".join(item['price'].split())
        guitar.append(price)

        img = et.Element('image')
        img.text = " ".join(item['img'].split())
        guitar.append(img)

        self.tree.append(guitar)

        return item