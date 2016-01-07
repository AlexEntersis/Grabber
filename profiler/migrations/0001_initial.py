# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=300)),
                ('comment_date', models.DateField(default=None)),
                ('comment_text', models.TextField(default=None)),
                ('vacancy', models.CharField(max_length=10, choices=[('QA', 'Quality Assurance'), ('JAVA', 'Java Developer'), ('C++', 'C++ Developer')])),
            ],
        ),
    ]