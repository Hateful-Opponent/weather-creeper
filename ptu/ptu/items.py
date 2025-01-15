# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PtuItem(scrapy.Item):

    date = scrapy.Field()

    avange_high_temp = scrapy.Field()
    avange_low_temp = scrapy.Field()

    higgest_temp = scrapy.Field()
    lowest_temp = scrapy.Field()

    avange_air = scrapy.Field()
    best_air = scrapy.Field()
    worst_air = scrapy.Field()