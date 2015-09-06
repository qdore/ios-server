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
                ('user_type', models.CharField(max_length=20, verbose_name='\u7528\u6237\u89d2\u8272', choices=[(b'0', b'\xe6\x91\x84\xe5\xbd\xb1\xe5\xb8\x88'), (b'1', b'\xe5\x88\xb6\xe7\x89\x87\xe4\xba\xba')])),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('gender', models.CharField(max_length=20, verbose_name='\u6027\u522b', choices=[(b'0', b'\xe7\x94\xb7'), (b'1', b'\xe5\xa5\xb3')])),
                ('brief', models.CharField(max_length=500, verbose_name='\u7b80\u4ecb')),
                ('token', models.CharField(default=b'wWDCiNcXOpPxGBZbvukqoeraFKTLJjAsQSIzlVtRMmyfHdEnUh', unique=True, max_length=50, verbose_name='Token')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u7ba1\u7406',
                'verbose_name_plural': '\u7528\u6237\u7ba1\u7406',
            },
        ),
    ]
