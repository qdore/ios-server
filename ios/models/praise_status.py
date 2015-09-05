# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
import string, random

# 动态
class PraiseStatus(models.Model):
    status_id = models.IntegerField(verbose_name = u"状态ID")
    tel = models.CharField(verbose_name = u"点赞人手机号",
            max_length = 11)

    class Meta:
        verbose_name = u'点赞管理'
        verbose_name_plural = u'点赞管理'
