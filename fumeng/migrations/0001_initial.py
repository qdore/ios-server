# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allcolumns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('column_id', models.IntegerField()),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Homeads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'photos')),
                ('add_date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Infodetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('column_id', models.IntegerField()),
                ('category_id', models.IntegerField(blank=True)),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=100)),
                ('add_date', models.DateField(null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'photos')),
            ],
        ),
        migrations.CreateModel(
            name='Maincolumns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('column_id', models.IntegerField()),
                ('image', models.ImageField(upload_to=b'photos')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
