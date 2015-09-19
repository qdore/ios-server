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
    title = models.CharField(verbose_name = u"公司/活动名称",
            max_length = 50)
    user_time = models.CharField(verbose_name = u"使用时间",
            max_length = 50)
    city = models.CharField(verbose_name = u"城市",
            max_length = 50)
    authorizer = models.CharField(verbose_name = u"批准人",
            max_length = 50)
    position = models.CharField(verbose_name = u"工作单位",
            max_length = 50)
    reason = models.CharField(verbose_name = u"申请理由",
            max_length = 500)
    details = models.CharField(verbose_name = u"设备及人员明细",
            max_length = 500)
    opinion = models.CharField(verbose_name = u"领导人意见",
            max_length = 500)
    memo = models.CharField(verbose_name = u"备注",
            max_length = 500)
    sponsor_name = models.CharField(verbose_name = u"申请人姓名",
            max_length = 20)
    studio = models.CharField(verbose_name = u"演播室",
            max_length = 20)
    job_number = models.CharField(verbose_name = u"部门/工号",
            max_length = 20)
    sponsor_tel = models.CharField(verbose_name = u"发起者手机",
            max_length = 11)
    status = models.CharField(verbose_name = u"工作状态",
            choices = JOB_STATUS,
            max_length = 30)
    time = models.DateField(verbose_name = u"申请日期")
    pic = models.ImageField(verbose_name = u"工作图片")
    appliers = models.CharField(verbose_name = u"申请者", max_length = 500)
    approve_applier = models.CharField(verbose_name = u"确认工作者(管理员请填入手机号)",
            max_length = 11)

    class Meta:
        verbose_name = u'工作管理'
        verbose_name_plural = u'工作管理'
