# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField

NEWS_TYPES = (
    ('fumengxinwen', '福梦新闻'),
    ('diqudongtai', '地区动态'),
    ('meitiguanzhu', '媒体关注'),
)

# 新闻
class News(models.Model):
    title = models.CharField(verbose_name = u"新闻标题",
            unique = True,
            max_length = 500)
    news_type = models.CharField(verbose_name = u"新闻类型",
            choices = NEWS_TYPES,
            max_length = 100)
    add_time = models.DateTimeField(verbose_name = u"添加日期",
            auto_now_add = True)
    add_by = models.CharField(verbose_name = u"本文来自",
            default = u"admin",
            max_length = 100)
    content = RichTextField(verbose_name = u"新闻内容")

    class Meta:
        verbose_name = u'新闻编辑'
        verbose_name_plural = u'新闻编辑'

