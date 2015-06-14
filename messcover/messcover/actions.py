from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from mess.mess.spiders.mess_spider import MazySpider
from scrapy.utils.project import get_project_settings
from messcover.models import CrawlUrl, ParseUrls


def run_spider():
    spider = MazySpider()
    settings = get_project_settings()
    crawler = Crawler(settings)
    crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()
    log.start()
    # the script will block here until the spider_closed signal was sent
    reactor.run(installSignalHandlers=0)


def clear_base():
    CrawlUrl.objects.all().delete()
    ParseUrls.objects.all().delete()


def get_main_urls():
    urls = [
        url for url in CrawlUrl.objects.all()
    ]

    return urls


def get_help_urls():
    urls = [
        url for url in ParseUrls.objects.all()
    ]

    return urls
