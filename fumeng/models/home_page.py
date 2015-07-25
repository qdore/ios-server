# coding:utf-8
from django.db import models

# 首页
class HomePage(models.Model):
    image_1 = models.ImageField(verbose_name="首页海报图1",
    upload_to="media/%Y/%m/%d",
            null=True)
    url_1 = models.CharField(verbose_name="首页海报图1链接", max_length = 1000)
    image_2 = models.ImageField(verbose_name="首页海报图2",
            upload_to="media/%Y/%m/%d",
            null=True)
    url_2 = models.CharField(verbose_name="首页海报图2链接", max_length = 1000)
    image_3 = models.ImageField(verbose_name="首页海报图3",
            upload_to="media/%Y/%m/%d",
            null=True)
    url_3 = models.CharField(verbose_name="首页海报图3链接", max_length = 1000)
    image_4 = models.ImageField(verbose_name="首页海报图4",
            upload_to="media/%Y/%m/%d",
            null=True)
    url_4 = models.CharField(verbose_name="首页海报图4链接", max_length = 1000)

    #关于福梦
    image_about = models.ImageField(verbose_name="首页关于我们图片",
            upload_to="media/%Y/%m/%d",
            null=True)
    data_about = models.CharField(verbose_name="首页关于我们简介", max_length = 1000)
    url_about = models.CharField(verbose_name="首页关于我们简介链接", max_length = 1000)

    #生态种植
    image_shengtaizhongzhi_1 = models.ImageField(verbose_name="生态种植图片1",
            upload_to="media/%Y/%m/%d",
            null=True)
    data_shengtaizhongzhi_1 = models.CharField(verbose_name="生态种植简介1", max_length = 1000)
    url_shengtaizhongzhi_1 = models.CharField(verbose_name="生态种植简介1链接", max_length = 1000)

    image_shengtaizhongzhi_2 = models.ImageField(verbose_name="生态种植图片2",
            upload_to="media/%Y/%m/%d",
            null=True)
    data_shengtaizhongzhi_2 = models.CharField(verbose_name="生态种植简介2", max_length = 1000)
    url_shengtaizhongzhi_2 = models.CharField(verbose_name="生态种植简介2链接", max_length = 1000)

    image_shengtaizhongzhi_3 = models.ImageField(verbose_name="生态种植图片3",
            upload_to="media/%Y/%m/%d",
            null=True)
    data_shengtaizhongzhi_3 = models.CharField(verbose_name="生态种植简介3", max_length = 1000)
    url_shengtaizhongzhi_3 = models.CharField(verbose_name="生态种植简介3链接", max_length = 1000)
    image_shengtaizhongzhi_4 = models.ImageField(verbose_name="生态种植图片4",
            upload_to="media/%Y/%m/%d",
            null=True)
    data_shengtaizhongzhi_4 = models.CharField(verbose_name="生态种植简介4", max_length = 1000)
    url_shengtaizhongzhi_4 = models.CharField(verbose_name="生态种植简介4链接", max_length = 1000)

    #生态养殖
    image_shengtaiyangzhi_1 = models.ImageField(verbose_name="生态养殖图片1",
            upload_to="media/%Y/%m/%d",
            null=True)
    data_shengtaiyangzhi_1 = models.CharField(verbose_name="生态养殖简介1", max_length = 1000)
    url_shengtaiyangzhi_1 = models.CharField(verbose_name="生态养殖简介1链接", max_length = 1000)

    image_shengtaiyangzhi_2 = models.ImageField(verbose_name="生态养殖图片2",
            upload_to="media/%Y/%m/%d",
            null=True)
    data_shengtaiyangzhi_2 = models.CharField(verbose_name="生态养殖简介2", max_length = 1000)
    url_shengtaiyangzhi_2 = models.CharField(verbose_name="生态养殖简介2链接", max_length = 1000)

    image_shengtaiyangzhi_3 = models.ImageField(verbose_name="生态养殖图片3",
            upload_to="media/%Y/%m/%d",
            null=True)
    data_shengtaiyangzhi_3 = models.CharField(verbose_name="生态养殖简介3", max_length = 1000)
    url_shengtaiyangzhi_3 = models.CharField(verbose_name="生态养殖简介3链接", max_length = 1000)
    image_shengtaiyangzhi_4 = models.ImageField(verbose_name="生态养殖图片4",
            upload_to="media/%Y/%m/%d",
            null=True)
    data_shengtaiyangzhi_4 = models.CharField(verbose_name="生态养殖简介4", max_length = 1000)
    url_shengtaiyangzhi_4 = models.CharField(verbose_name="生态养殖简介4链接", max_length = 1000)

    #矿产资源
    image_kuangchanziyuan_1 = models.ImageField(verbose_name="矿产资源图片1",
            upload_to="media/%Y/%m/%d",
            null=True)
    data_kuangchanziyuan_1 = models.CharField(verbose_name="矿产资源简介1", max_length = 1000)
    url_kuangchanziyuan_1 = models.CharField(verbose_name="矿产资源简介1链接", max_length = 1000)

    image_kuangchanziyuan_2 = models.ImageField(verbose_name="矿产资源图片2",
            upload_to="media/%Y/%m/%d",
            null=True)
    data_kuangchanziyuan_2 = models.CharField(verbose_name="矿产资源简介2", max_length = 1000)
    url_kuangchanziyuan_2 = models.CharField(verbose_name="矿产资源简介2链接", max_length = 1000)

    image_kuangchanziyuan_3 = models.ImageField(verbose_name="矿产资源图片3",
            upload_to="media/%Y/%m/%d",
            null=True)
    data_kuangchanziyuan_3 = models.CharField(verbose_name="矿产资源简介3", max_length = 1000)
    url_kuangchanziyuan_3 = models.CharField(verbose_name="矿产资源简介3链接", max_length = 1000)
    image_kuangchanziyuan_4 = models.ImageField(verbose_name="矿产资源图片4",
            upload_to="media/%Y/%m/%d",
            null=True)
    data_kuangchanziyuan_4 = models.CharField(verbose_name="矿产资源简介4", max_length = 1000)
    url_kuangchanziyuan_4 = models.CharField(verbose_name="矿产资源简介4链接", max_length = 1000)

    class Meta:
        verbose_name = u'首页设置'
        verbose_name_plural = u'首页设置'

