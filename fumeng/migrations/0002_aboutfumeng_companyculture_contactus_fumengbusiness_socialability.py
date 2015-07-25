# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fumeng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutFumeng',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fumenggaishu', ckeditor.fields.RichTextField(verbose_name='\u798f\u68a6\u6982\u8ff0')),
                ('fumengzhanlve', ckeditor.fields.RichTextField(verbose_name='\u798f\u68a6\u6218\u7565')),
                ('hexinyoushi', ckeditor.fields.RichTextField(verbose_name='\u6838\u5fc3\u4f18\u52bf')),
                ('fazhanlicheng', ckeditor.fields.RichTextField(verbose_name='\u53d1\u5c55\u5386\u7a0b')),
            ],
            options={
                'verbose_name': '\u5173\u4e8e\u798f\u68a6',
                'verbose_name_plural': '\u5173\u4e8e\u798f\u68a6',
            },
        ),
        migrations.CreateModel(
            name='CompanyCulture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guanlizhidao', ckeditor.fields.RichTextField(verbose_name='\u7ba1\u7406\u4e4b\u9053')),
                ('qiyezongzhi', ckeditor.fields.RichTextField(verbose_name='\u4f01\u4e1a\u5b97\u65e8')),
                ('qiyejinshen', ckeditor.fields.RichTextField(verbose_name='\u4f01\u4e1a\u7cbe\u795e')),
                ('qiyezuoyong', ckeditor.fields.RichTextField(verbose_name=' \u4f01\u4e1a\u4f5c\u7528')),
            ],
            options={
                'verbose_name': '\u4f01\u4e1a\u6587\u5316',
                'verbose_name_plural': '\u4f01\u4e1a\u6587\u5316',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fumengzongbu', ckeditor.fields.RichTextField(verbose_name='\u798f\u68a6\u603b\u90e8')),
                ('xiashugongsi', ckeditor.fields.RichTextField(verbose_name='\u4e0b\u5c5e\u516c\u53f8')),
            ],
            options={
                'verbose_name': '\u793e\u4f1a\u8d23\u4efb',
                'verbose_name_plural': '\u793e\u4f1a\u8d23\u4efb',
            },
        ),
        migrations.CreateModel(
            name='FumengBusiness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shengtaizhongzhi', ckeditor.fields.RichTextField(verbose_name='\u798f\u68a6\u6982\u8ff0')),
                ('shengtaiyangzhi', ckeditor.fields.RichTextField(verbose_name='\u798f\u68a6\u6218\u7565')),
                ('kuangchanziyuan', ckeditor.fields.RichTextField(verbose_name='\u6838\u5fc3\u4f18\u52bf')),
            ],
            options={
                'verbose_name': '\u5173\u4e8e\u798f\u68a6',
                'verbose_name_plural': '\u5173\u4e8e\u798f\u68a6',
            },
        ),
        migrations.CreateModel(
            name='SocialAbility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gongyilinian', ckeditor.fields.RichTextField(verbose_name='\u516c\u76ca\u7406\u5ff5')),
                ('cishanjuanzhu', ckeditor.fields.RichTextField(verbose_name='\u6148\u5584\u6350\u52a9')),
                ('shehuizanyu', ckeditor.fields.RichTextField(verbose_name='\u793e\u4f1a\u8d5e\u8d4f')),
            ],
            options={
                'verbose_name': '\u793e\u4f1a\u8d23\u4efb',
                'verbose_name_plural': '\u793e\u4f1a\u8d23\u4efb',
            },
        ),
    ]
