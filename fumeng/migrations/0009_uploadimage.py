# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fumeng', '0008_fumengbusiness_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe5\x9b\xbe\xe7\x89\x87')),
            ],
            options={
                'verbose_name': '\u56fe\u7247\u4e0a\u4f20',
                'verbose_name_plural': '\u56fe\u7247\u4e0a\u4f20',
            },
        ),
    ]
