# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-14 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
