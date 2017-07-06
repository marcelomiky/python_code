# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#import scrapy


#class ScrapyCulturalSpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#    pass

from scrapy.item import Item, Field

class Atracao(Item):
    cidade = Field()
    endereco = Field()
    dia = Field()
    hora = Field()
    artista = Field()
