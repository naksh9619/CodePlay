# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algo', models.CharField(max_length=1000)),
                ('descript', models.CharField(max_length=2000)),
                ('spaceComplexity', models.CharField(max_length=1000)),
                ('timeComlexity', models.CharField(max_length=1000)),
                ('links', models.CharField(max_length=2000)),
            ],
        ),
    ]
