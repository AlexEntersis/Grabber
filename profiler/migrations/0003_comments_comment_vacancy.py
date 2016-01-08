# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiler', '0002_remove_comments_vacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_vacancy',
            field=models.CharField(max_length=20, default=None),
        ),
    ]
