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
    url(r'^about/(?P<about_type>\w+)/$', views.about,name='fumeng-about'),

    url(r'^news/(?P<new_type>\w+)/$', views.news_list),
    url(r'^news/list/(?P<title>\w+)/$', views.get_news_detail),

    url(r'^business/(?P<about_type>\w+)/$', views.fumeng_business),

    url(r'^culture/(?P<about_type>\w+)/$', views.fumeng_culture),
    
    url(r'^ability/(?P<about_type>\w+)/$', views.fumeng_ability),

    url(r'^resource/(?P<about_type>\w+)/$', views.fumeng_resource),

    url(r'^contact/(?P<about_type>\w+)/$', views.fumeng_contact),
) 

