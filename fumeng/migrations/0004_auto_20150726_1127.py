# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fumeng', '0003_auto_20150725_1816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fumengbusiness',
            options={'verbose_name': '\u798f\u68a6\u4e1a\u52a1', 'verbose_name_plural': '\u798f\u68a6\u4e1a\u52a1'},
        ),
        migrations.AlterField(
            model_name='aboutfumeng',
            name='fazhanlicheng',
            field=models.TextField(max_length=10000, verbose_name='\u53d1\u5c55\u5386\u7a0b'),
        ),
        migrations.AlterField(
            model_name='aboutfumeng',
            name='fumenggaishu',
            field=models.TextField(max_length=10000, verbose_name='\u798f\u68a6\u6982\u8ff0'),
        ),
        migrations.AlterField(
            model_name='aboutfumeng',
            name='fumengzhanlve',
            field=models.TextField(max_length=10000, verbose_name='\u798f\u68a6\u6218\u7565'),
        ),
        migrations.AlterField(
            model_name='aboutfumeng',
            name='hexinyoushi',
            field=models.TextField(max_length=10000, verbose_name='\u6838\u5fc3\u4f18\u52bf'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_type',
            field=models.CharField(max_length=100, verbose_name='\u65b0\u95fb\u7c7b\u578b', choices=[(b'fumengxinwen', b'\xe7\xa6\x8f\xe6\xa2\xa6\xe6\x96\xb0\xe9\x97\xbb'), (b'diqudongtai', b'\xe5\x9c\xb0\xe5\x8c\xba\xe5\x8a\xa8\xe6\x80\x81'), (b'meitiguanzhu', b'\xe5\xaa\x92\xe4\xbd\x93\xe5\x85\xb3\xe6\xb3\xa8')]),
        ),
    ]
