# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ios', '0008_auto_20150917_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='head_photo',
            field=models.ImageField(upload_to=b'', verbose_name='\u5934\u50cf'),
        ),
        migrations.AlterField(
            model_name='users',
            name='token',
            field=models.CharField(default=b'WmSoVNQKCpZEhlqUtPedfJugYxMAiLacBOnywDsrHRGXzITbkv', unique=True, max_length=50, verbose_name='Token'),
        ),
    ]
