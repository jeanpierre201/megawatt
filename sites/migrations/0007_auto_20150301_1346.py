# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0006_auto_20150228_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valueA', models.IntegerField(default=0)),
                ('valueB', models.IntegerField(default=0)),
                ('entry_date', models.DateField(verbose_name=b'date inserted')),
                ('site', models.ForeignKey(to='sites.Sites')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='entry',
            name='site',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
