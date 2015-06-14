# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mazypages', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thema', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]
