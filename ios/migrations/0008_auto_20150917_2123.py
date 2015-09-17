# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ios', '0007_auto_20150912_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='head_photo',
            field=models.ImageField(default='', upload_to=b'', verbose_name='\u5934\u50cf'),
        ),
        migrations.AlterField(
            model_name='users',
            name='token',
            field=models.CharField(default=b'zyOoQhwseqxVMCLKWJHtpkiYDjlTNEBcaZdmgXRFAfuGPnIbrv', unique=True, max_length=50, verbose_name='Token'),
        ),
    ]
