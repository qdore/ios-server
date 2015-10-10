# coding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
import string, random
import time

USER_TYPES = (
    ('0', '摄影师'),
    ('1', '制片人'),
)

GENDER_TYPES = (
    ('0', '男'),
    ('1', '女'),
)

VERIFY_TYPES = (
    ('0', '未提交审核'),
    ('1', '已提交审核'),
    ('2', '审核通过'),
    ('3', '审核不通过'),
)
# 新闻
class Users(models.Model):
    tel = models.CharField(verbose_name = u"手机号",
            unique = True,
            max_length = 11)
    password = models.CharField(verbose_name = u"密码",
            max_length = 20)
    user_id = models.CharField(verbose_name = u"身份证号",
            default = u"admin",
            unique = True,
            max_length = 18)
    work_id = models.CharField(verbose_name = u"工号",
            default = u"admin",
            unique = True,
            max_length = 20)
    head_photo = models.ImageField(verbose_name = u"头像")
    user_type = models.CharField(verbose_name = u"用户角色",
            choices = USER_TYPES,
            max_length = 20)
    name = models.CharField(verbose_name = u"用户名",
            max_length = 20)
    gender = models.CharField(verbose_name = u"性别",
            choices = GENDER_TYPES,
            max_length = 20)
    brief =  models.CharField(verbose_name = u"简介",
            max_length = 500)
    token = models.CharField(verbose_name = u"Token",
            default = str(time.time()).replace('.', '') + \
            ''.join(random.sample(string.letters, 38)),
            unique = True,
            max_length = 50)
    true_name = models.CharField(verbose_name = u"真实姓名",
            max_length = 20)
    identity = models.CharField(verbose_name = u"身份证号",
            max_length = 18)
    identity_photo = models.ImageField(verbose_name = u"身份证照片")
    work_photo = models.ImageField(verbose_name = u"工作证照片")
    is_verified = models.CharField(verbose_name = u"审核状态",
            choices = VERIFY_TYPES,
            default = '0',
            max_length = 1)

    class Meta:
        verbose_name = u'用户管理'
        verbose_name_plural = u'用户管理'

