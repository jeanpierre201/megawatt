# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0007_node'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Node',
        ),
    ]
