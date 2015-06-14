# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors import LinkExtractor

from messcover.mess.mess.items import Website
from messcover.mess import actions


class MazySpider(CrawlSpider):

    name = "mazy"
    allowed_domains = ["localhost"]
    start_urls = [
        actions.get_start_url(),
    ]

    rules = [Rule
             (
                 LinkExtractor(
                     restrict_xpaths=('//a[@class="pageNext"]')),
                 callback = 'parse_links',
                 follow = True,
             )
             ]

    def parse_links(self, response):
        hxs = Selector(response)

        item = Website()

        item['from_url'] = response.url
        item['name'] = hxs.xpath('//a[@class="pageNext"]/text()').extract()
        item['url'] = hxs.xpath('//a[@class="pageNext"]/@href').extract()
        item['status'] = response.status

        need_url = actions.save_crawl(item['from_url'], item['status'])

        if len(item['url']) > 6:
            actions.save_parse(item['url'], item['name'], need_url)

        return item
