# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='current',
            field=models.IntegerField(default=0),
        ),
    ]
