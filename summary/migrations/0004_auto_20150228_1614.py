# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0003_sum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sum',
            name='entry_avg',
        ),
        migrations.RemoveField(
            model_name='sum',
            name='site_avg',
        ),
        migrations.DeleteModel(
            name='Sum',
        ),
    ]
