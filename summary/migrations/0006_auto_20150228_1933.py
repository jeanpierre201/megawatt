# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0005_sitios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitios',
            name='sitio',
        ),
        migrations.DeleteModel(
            name='Sitios',
        ),
    ]
