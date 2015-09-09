# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
import string, random

# 聊天管理
class Chat(models.Model):
    sender = models.CharField(verbose_name = u"发送者手机号",
            max_length = 11)
    reciver = models.CharField(verbose_name = u"接受者手机号",
            max_length = 11)
    content = models.CharField(verbose_name = u"聊天内容",
            max_length = 1000)
    readed = models.BooleanField(verbose_name = u"已读",
            default = False)

    class Meta:
        verbose_name = u'聊天内容管理'
        verbose_name_plural = u'聊天内容管理'
