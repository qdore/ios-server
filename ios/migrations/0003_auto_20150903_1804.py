# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ios', '0002_auto_20150903_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='PraiseStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_id', models.IntegerField(verbose_name='\u72b6\u6001ID')),
                ('tel', models.CharField(max_length=11, verbose_name='\u70b9\u8d5e\u4eba\u624b\u673a\u53f7')),
            ],
            options={
                'verbose_name': '\u70b9\u8d5e\u7ba1\u7406',
                'verbose_name_plural': '\u70b9\u8d5e\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tel', models.CharField(max_length=11, verbose_name='\u624b\u673a\u53f7')),
                ('brief', models.CharField(max_length=500, verbose_name='\u7b80\u4ecb')),
            ],
            options={
                'verbose_name': '\u72b6\u6001\u7ba1\u7406',
                'verbose_name_plural': '\u72b6\u6001\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='StatusPics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_id', models.IntegerField(verbose_name='\u72b6\u6001ID')),
                ('pic', models.ImageField(upload_to=b'', verbose_name='\u56fe\u7247')),
            ],
            options={
                'verbose_name': '\u56fe\u7247\u7ba1\u7406',
                'verbose_name_plural': '\u56fe\u7247\u7ba1\u7406',
            },
        ),
        migrations.AlterField(
            model_name='users',
            name='token',
            field=models.CharField(default=b'EsifXMTROKntjzdQocpWHvLGqAayBDZCPhJkmIbeFSurlNYUVw', unique=True, max_length=50, verbose_name='Token'),
        ),
    ]
