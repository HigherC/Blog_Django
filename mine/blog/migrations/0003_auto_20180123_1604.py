# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-23 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180116_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='content',
            field=models.TextField(),
        ),
    ]
