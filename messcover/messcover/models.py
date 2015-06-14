from django.db import models


class CrawlUrl(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=300, default='name url')
    code = models.IntegerField()

    def __unicode__(self):
        return '{0} ( {1} )'.format(self.name, self.code)


class ParseUrls(models.Model):
    id_url = models.ForeignKey(CrawlUrl)
    urls = models.CharField(max_length=200)
    name = models.CharField(max_length=300, default='name url')

    def __unicode__(self):
        return '{0} --> {1} ( {2} )'.format(self.id_url, self.name, self.urls)
