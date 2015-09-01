# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='token',
            field=models.CharField(default=b'dSykfZElURXiJzaGxoIMnhOYcKADWmBuNbQsqpLHFVjevtPrgT', unique=True, max_length=50, verbose_name='Token'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_type',
            field=models.CharField(max_length=20, verbose_name='\u7528\u6237\u89d2\u8272', choices=[(b'0', b'\xe6\x91\x84\xe5\xbd\xb1\xe5\xb8\x88'), (b'1', b'\xe5\x88\xb6\xe7\x89\x87\xe4\xba\xba')]),
        ),
    ]
