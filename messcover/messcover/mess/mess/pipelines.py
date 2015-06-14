# -*- coding: utf-8 -*-
import json
#from messcover.models import CrawlUrl


class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        """
        """
        #CrawlUrl.objects.create(url=item['from_url'],
                               # name='Home page',
                              #  code=item['status'])

        return item
