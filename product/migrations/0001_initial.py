# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='nil', max_length=30, null=True)),
                ('author', models.CharField(default='nil', max_length=30, null=True)),
                ('date', models.DateField(null=True)),
                ('price', models.FloatField(default=0, null=True)),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('soldcount', models.IntegerField(default=0, null=True)),
                ('category', models.CharField(default='nil', max_length=30, null=True)),
            ],
        ),
    ]