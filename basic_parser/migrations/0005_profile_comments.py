# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiler', '0001_initial'),
        ('basic_parser', '0004_auto_20151003_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='comments',
            field=models.ManyToManyField(null=True, to='profiler.Comments', default=None),
        ),
    ]
