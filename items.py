# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class realstateScraperItem(scrapy.Item):
    house_title = scrapy.Field()
    house_price = scrapy.Field()
    house_link = scrapy.Field()
    published_in = scrapy.Field()
