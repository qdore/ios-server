# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField

BUS_TYPES = (
    ('shengtaizhongzhi', '生态种植'),
    ('shengtaiyangzhi', '生态养殖'),
    ('kuangchanziyuan', '矿产资源'),
)

class FumengBusiness(models.Model):
    image = models.ImageField(verbose_name="预览图",
            upload_to="media/%Y/%m/%d",
            null=True)
    title = models.CharField(verbose_name = u"福梦业务标题",
            default = "",
            max_length = 500)
    news_type = models.CharField(verbose_name = u"福梦业务类型",
            choices = BUS_TYPES,
            default = "生态种植",
            max_length = 100)
    content = RichTextField(verbose_name = u"内容", default = "")

    class Meta:
        verbose_name = u'福梦业务'
        verbose_name_plural = u'福梦业务'
