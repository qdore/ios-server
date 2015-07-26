# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fumeng', '0005_auto_20150726_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='HumanResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('renlilinian', models.TextField(max_length=10000, verbose_name='\u4eba\u529b\u7406\u5ff5<html>')),
                ('shehuizhaopin', models.TextField(max_length=10000, verbose_name='\u793e\u4f1a\u62db\u8058<html>')),
                ('xiaoyuanzhaopin', models.TextField(max_length=10000, verbose_name='\u6821\u56ed\u62db\u8058<html>')),
            ],
            options={
                'verbose_name': '\u4eba\u529b\u8d44\u6e90',
                'verbose_name_plural': '\u4eba\u529b\u8d44\u6e90',
            },
        ),
    ]
