# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0005_auto_20150226_2259'),
        ('summary', '0002_auto_20150227_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valueA_avg', models.IntegerField(default=0)),
                ('valueB_avg', models.IntegerField(default=0)),
                ('entry_avg', models.ForeignKey(to='sites.Entry')),
                ('site_avg', models.ForeignKey(to='sites.Sites')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
