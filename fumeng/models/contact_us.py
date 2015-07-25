# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField

class ContactUs(models.Model):
    fumengzongbu = RichTextField(verbose_name = u"福梦总部")
    xiashugongsi = RichTextField(verbose_name = u"下属公司")

    class Meta:
        verbose_name = u'联系我们'
        verbose_name_plural = u'联系我们'
