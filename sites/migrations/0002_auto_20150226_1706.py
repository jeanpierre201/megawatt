# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sites',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='values',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 26, 16, 6, 54, 31300, tzinfo=utc), verbose_name=b'date inserted'),
            preserve_default=False,
        ),
    ]
