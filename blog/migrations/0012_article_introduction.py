# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 02:10
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170512_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='introduction',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容'),
        ),
    ]
