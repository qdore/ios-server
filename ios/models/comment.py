# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
import string, random

# 评论动态
class Comment(models.Model):
    status_id = models.IntegerField(verbose_name = u"状态ID")
    comment_id = models.IntegerField(verbose_name = u"评论ID")
    commenter = models.CharField(verbose_name = u"评论人手机号",
            max_length = 11)
    comment_by = models.CharField(verbose_name = u"被评论人手机号",
            max_length = 11)
    comment_content = models.CharField(verbose_name = u"评论内容",
            max_length = 1000)


    class Meta:
        verbose_name = u'评论管理'
        verbose_name_plural = u'评论管理'
