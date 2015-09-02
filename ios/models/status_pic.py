# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
import string, random

# 动态中的图片
class PraiseStatus(models.Model):
    status_openid = models.CharField(verbose_name = u"Token",
            default = ''.join(random.sample(string.letters, 50)),
            unique = True,
            max_length = 50)
    pic = models.ImageField(verbose_name = u"图片")

    class Meta:
        verbose_name = u'图片管理'
        verbose_name_plural = u'图片管理'
