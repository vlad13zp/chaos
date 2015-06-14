# -*- coding: utf-8 -*-

# Scrapy settings for mess project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mess'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['mess.spiders']
NEWSPIDER_MODULE = 'mess.spiders'
DEFAULT_ITEM_CLASS = 'mess.items.Website'
ITEM_PIPELINES = {'mess.pipelines.JsonWriterPipeline': 1}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mess (+http://www.yourdomain.com)'
