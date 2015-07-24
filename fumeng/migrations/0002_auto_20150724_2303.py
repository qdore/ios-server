# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fumeng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_1', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe6\xb5\xb7\xe6\x8a\xa5\xe5\x9b\xbe1')),
                ('url_1', models.CharField(max_length=1000, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe6\xb5\xb7\xe6\x8a\xa5\xe5\x9b\xbe1\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_2', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe6\xb5\xb7\xe6\x8a\xa5\xe5\x9b\xbe2')),
                ('url_2', models.CharField(max_length=1000, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe6\xb5\xb7\xe6\x8a\xa5\xe5\x9b\xbe2\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_3', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe6\xb5\xb7\xe6\x8a\xa5\xe5\x9b\xbe3')),
                ('url_3', models.CharField(max_length=1000, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe6\xb5\xb7\xe6\x8a\xa5\xe5\x9b\xbe3\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_4', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe6\xb5\xb7\xe6\x8a\xa5\xe5\x9b\xbe4')),
                ('url_4', models.CharField(max_length=1000, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe6\xb5\xb7\xe6\x8a\xa5\xe5\x9b\xbe4\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_about', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe5\x85\xb3\xe4\xba\x8e\xe6\x88\x91\xe4\xbb\xac\xe5\x9b\xbe\xe7\x89\x87')),
                ('data_about', models.CharField(max_length=1000, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe5\x85\xb3\xe4\xba\x8e\xe6\x88\x91\xe4\xbb\xac\xe7\xae\x80\xe4\xbb\x8b')),
                ('url_about', models.CharField(max_length=1000, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe5\x85\xb3\xe4\xba\x8e\xe6\x88\x91\xe4\xbb\xac\xe7\xae\x80\xe4\xbb\x8b\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_shengtaizhongzhi_1', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe7\xa7\x8d\xe6\xa4\x8d\xe5\x9b\xbe\xe7\x89\x871')),
                ('data_shengtaizhongzhi_1', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe7\xa7\x8d\xe6\xa4\x8d\xe7\xae\x80\xe4\xbb\x8b1')),
                ('url_shengtaizhongzhi_1', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe7\xa7\x8d\xe6\xa4\x8d\xe7\xae\x80\xe4\xbb\x8b1\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_shengtaizhongzhi_2', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe7\xa7\x8d\xe6\xa4\x8d\xe5\x9b\xbe\xe7\x89\x872')),
                ('data_shengtaizhongzhi_2', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe7\xa7\x8d\xe6\xa4\x8d\xe7\xae\x80\xe4\xbb\x8b2')),
                ('url_shengtaizhongzhi_2', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe7\xa7\x8d\xe6\xa4\x8d\xe7\xae\x80\xe4\xbb\x8b2\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_shengtaizhongzhi_3', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe7\xa7\x8d\xe6\xa4\x8d\xe5\x9b\xbe\xe7\x89\x873')),
                ('data_shengtaizhongzhi_3', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe7\xa7\x8d\xe6\xa4\x8d\xe7\xae\x80\xe4\xbb\x8b3')),
                ('url_shengtaizhongzhi_3', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe7\xa7\x8d\xe6\xa4\x8d\xe7\xae\x80\xe4\xbb\x8b3\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_shengtaizhongzhi_4', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe7\xa7\x8d\xe6\xa4\x8d\xe5\x9b\xbe\xe7\x89\x874')),
                ('data_shengtaizhongzhi_4', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe7\xa7\x8d\xe6\xa4\x8d\xe7\xae\x80\xe4\xbb\x8b4')),
                ('url_shengtaizhongzhi_4', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe7\xa7\x8d\xe6\xa4\x8d\xe7\xae\x80\xe4\xbb\x8b4\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_shengtaiyangzhi_1', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe5\x85\xbb\xe6\xae\x96\xe5\x9b\xbe\xe7\x89\x871')),
                ('data_shengtaiyangzhi_1', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe5\x85\xbb\xe6\xae\x96\xe7\xae\x80\xe4\xbb\x8b1')),
                ('url_shengtaiyangzhi_1', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe5\x85\xbb\xe6\xae\x96\xe7\xae\x80\xe4\xbb\x8b1\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_shengtaiyangzhi_2', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe5\x85\xbb\xe6\xae\x96\xe5\x9b\xbe\xe7\x89\x872')),
                ('data_shengtaiyangzhi_2', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe5\x85\xbb\xe6\xae\x96\xe7\xae\x80\xe4\xbb\x8b2')),
                ('url_shengtaiyangzhi_2', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe5\x85\xbb\xe6\xae\x96\xe7\xae\x80\xe4\xbb\x8b2\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_shengtaiyangzhi_3', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe5\x85\xbb\xe6\xae\x96\xe5\x9b\xbe\xe7\x89\x873')),
                ('data_shengtaiyangzhi_3', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe5\x85\xbb\xe6\xae\x96\xe7\xae\x80\xe4\xbb\x8b3')),
                ('url_shengtaiyangzhi_3', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe5\x85\xbb\xe6\xae\x96\xe7\xae\x80\xe4\xbb\x8b3\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_shengtaiyangzhi_4', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe5\x85\xbb\xe6\xae\x96\xe5\x9b\xbe\xe7\x89\x874')),
                ('data_shengtaiyangzhi_4', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe5\x85\xbb\xe6\xae\x96\xe7\xae\x80\xe4\xbb\x8b4')),
                ('url_shengtaiyangzhi_4', models.CharField(max_length=1000, verbose_name=b'\xe7\x94\x9f\xe6\x80\x81\xe5\x85\xbb\xe6\xae\x96\xe7\xae\x80\xe4\xbb\x8b4\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_kuangchanziyuan_1', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe7\x9f\xbf\xe4\xba\xa7\xe8\xb5\x84\xe6\xba\x90\xe5\x9b\xbe\xe7\x89\x871')),
                ('data_kuangchanziyuan_1', models.CharField(max_length=1000, verbose_name=b'\xe7\x9f\xbf\xe4\xba\xa7\xe8\xb5\x84\xe6\xba\x90\xe7\xae\x80\xe4\xbb\x8b1')),
                ('url_kuangchanziyuan_1', models.CharField(max_length=1000, verbose_name=b'\xe7\x9f\xbf\xe4\xba\xa7\xe8\xb5\x84\xe6\xba\x90\xe7\xae\x80\xe4\xbb\x8b1\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_kuangchanziyuan_2', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe7\x9f\xbf\xe4\xba\xa7\xe8\xb5\x84\xe6\xba\x90\xe5\x9b\xbe\xe7\x89\x872')),
                ('data_kuangchanziyuan_2', models.CharField(max_length=1000, verbose_name=b'\xe7\x9f\xbf\xe4\xba\xa7\xe8\xb5\x84\xe6\xba\x90\xe7\xae\x80\xe4\xbb\x8b2')),
                ('url_kuangchanziyuan_2', models.CharField(max_length=1000, verbose_name=b'\xe7\x9f\xbf\xe4\xba\xa7\xe8\xb5\x84\xe6\xba\x90\xe7\xae\x80\xe4\xbb\x8b2\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_kuangchanziyuan_3', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe7\x9f\xbf\xe4\xba\xa7\xe8\xb5\x84\xe6\xba\x90\xe5\x9b\xbe\xe7\x89\x873')),
                ('data_kuangchanziyuan_3', models.CharField(max_length=1000, verbose_name=b'\xe7\x9f\xbf\xe4\xba\xa7\xe8\xb5\x84\xe6\xba\x90\xe7\xae\x80\xe4\xbb\x8b3')),
                ('url_kuangchanziyuan_3', models.CharField(max_length=1000, verbose_name=b'\xe7\x9f\xbf\xe4\xba\xa7\xe8\xb5\x84\xe6\xba\x90\xe7\xae\x80\xe4\xbb\x8b3\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image_kuangchanziyuan_4', models.ImageField(upload_to=b'media/%Y/%m/%d', null=True, verbose_name=b'\xe7\x9f\xbf\xe4\xba\xa7\xe8\xb5\x84\xe6\xba\x90\xe5\x9b\xbe\xe7\x89\x874')),
                ('data_kuangchanziyuan_4', models.CharField(max_length=1000, verbose_name=b'\xe7\x9f\xbf\xe4\xba\xa7\xe8\xb5\x84\xe6\xba\x90\xe7\xae\x80\xe4\xbb\x8b4')),
                ('url_kuangchanziyuan_4', models.CharField(max_length=1000, verbose_name=b'\xe7\x9f\xbf\xe4\xba\xa7\xe8\xb5\x84\xe6\xba\x90\xe7\xae\x80\xe4\xbb\x8b4\xe9\x93\xbe\xe6\x8e\xa5')),
            ],
            options={
                'verbose_name': '\u9996\u9875\u8bbe\u7f6e',
                'verbose_name_plural': '\u9996\u9875\u8bbe\u7f6e',
            },
        ),
        migrations.DeleteModel(
            name='Allcolumns',
        ),
        migrations.DeleteModel(
            name='Homeads',
        ),
        migrations.DeleteModel(
            name='Infodetail',
        ),
        migrations.DeleteModel(
            name='Maincolumns',
        ),
    ]
