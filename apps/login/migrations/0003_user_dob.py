# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20161030_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]