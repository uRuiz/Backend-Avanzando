# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20161024_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_resized',
            field=models.BooleanField(default=False),
        ),
    ]
