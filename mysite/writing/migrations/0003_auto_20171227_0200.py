# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-27 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0002_auto_20171226_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='modified',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
