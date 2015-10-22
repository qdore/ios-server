# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
import string, random
import datetime
import time
import user

# 外出申请 
class ApplyOut(models.Model):
    tel = models.CharField(verbose_name = u"手机号",
            max_length = 11)
    start_time = models.CharField(verbose_name = u"开始时间",
            max_length = 30)
    out_time = models.CharField(verbose_name = u"外出时间",
            max_length = 30)
    end_time = models.CharField(verbose_name = u"结束时间",
            max_length = 30)
    reason = models.CharField(verbose_name = u"外出原因",
            max_length = 500)
    def out_time2(self):
        start_time = datetime.datetime.strptime(self.start_time, "%Y-%m-%d %H:%M:%S")
        end_time = datetime.datetime.strptime(self.end_time, "%Y-%m-%d %H:%M:%S") 
        time = end_time - start_time
        return str(time)
    out_time2.short_description = u"外出时间"

    def true_name(self):
        use = user.Users.objects.filter(tel = self.tel)
        for us in use:
            return us.true_name
    true_name.short_description = u"姓名"
    def user_name(self):
        use = user.Users.objects.filter(tel = self.tel)
        for us in use:
            return us.name
    user_name.short_description = u"用户名"

    class Meta:
        verbose_name = u'外出申请管理'
        verbose_name_plural = u'外出申请管理'
