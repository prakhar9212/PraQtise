# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-30 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=120)),
                ('description', models.TextField(default='description text')),
                ('phno', models.IntegerField(max_length=120)),
            ],
        ),
    ]