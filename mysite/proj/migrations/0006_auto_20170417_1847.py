# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0005_auto_20170417_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='blurb',
            name='current_page',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='total_pages',
            field=models.IntegerField(null=True),
        ),
    ]
