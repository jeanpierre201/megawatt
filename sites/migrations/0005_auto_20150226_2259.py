# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0004_auto_20150226_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='entry',
            new_name='site',
        ),
    ]
