# coding:utf-8
from django.db import models

class FumengBusiness(models.Model):
    shengtaizhongzhi = models.TextField(max_length = 10000,
            verbose_name = u"福梦概述")
    shengtaiyangzhi = models.TextField(max_length = 10000,
            verbose_name = u"福梦战略")
    kuangchanziyuan = models.TextField(max_length = 10000,
            verbose_name = u"核心优势")

    class Meta:
        verbose_name = u'福梦业务'
        verbose_name_plural = u'福梦业务'

