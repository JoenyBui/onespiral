# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-30 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0007_auto_20171230_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentlink',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
