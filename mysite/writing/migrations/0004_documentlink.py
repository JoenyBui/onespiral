# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-29 05:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0003_auto_20171227_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.IntegerField(default=0)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_link_from_user', to='writing.Writer')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_link_to_userr', to='writing.Writer')),
            ],
        ),
    ]
