# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ios', '0003_auto_20150903_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='token',
            field=models.CharField(default=b'kprWmTCbUNGxMRsKAqnILFhDdYJwuQifZVyvBjSgPoXHOzetlE', unique=True, max_length=50, verbose_name='Token'),
        ),
    ]
