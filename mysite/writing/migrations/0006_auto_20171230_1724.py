# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-30 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0005_auto_20171229_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentlink',
            name='from_user',
        ),
        migrations.AddField(
            model_name='documentlink',
            name='document',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='writing.Document'),
            preserve_default=False,
        ),
    ]