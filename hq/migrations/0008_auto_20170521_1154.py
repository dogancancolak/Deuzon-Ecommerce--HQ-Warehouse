# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hq', '0007_auto_20170521_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='ord_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='order.Order'),
        ),
    ]