# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_auto_20150226_1830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='valueA_num',
            new_name='valueA',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='valueB_num',
            new_name='valueB',
        ),
    ]
