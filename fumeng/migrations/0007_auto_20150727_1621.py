# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fumeng', '0006_humanresource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fumengbusiness',
            name='kuangchanziyuan',
        ),
        migrations.RemoveField(
            model_name='fumengbusiness',
            name='shengtaiyangzhi',
        ),
        migrations.RemoveField(
            model_name='fumengbusiness',
            name='shengtaizhongzhi',
        ),
        migrations.AddField(
            model_name='fumengbusiness',
            name='content',
            field=ckeditor.fields.RichTextField(default=b'', verbose_name='\u5185\u5bb9'),
        ),
        migrations.AddField(
            model_name='fumengbusiness',
            name='news_type',
            field=models.CharField(default=b'\xe7\x94\x9f\xe6\x80\x81\xe7\xa7\x8d\xe6\xa4\x8d', max_length=100, verbose_name='\u798f\u68a6\u4e1a\u52a1\u7c7b\u578b', choices=[(b'shengtaizhongzhi', b'\xe7\x94\x9f\xe6\x80\x81\xe7\xa7\x8d\xe6\xa4\x8d'), (b'shengtaiyangzhi', b'\xe7\x94\x9f\xe6\x80\x81\xe5\x85\xbb\xe6\xae\x96'), (b'kuangchanziyuan', b'\xe7\x9f\xbf\xe4\xba\xa7\xe8\xb5\x84\xe6\xba\x90')]),
        ),
        migrations.AddField(
            model_name='fumengbusiness',
            name='title',
            field=models.CharField(default=b'', max_length=500, verbose_name='\u798f\u68a6\u4e1a\u52a1\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='fumengzongbu',
            field=models.TextField(max_length=10000, verbose_name='\u798f\u68a6\u603b\u90e8<html>'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='xiashugongsi',
            field=models.TextField(max_length=10000, verbose_name='\u4e0b\u5c5e\u516c\u53f8<html>'),
        ),
    ]
