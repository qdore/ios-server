# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fumeng', '0004_auto_20150726_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutfumeng',
            name='fazhanlicheng',
            field=models.TextField(max_length=10000, verbose_name='\u53d1\u5c55\u5386\u7a0b<html>'),
        ),
        migrations.AlterField(
            model_name='aboutfumeng',
            name='fumenggaishu',
            field=models.TextField(max_length=10000, verbose_name='\u798f\u68a6\u6982\u8ff0<html>'),
        ),
        migrations.AlterField(
            model_name='aboutfumeng',
            name='fumengzhanlve',
            field=models.TextField(max_length=10000, verbose_name='\u798f\u68a6\u6218\u7565<html>'),
        ),
        migrations.AlterField(
            model_name='aboutfumeng',
            name='hexinyoushi',
            field=models.TextField(max_length=10000, verbose_name='\u6838\u5fc3\u4f18\u52bf<html>'),
        ),
        migrations.AlterField(
            model_name='companyculture',
            name='guanlizhidao',
            field=models.TextField(max_length=10000, verbose_name='\u7ba1\u7406\u4e4b\u9053<html>'),
        ),
        migrations.AlterField(
            model_name='companyculture',
            name='qiyejinshen',
            field=models.TextField(max_length=10000, verbose_name='\u4f01\u4e1a\u7cbe\u795e<html>'),
        ),
        migrations.AlterField(
            model_name='companyculture',
            name='qiyezongzhi',
            field=models.TextField(max_length=10000, verbose_name='\u4f01\u4e1a\u5b97\u65e8<html>'),
        ),
        migrations.AlterField(
            model_name='companyculture',
            name='qiyezuoyong',
            field=models.TextField(max_length=10000, verbose_name=' \u4f01\u4e1a\u4f5c\u7528<html>'),
        ),
        migrations.AlterField(
            model_name='fumengbusiness',
            name='kuangchanziyuan',
            field=models.TextField(max_length=10000, verbose_name='\u77ff\u4ea7\u8d44\u6e90<html>'),
        ),
        migrations.AlterField(
            model_name='fumengbusiness',
            name='shengtaiyangzhi',
            field=models.TextField(max_length=10000, verbose_name='\u751f\u6001\u517b\u6b96<html>'),
        ),
        migrations.AlterField(
            model_name='fumengbusiness',
            name='shengtaizhongzhi',
            field=models.TextField(max_length=10000, verbose_name='\u751f\u6001\u79cd\u690d<html>'),
        ),
        migrations.AlterField(
            model_name='socialability',
            name='cishanjuanzhu',
            field=models.TextField(max_length=10000, verbose_name='\u6148\u5584\u6350\u52a9<html>'),
        ),
        migrations.AlterField(
            model_name='socialability',
            name='gongyilinian',
            field=models.TextField(max_length=10000, verbose_name='\u516c\u76ca\u7406\u5ff5<html>'),
        ),
        migrations.AlterField(
            model_name='socialability',
            name='shehuizanyu',
            field=models.TextField(max_length=10000, verbose_name='\u793e\u4f1a\u8d5e\u8d4f<html>'),
        ),
    ]
