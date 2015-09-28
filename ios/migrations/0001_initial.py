# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyOut',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tel', models.CharField(max_length=11, verbose_name='\u624b\u673a\u53f7')),
                ('start_time', models.CharField(max_length=30, verbose_name='\u5916\u51fa\u65f6\u95f4')),
                ('end_time', models.CharField(max_length=30, verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('reason', models.CharField(max_length=500, verbose_name='\u5916\u51fa\u539f\u56e0')),
            ],
            options={
                'verbose_name': '\u5916\u51fa\u7533\u8bf7\u7ba1\u7406',
                'verbose_name_plural': '\u5916\u51fa\u7533\u8bf7\u7ba1\u7406',
            },
        ),
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
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.CharField(max_length=11, verbose_name='\u53d1\u9001\u8005\u624b\u673a\u53f7')),
                ('reciver', models.CharField(max_length=11, verbose_name='\u63a5\u53d7\u8005\u624b\u673a\u53f7')),
                ('content', models.CharField(max_length=1000, verbose_name='\u804a\u5929\u5185\u5bb9')),
                ('readed', models.BooleanField(default=False, verbose_name='\u5df2\u8bfb')),
            ],
            options={
                'verbose_name': '\u804a\u5929\u5185\u5bb9\u7ba1\u7406',
                'verbose_name_plural': '\u804a\u5929\u5185\u5bb9\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_id', models.IntegerField(verbose_name='\u72b6\u6001ID')),
                ('comment_id', models.IntegerField(verbose_name='\u8bc4\u8bbaID')),
                ('commenter', models.CharField(max_length=11, verbose_name='\u8bc4\u8bba\u4eba\u624b\u673a\u53f7')),
                ('comment_by', models.CharField(max_length=11, verbose_name='\u88ab\u8bc4\u8bba\u4eba\u624b\u673a\u53f7')),
                ('comment_content', models.CharField(max_length=1000, verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba\u7ba1\u7406',
                'verbose_name_plural': '\u8bc4\u8bba\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u516c\u53f8/\u6d3b\u52a8\u540d\u79f0')),
                ('user_time', models.CharField(max_length=50, verbose_name='\u4f7f\u7528\u65f6\u95f4')),
                ('city', models.CharField(max_length=50, verbose_name='\u57ce\u5e02')),
                ('authorizer', models.CharField(max_length=50, verbose_name='\u6279\u51c6\u4eba')),
                ('position', models.CharField(max_length=50, verbose_name='\u5de5\u4f5c\u5355\u4f4d')),
                ('reason', models.CharField(max_length=500, verbose_name='\u7533\u8bf7\u7406\u7531')),
                ('details', models.CharField(max_length=500, verbose_name='\u8bbe\u5907\u53ca\u4eba\u5458\u660e\u7ec6')),
                ('opinion', models.CharField(max_length=500, verbose_name='\u9886\u5bfc\u4eba\u610f\u89c1')),
                ('memo', models.CharField(max_length=500, verbose_name='\u5907\u6ce8')),
                ('sponsor_name', models.CharField(max_length=20, verbose_name='\u7533\u8bf7\u4eba\u59d3\u540d')),
                ('studio', models.CharField(max_length=20, verbose_name='\u6f14\u64ad\u5ba4')),
                ('job_number', models.CharField(max_length=20, verbose_name='\u90e8\u95e8/\u5de5\u53f7')),
                ('sponsor_tel', models.CharField(max_length=11, verbose_name='\u53d1\u8d77\u8005\u624b\u673a')),
                ('camera', models.CharField(max_length=20, verbose_name='\u6444\u5f71\u673a')),
                ('broadcast_car', models.CharField(max_length=20, verbose_name='\u8f6c\u64ad\u8f66')),
                ('later_period', models.CharField(max_length=20, verbose_name='\u540e\u671f')),
                ('status', models.CharField(max_length=30, verbose_name='\u5de5\u4f5c\u72b6\u6001', choices=[(b'0', b'\xe6\x8b\x9b\xe8\x81\x98\xe4\xb8\xad'), (b'1', b'\xe5\xb7\xb2\xe5\x88\x86\xe9\x85\x8d'), (b'2', b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')])),
                ('time', models.CharField(max_length=30, verbose_name='\u7533\u8bf7\u65e5\u671f')),
                ('pic', models.ImageField(upload_to=b'', verbose_name='\u5de5\u4f5c\u56fe\u7247')),
                ('appliers', models.CharField(max_length=500, verbose_name='\u7533\u8bf7\u8005')),
                ('approve_applier', models.CharField(max_length=11, verbose_name='\u786e\u8ba4\u5de5\u4f5c\u8005(\u7ba1\u7406\u5458\u8bf7\u586b\u5165\u624b\u673a\u53f7)')),
            ],
            options={
                'verbose_name': '\u5de5\u4f5c\u7ba1\u7406',
                'verbose_name_plural': '\u5de5\u4f5c\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='PraiseStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_id', models.IntegerField(verbose_name='\u72b6\u6001ID')),
                ('tel', models.CharField(max_length=11, verbose_name='\u70b9\u8d5e\u4eba\u624b\u673a\u53f7')),
            ],
            options={
                'verbose_name': '\u70b9\u8d5e\u7ba1\u7406',
                'verbose_name_plural': '\u70b9\u8d5e\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tel', models.CharField(max_length=11, verbose_name='\u624b\u673a\u53f7')),
                ('brief', models.CharField(max_length=500, verbose_name='\u7b80\u4ecb')),
            ],
            options={
                'verbose_name': '\u72b6\u6001\u7ba1\u7406',
                'verbose_name_plural': '\u72b6\u6001\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='StatusPics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_id', models.IntegerField(verbose_name='\u72b6\u6001ID')),
                ('pic', models.ImageField(upload_to=b'', verbose_name='\u56fe\u7247')),
            ],
            options={
                'verbose_name': '\u56fe\u7247\u7ba1\u7406',
                'verbose_name_plural': '\u56fe\u7247\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tel', models.CharField(unique=True, max_length=11, verbose_name='\u624b\u673a\u53f7')),
                ('password', models.CharField(max_length=20, verbose_name='\u5bc6\u7801')),
                ('user_id', models.CharField(default='admin', unique=True, max_length=20, verbose_name='\u8eab\u4efd\u8bc1\u53f7\u6216\u5de5\u53f7')),
                ('head_photo', models.ImageField(upload_to=b'', verbose_name='\u5934\u50cf')),
                ('user_type', models.CharField(max_length=20, verbose_name='\u7528\u6237\u89d2\u8272', choices=[(b'0', b'\xe6\x91\x84\xe5\xbd\xb1\xe5\xb8\x88'), (b'1', b'\xe5\x88\xb6\xe7\x89\x87\xe4\xba\xba')])),
                ('name', models.CharField(max_length=20, verbose_name='\u7528\u6237\u540d')),
                ('gender', models.CharField(max_length=20, verbose_name='\u6027\u522b', choices=[(b'0', b'\xe7\x94\xb7'), (b'1', b'\xe5\xa5\xb3')])),
                ('brief', models.CharField(max_length=500, verbose_name='\u7b80\u4ecb')),
                ('token', models.CharField(default=b'14429863667hpyEZagiPdnFzSQOmxuWjMCcAtVwkeTKfqDGNo', unique=True, max_length=50, verbose_name='Token')),
                ('true_name', models.CharField(max_length=20, verbose_name='\u771f\u5b9e\u59d3\u540d')),
                ('identity', models.CharField(max_length=18, verbose_name='\u8eab\u4efd\u8bc1\u53f7')),
                ('identity_photo', models.ImageField(upload_to=b'', verbose_name='\u8eab\u4efd\u8bc1\u7167\u7247')),
                ('work_photo', models.ImageField(upload_to=b'', verbose_name='\u5de5\u4f5c\u8bc1\u7167\u7247')),
                ('is_verified', models.CharField(default=b'0', max_length=1, verbose_name='\u5ba1\u6838\u72b6\u6001')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u7ba1\u7406',
                'verbose_name_plural': '\u7528\u6237\u7ba1\u7406',
            },
        ),
    ]
