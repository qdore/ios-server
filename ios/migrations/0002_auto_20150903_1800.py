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
            field=models.CharField(default=b'tAxzhYTjKvpLXwJrWOPbyBnlMqeCRcSGskuHgINQUEFdDmiZVo', unique=True, max_length=50, verbose_name='Token'),
        ),
    ]
