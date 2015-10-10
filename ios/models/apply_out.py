# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
import string, random
import time

# 外出申请 
class ApplyOut(models.Model):
    tel = models.CharField(verbose_name = u"手机号",
            max_length = 11)
    start_time = models.CharField(verbose_name = u"开始时间",
            max_length = 30)
    out_time = models.CharField(verbose_name = u"外出时间",
            max_length = 30)
    end_time = models.CharField(verbose_name = u"结束时间",
            max_length = 30)
    reason = models.CharField(verbose_name = u"外出原因",
            max_length = 500)

    class Meta:
        verbose_name = u'外出申请管理'
        verbose_name_plural = u'外出申请管理'
