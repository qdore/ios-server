# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ios', '0006_auto_20150910_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_id', models.IntegerField(verbose_name='\u72b6\u6001ID')),
                ('comment_id', models.IntegerField(verbose_name='\u8bc4\u8bbaID')),
                ('commenter', models.CharField(max_length=11, verbose_name='\u8bc4\u8bba\u4eba\u624b\u673a\u53f7')),
                ('comment_by', models.CharField(max_length=11, verbose_name='\u88ab\u8bc4\u8bba\u4eba\u624b\u673a\u53f7')),
                ('comment_content', models.CharField(max_length=1000, verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba\u7ba1\u7406',
                'verbose_name_plural': '\u8bc4\u8bba\u7ba1\u7406',
            },
        ),
        migrations.AlterField(
            model_name='users',
            name='token',
            field=models.CharField(default=b'pleVErcyZTtXPAMNLqubnsKxJDWFRfzaHwCjBkSoYmvGIUQOgd', unique=True, max_length=50, verbose_name='Token'),
        ),
    ]
