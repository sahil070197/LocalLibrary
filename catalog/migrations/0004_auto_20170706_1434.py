# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 09:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20170706_1432'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Samples',
            new_name='SamplesSinger',
        ),
    ]
