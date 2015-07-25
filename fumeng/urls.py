# coding:utf-8
from django.conf.urls import patterns, url

from . import views

from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'weixin2py.views.home', name='home'),
    # url(r'^weixin2py/', include('weixin2py.foo.urls')),
    url(r'^$', views.home),
    url(r'^about/$', views.about,name='fumeng-about'),
    url(r'^about/overview/$', views.about_overview,name='about_overview'),
    url(r'^about/strategy/$', views.about_strategy,name='about_strategy'),
    url(r'^about/advantage/$', views.about_advantage,name='about_advantage'),
    url(r'^about/progress/$', views.about_progress,name='about_progress'),
    url(r'^news/list/$', views.news_list),
    url(r'^news/list/(?P<title>\w+)/$', views.get_news_detail),
    url(r'^news/dynamic/$', views.news_dynamic,name='news_dynamic'),
    url(r'^news/map/$', views.news_map,name='news_map'),
    url(r'^news/attention/$', views.news_attention,name='news_attention'),
    url(r'^business/$', views.business,name='fumeng-business'),
    url(r'^culture/$', views.culture,name='fumeng-culture'),
    url(r'^mission/$', views.mission,name='fumeng-mission'),
    url(r'^hr/$', views.hr,name='fumeng-hr'),
    url(r'^contact/$', views.contact,name='fumeng-contact'),
) 

