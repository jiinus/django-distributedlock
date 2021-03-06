# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Lock',
                'verbose_name_plural': 'Locks',
            },
        ),
    ]
