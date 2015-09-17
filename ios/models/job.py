# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
import string, random

JOB_STATUS = (
        ('0', '招聘中'),
        ('1', '已分配'),
        ('2', '已完成'),
        )
# 工作
class Job(models.Model):
    title = models.CharField(verbose_name = u"工作标题",
            max_length = 50)
    job = models.CharField(verbose_name = u"工作岗位",
            max_length = 50)
    position = models.CharField(verbose_name = u"工作地址",
            max_length = 50)
    content = models.CharField(verbose_name = u"工作内容",
            max_length = 500)
    sponsor_name = models.CharField(verbose_name = u"发起者",
            max_length = 20)
    sponsor_tel = models.CharField(verbose_name = u"发起者手机",
            max_length = 11)
    status = models.CharField(verbose_name = u"工作状态",
            choices = JOB_STATUS,
            max_length = 30)
    start_time = models.DateField(verbose_name = u"开始时间")
    end_time = models.DateField(verbose_name = u"结束时间")
    pic = models.ImageField(verbose_name = u"工作图片")
    appliers = models.CharField(verbose_name = u"申请者", max_length = 500)
    approve_applier = models.CharField(verbose_name = u"确认工作者(管理员请填入手机号)", max_length = 11)

    class Meta:
        verbose_name = u'工作管理'
        verbose_name_plural = u'工作管理'
