# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-26 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190724_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='uv',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
