# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 04:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170512_1249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '类别', 'verbose_name_plural': '类别'},
        ),
        migrations.AlterModelOptions(
            name='navigation',
            options={'verbose_name': '导航栏目', 'verbose_name_plural': '导航栏目'},
        ),
    ]
