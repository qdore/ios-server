# coding:utf-8
from django.db import models

class AboutFumeng(models.Model):
    fumenggaishu = models.TextField(verbose_name = u"福梦概述<html>",
            max_length = 10000)
    fumengzhanlve = models.TextField(verbose_name = u"福梦战略<html>",
            max_length = 10000)
    hexinyoushi = models.TextField(verbose_name = u"核心优势<html>",
            max_length = 10000)
    fazhanlicheng = models.TextField(verbose_name = u"发展历程<html>",
            max_length = 10000)

    class Meta:
        verbose_name = u'关于福梦'
        verbose_name_plural = u'关于福梦'

