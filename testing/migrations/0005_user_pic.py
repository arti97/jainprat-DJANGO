# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0004_auto_20170328_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.FileField(max_length=10485760, null=True, upload_to=b''),
        ),
    ]