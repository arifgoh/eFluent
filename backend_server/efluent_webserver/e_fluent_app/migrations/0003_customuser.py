# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-04 08:37
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('e_fluent_app', '0002_auto_20160503_0753'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]