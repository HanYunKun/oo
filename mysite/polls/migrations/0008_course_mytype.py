# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20170531_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='mytype',
            field=models.CharField(default='\u5fc5\u4fee', max_length=7),
        ),
    ]
