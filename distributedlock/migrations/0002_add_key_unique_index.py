# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-03 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributedlock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lock',
            name='key',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]