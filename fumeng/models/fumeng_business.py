# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField

class FumengBusiness(models.Model):
    shengtaizhongzhi = RichTextField(verbose_name = u"福梦概述")
    shengtaiyangzhi = RichTextField(verbose_name = u"福梦战略")
    kuangchanziyuan = RichTextField(verbose_name = u"核心优势")

    class Meta:
        verbose_name = u'关于福梦'
        verbose_name_plural = u'关于福梦'

