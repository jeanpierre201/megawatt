# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0005_auto_20150226_2259'),
        ('summary', '0004_auto_20150228_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sitios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sitio', models.ForeignKey(to='sites.Sites')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
