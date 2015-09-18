# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ios', '0009_auto_20150917_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u5de5\u4f5c\u6807\u9898')),
                ('job', models.CharField(max_length=50, verbose_name='\u5de5\u4f5c\u5c97\u4f4d')),
                ('position', models.CharField(max_length=50, verbose_name='\u5de5\u4f5c\u5730\u5740')),
                ('content', models.CharField(max_length=500, verbose_name='\u5de5\u4f5c\u5185\u5bb9')),
                ('sponsor_name', models.CharField(max_length=20, verbose_name='\u53d1\u8d77\u8005')),
                ('sponsor_tel', models.CharField(max_length=11, verbose_name='\u53d1\u8d77\u8005\u624b\u673a')),
                ('status', models.CharField(max_length=30, verbose_name='\u5de5\u4f5c\u72b6\u6001', choices=[(b'0', b'\xe6\x8b\x9b\xe8\x81\x98\xe4\xb8\xad'), (b'1', b'\xe5\xb7\xb2\xe5\x88\x86\xe9\x85\x8d'), (b'2', b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')])),
                ('start_time', models.DateField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end_time', models.DateField(verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('pic', models.ImageField(upload_to=b'', verbose_name='\u5de5\u4f5c\u56fe\u7247')),
                ('appliers', models.CharField(max_length=500, verbose_name='\u7533\u8bf7\u8005')),
                ('approve_applier', models.CharField(max_length=11, verbose_name='\u786e\u8ba4\u5de5\u4f5c\u8005(\u7ba1\u7406\u5458\u8bf7\u586b\u5165\u624b\u673a\u53f7)')),
            ],
            options={
                'verbose_name': '\u5de5\u4f5c\u7ba1\u7406',
                'verbose_name_plural': '\u5de5\u4f5c\u7ba1\u7406',
            },
        ),
        migrations.AlterField(
            model_name='users',
            name='token',
            field=models.CharField(default=b'144256535418FLkRJdXiGoSDbpxZKtzWysNVvnIuHPErMlTcBa', unique=True, max_length=50, verbose_name='Token'),
        ),
    ]
