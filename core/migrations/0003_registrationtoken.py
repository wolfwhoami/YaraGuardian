# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-06-29 18:39
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170302_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('token', models.CharField(default=core.models.RegistrationToken.generate_token, max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
