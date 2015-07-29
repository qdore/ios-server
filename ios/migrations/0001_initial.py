# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tel', models.CharField(unique=True, max_length=11, verbose_name='\u624b\u673a\u53f7')),
                ('password', models.CharField(max_length=20, verbose_name='\u5bc6\u7801', choices=[(b'fumengxinwen', b'\xe7\xa6\x8f\xe6\xa2\xa6\xe6\x96\xb0\xe9\x97\xbb'), (b'diqudongtai', b'\xe5\x9c\xb0\xe5\x8c\xba\xe5\x8a\xa8\xe6\x80\x81'), (b'meitiguanzhu', b'\xe5\xaa\x92\xe4\xbd\x93\xe5\x85\xb3\xe6\xb3\xa8')])),
                ('user_id', models.CharField(default='admin', max_length=20, verbose_name='\u8eab\u4efd\u8bc1\u53f7\u6216\u5de5\u53f7')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u7ba1\u7406',
                'verbose_name_plural': '\u7528\u6237\u7ba1\u7406',
            },
        ),
    ]
