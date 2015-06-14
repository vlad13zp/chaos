# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class Website(Item):
    from_url = Field()
    name = Field()
    url = Field()
    status = Field()
