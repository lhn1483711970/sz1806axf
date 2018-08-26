# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-18 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20180818_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='axf_foodtypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=20)),
                ('typename', models.CharField(max_length=50)),
                ('childtypenames', models.CharField(max_length=50)),
                ('typesort', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
    ]
