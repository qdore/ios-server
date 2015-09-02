# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
import string, random

# 动态
class Status(models.Model):
    openid = models.CharField(verbose_name = u"Token",
            default = ''.join(random.sample(string.letters, 50)),
            unique = True,
            max_length = 50)
    tel = models.CharField(verbose_name = u"手机号",
            max_length = 11)
    brief =  models.CharField(verbose_name = u"简介",
            max_length = 500)

    class Meta:
        verbose_name = u'用户管理'
        verbose_name_plural = u'用户管理'
