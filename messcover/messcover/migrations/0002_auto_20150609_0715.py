# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messcover', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawlurl',
            name='name',
            field=models.CharField(default=b'name url', max_length=300),
        ),
        migrations.AddField(
            model_name='parseurls',
            name='name',
            field=models.CharField(default=b'name url', max_length=300),
        ),
    ]
