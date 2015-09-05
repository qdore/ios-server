# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
import string, random

# 动态
class Status(models.Model):
    tel = models.CharField(verbose_name = u"手机号",
            max_length = 11)
    brief =  models.CharField(verbose_name = u"简介",
            max_length = 500)
    class Meta:
        verbose_name = u'状态管理'
        verbose_name_plural = u'状态管理'
