# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField

class SocialAbility(models.Model):
    gongyilinian = RichTextField(verbose_name = u"公益理念")
    cishanjuanzhu = RichTextField(verbose_name = u"慈善捐助")
    shehuizanyu = RichTextField(verbose_name = u"社会赞赏")

    class Meta:
        verbose_name = u'社会责任'
        verbose_name_plural = u'社会责任'
