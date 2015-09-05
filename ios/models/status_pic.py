# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
import string, random

# 动态中的图片
class StatusPics(models.Model):
    status_id = models.IntegerField(verbose_name = u"状态ID")
    pic = models.ImageField(verbose_name = u"图片")

    class Meta:
        verbose_name = u'图片管理'
        verbose_name_plural = u'图片管理'
