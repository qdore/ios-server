# coding:utf-8
from django.db import models

class FumengBusiness(models.Model):
    shengtaizhongzhi = models.TextField(max_length = 10000,
            verbose_name = u"生态种植<html>")
    shengtaiyangzhi = models.TextField(max_length = 10000,
            verbose_name = u"生态养殖<html>")
    kuangchanziyuan = models.TextField(max_length = 10000,
            verbose_name = u"矿产资源<html>")

    class Meta:
        verbose_name = u'福梦业务'
        verbose_name_plural = u'福梦业务'

