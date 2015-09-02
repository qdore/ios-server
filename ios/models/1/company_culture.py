# coding:utf-8
from django.db import models

class CompanyCulture(models.Model):
    guanlizhidao = models.TextField(max_length = 10000,verbose_name = u"管理之道<html>")
    qiyezongzhi = models.TextField(max_length = 10000,verbose_name = u"企业宗旨<html>")
    qiyejinshen = models.TextField(max_length = 10000,verbose_name = u"企业精神<html>")
    qiyezuoyong = models.TextField(max_length = 10000,verbose_name = u" 企业作用<html>")

    class Meta:
        verbose_name = u'企业文化'
        verbose_name_plural = u'企业文化'

