# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-15 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagsecond',
            name='tag',
            field=models.CharField(max_length=20, verbose_name='二级标签'),
        ),
    ]
