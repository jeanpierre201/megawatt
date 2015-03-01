# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0006_auto_20150228_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField()),
                ('parent', models.ForeignKey(blank=True, to='summary.Node', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
