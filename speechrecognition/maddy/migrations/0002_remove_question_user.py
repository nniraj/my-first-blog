# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-07 13:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maddy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
    ]
