# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ios', '0004_auto_20150903_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttentionRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attent_tel', models.CharField(max_length=11, verbose_name='\u5173\u6ce8\u4eba\u624b\u673a\u53f7')),
                ('tel_by_attent', models.CharField(max_length=11, verbose_name='\u88ab\u5173\u6ce8\u4eba\u624b\u673a\u53f7')),
            ],
            options={
                'verbose_name': '\u5173\u6ce8\u4fe1\u606f\u7ba1\u7406',
                'verbose_name_plural': '\u5173\u6ce8\u4fe1\u606f\u7ba1\u7406',
            },
        ),
        migrations.AlterField(
            model_name='users',
            name='token',
            field=models.CharField(default=b'blBoFOUuEMLznShIeHiYxjGXsTZQyKWfcVPRvJAgakDwqrpdNm', unique=True, max_length=50, verbose_name='Token'),
        ),
    ]
