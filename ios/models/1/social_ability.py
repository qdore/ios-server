# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField

class SocialAbility(models.Model):
    gongyilinian = models.TextField(max_length = 10000,verbose_name = u"公益理念<html>")
    cishanjuanzhu = models.TextField(max_length = 10000,verbose_name = u"慈善捐助<html>")
    shehuizanyu = models.TextField(max_length = 10000,verbose_name = u"社会赞赏<html>")

    class Meta:
        verbose_name = u'社会责任'
        verbose_name_plural = u'社会责任'
