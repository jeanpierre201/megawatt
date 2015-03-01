# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_auto_20150226_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valueA_num', models.IntegerField(default=0)),
                ('valueB_num', models.IntegerField(default=0)),
                ('entry_date', models.DateTimeField(verbose_name=b'date inserted')),
                ('entry', models.ForeignKey(to='sites.Sites')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='values',
            name='value',
        ),
        migrations.DeleteModel(
            name='Values',
        ),
    ]
