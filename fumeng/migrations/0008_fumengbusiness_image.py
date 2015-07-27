# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fumeng', '0007_auto_20150727_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='fumengbusiness',
            name='image',
            field=models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe9\xa2\x84\xe8\xa7\x88\xe5\x9b\xbe'),
        ),
    ]
