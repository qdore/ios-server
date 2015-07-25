# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fumeng', '0002_aboutfumeng_companyculture_contactus_fumengbusiness_socialability'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='\u65b0\u95fb\u6807\u9898')),
                ('news_type', models.CharField(max_length=30, verbose_name='\u65b0\u95fb\u7c7b\u578b', choices=[(b'\xe7\xa6\x8f\xe6\xa2\xa6\xe6\x96\xb0\xe9\x97\xbb', b'\xe7\xa6\x8f\xe6\xa2\xa6\xe6\x96\xb0\xe9\x97\xbb'), (b'\xe5\x9c\xb0\xe5\x8c\xba\xe5\x8a\xa8\xe6\x80\x81', b'\xe5\x9c\xb0\xe5\x8c\xba\xe5\x8a\xa8\xe6\x80\x81'), (b'\xe4\xb8\x8b\xe5\xb1\x9e\xe5\x85\xac\xe5\x8f\xb8', b'\xe4\xb8\x8b\xe5\xb1\x9e\xe5\x85\xac\xe5\x8f\xb8'), (b'\xe5\xaa\x92\xe4\xbd\x93\xe5\x85\xb3\xe6\xb3\xa8', b'\xe5\xaa\x92\xe4\xbd\x93\xe5\x85\xb3\xe6\xb3\xa8')])),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65e5\u671f')),
                ('add_by', models.CharField(default='admin', max_length=100, verbose_name='\u672c\u6587\u6765\u81ea')),
                ('content', ckeditor.fields.RichTextField(verbose_name='\u65b0\u95fb\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u65b0\u95fb\u7f16\u8f91',
                'verbose_name_plural': '\u65b0\u95fb\u7f16\u8f91',
            },
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': '\u8054\u7cfb\u6211\u4eec', 'verbose_name_plural': '\u8054\u7cfb\u6211\u4eec'},
        ),
    ]
