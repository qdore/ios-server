# coding:utf-8
from django.db import models

class HumanResource(models.Model):
    renlilinian = models.TextField(max_length = 10000,
            verbose_name = u"人力理念<html>")
    shehuizhaopin = models.TextField(max_length = 10000,
            verbose_name = u"社会招聘<html>")
    xiaoyuanzhaopin = models.TextField(max_length = 10000,
            verbose_name = u"校园招聘<html>")

    class Meta:
        verbose_name = u'人力资源'
        verbose_name_plural = u'人力资源'
