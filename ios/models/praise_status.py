# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
import string, random

# 动态
class PraiseStatus(models.Model):
    status_openid = models.CharField(verbose_name = u"Token",
            default = ''.join(random.sample(string.letters, 50)),
            unique = True,
            max_length = 50)
    tel = models.CharField(verbose_name = u"点赞人手机号",
            max_length = 11)

    class Meta:
        verbose_name = u'状态管理'
        verbose_name_plural = u'状态管理'
