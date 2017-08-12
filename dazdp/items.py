# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item

class DianpingItem(Item):
    _id = Field()
    item_name = Field()
    location = Field()
    shopname = Field()
    shoplevel = Field()
    shopurl = Field()
    commentnum = Field()
    avgcost = Field()
    taste = Field()
    envi = Field()
    service = Field()
    foodtype = Field()
    loc = Field()


