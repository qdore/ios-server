# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='token',
            field=models.CharField(default=b'jHKdXOyakomnGNCJrtVvELhuARzgQwslUYqTiWFIcbBMZDSexf', unique=True, max_length=50, verbose_name='Token'),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=20, verbose_name='\u5bc6\u7801'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.CharField(default='admin', unique=True, max_length=20, verbose_name='\u8eab\u4efd\u8bc1\u53f7\u6216\u5de5\u53f7'),
        ),
    ]
