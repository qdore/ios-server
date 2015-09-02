# coding:utf-8
from django.db import models

class UploadImage(models.Model):
    image = models.ImageField(verbose_name="上传图片",
            upload_to="media/%Y/%m/%d",
            null=True)
    class Meta:
        verbose_name = u'图片上传'
        verbose_name_plural = u'图片上传'

