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
                ('password', models.CharField(max_length=20, verbose_name='\u5bc6\u7801')),
                ('user_id', models.CharField(default='admin', unique=True, max_length=20, verbose_name='\u8eab\u4efd\u8bc1\u53f7\u6216\u5de5\u53f7')),
                ('user_type', models.CharField(max_length=20, verbose_name='\u7528\u6237\u89d2\u8272')),
                ('token', models.CharField(default=b'yzenETvBLkqcKutSVoJUsfRjACWaFZiHGmrbOgwPDlQdIMpNXx', unique=True, max_length=50, verbose_name='Token')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u7ba1\u7406',
                'verbose_name_plural': '\u7528\u6237\u7ba1\u7406',
            },
        ),
    ]
