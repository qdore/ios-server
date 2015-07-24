# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_1', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe6\xb5\xb7\xe6\x8a\xa5\xe5\x9b\xbe1')),
                ('url_1', models.CharField(max_length=1000, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe6\xb5\xb7\xe6\x8a\xa5\xe5\x9b\xbe1\xe9\x93\xbe\xe6\x8e\xa5')),
            ],
            options={
                'verbose_name': '\u9996\u9875\u8bbe\u7f6e',
                'verbose_name_plural': '\u9996\u9875\u8bbe\u7f6e',
            },
        ),
    ]
