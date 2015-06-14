from django.db import models


class Route(models.Model):
    start_route = models.CharField(max_length=200)
    end_route = models.CharField(max_length=200)

    def __unicode__(self):
        return 'From {0} to {1}'.format(self.start_route, self.end_route)


class User(models.Model):
    name_user = models.CharField(max_length=100)
    status_user = models.IntegerField()

    def __unicode__(self):
        return '{0}'.format(self.name_user)


class Plan(models.Model):
    thema = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    status = models.IntegerField()

    def __unicode__(self):
        return '{0} ({1}) - {2}'.format(self.thema, self.date_time, self.status)
