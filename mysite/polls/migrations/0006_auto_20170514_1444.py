# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 06:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20170514_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='_type',
            new_name='mytype',
        ),
        migrations.RenameField(
            model_name='process',
            old_name='_type',
            new_name='mytype',
        ),
    ]