# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField

class AboutFumeng(models.Model):
    fumenggaishu = RichTextField(verbose_name = u"福梦概述")
    fumengzhanlve = RichTextField(verbose_name = u"福梦战略")
    hexinyoushi = RichTextField(verbose_name = u"核心优势")
    fazhanlicheng = RichTextField(verbose_name = u"发展历程")

    class Meta:
        verbose_name = u'关于福梦'
        verbose_name_plural = u'关于福梦'

