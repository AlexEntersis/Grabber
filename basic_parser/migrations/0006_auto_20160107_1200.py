# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_parser', '0005_profile_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='comments',
            field=models.ManyToManyField(to='profiler.Comments', default=None),
        ),
    ]
