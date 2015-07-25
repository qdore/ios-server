# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField

class CompanyCulture(models.Model):
    guanlizhidao = RichTextField(verbose_name = u"管理之道")
    qiyezongzhi = RichTextField(verbose_name = u"企业宗旨")
    qiyejinshen = RichTextField(verbose_name = u"企业精神")
    qiyezuoyong = RichTextField(verbose_name = u" 企业作用")

    class Meta:
        verbose_name = u'企业文化'
        verbose_name_plural = u'企业文化'

