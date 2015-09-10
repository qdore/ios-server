# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ios', '0005_auto_20150907_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.CharField(max_length=11, verbose_name='\u53d1\u9001\u8005\u624b\u673a\u53f7')),
                ('reciver', models.CharField(max_length=11, verbose_name='\u63a5\u53d7\u8005\u624b\u673a\u53f7')),
                ('content', models.CharField(max_length=1000, verbose_name='\u804a\u5929\u5185\u5bb9')),
                ('readed', models.BooleanField(default=False, verbose_name='\u5df2\u8bfb')),
            ],
            options={
                'verbose_name': '\u804a\u5929\u5185\u5bb9\u7ba1\u7406',
                'verbose_name_plural': '\u804a\u5929\u5185\u5bb9\u7ba1\u7406',
            },
        ),
        migrations.AlterField(
            model_name='users',
            name='token',
            field=models.CharField(default=b'eHcSXNbKYymaMFzrjhdxJDCkVpOugfABwUlqtsGTnRZiWQEIPv', unique=True, max_length=50, verbose_name='Token'),
        ),
    ]
