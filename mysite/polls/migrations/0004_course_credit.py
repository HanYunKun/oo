# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_course_current'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credit',
            field=models.IntegerField(default=2),
        ),
    ]