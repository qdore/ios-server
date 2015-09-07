# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
import string, random

# 关注关系
class AttentionRelation(models.Model):
    attent_tel = models.CharField(verbose_name = u"关注人手机号",
            max_length = 11)
    tel_by_attent = models.CharField(verbose_name = u"被关注人手机号",
            max_length = 11)

    class Meta:
        verbose_name = u'关注信息管理'
        verbose_name_plural = u'关注信息管理'
