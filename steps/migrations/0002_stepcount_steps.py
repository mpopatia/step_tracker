# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stepcount',
            name='steps',
            field=models.IntegerField(default=0),
        ),
    ]
