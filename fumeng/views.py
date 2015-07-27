# coding:utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Context
from fumeng.models.home_page import HomePage
from fumeng.models.news import News
from fumeng.models.about_fumeng import AboutFumeng
from fumeng.models.fumeng_business import FumengBusiness
from fumeng.models.company_culture import CompanyCulture
from fumeng.models.human_resources import HumanResource
from fumeng.models.social_ability import SocialAbility
from fumeng.models.contact_us import ContactUs
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    home_list = HomePage.objects.all()
    if len(home_list) == 0:
        raise Exception(u"首页还没有配置呢！")
    for key in home_list:
        context = RequestContext(request, {
            'home':key,
        })
    return render(request, 'fumeng/fumeng-index.html',context)

def get_news_detail(request,title):
    new = News.objects.get(title=title)
    context = RequestContext(request, {
        'new':new,              
    })  
    return render(request, 'fumeng/fumeng-news-detail.html',context)

def news_list(request, new_type):
    news_list = News.objects.filter(news_type = new_type)
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    p = Paginator(news_list, 5) 
    try:
        page = p.page(page)
    except:
        page = None
    context = RequestContext(request, {
        'news': page,
        new_type: 'her',
    })
    return render(request, 'fumeng/fumeng-news-list.html',context)

def fumeng_business_list(request, new_type):
    news_list = FumengBusiness.objects.filter(news_type = new_type)
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    p = Paginator(news_list, 12) 
    try:
        page = p.page(page)
    except:
        page = None
    context = RequestContext(request, {
        'news': page,
        new_type: 'her',
    })
    return render(request, 'fumeng/fumeng-bus-list.html',context)

def get_business_detail(request,title):
    new = FumengBusiness.objects.get(title=title)
    context = RequestContext(request, {
        'new':new,              
    })  
    return render(request, 'fumeng/fumeng-bus-detail.html',context)

def about(request, about_type):
    about_list = AboutFumeng.objects.all()
    if len(about_list) == 0:
        raise Exception(u"关于页面还没有配置呢！")
    about_fumeng = None
    for about in about_list:
        about_fumeng = about
    about_fumeng_map = {
        'fumenggaishu': about_fumeng.fumenggaishu,
        'fumengzhanlve': about_fumeng.fumengzhanlve,
        'hexinyoushi': about_fumeng.hexinyoushi,
        'fazhanlicheng': about_fumeng.fazhanlicheng,
    }
    context = RequestContext(request, {
        'about':about_fumeng_map[about_type],
        about_type: 'her',
    })  
    return render(request, 'fumeng/fumeng-about.html',context)

def fumeng_business(request, about_type):
    about_list = FumengBusiness.objects.all()
    if len(about_list) == 0:
        raise Exception(u"页面还没有配置呢！")
    about_fumeng = None
    for about in about_list:
        about_fumeng = about
    about_fumeng_map = {
        'shengtaizhongzhi': about_fumeng.shengtaizhongzhi,
        'shengtaiyangzhi': about_fumeng.shengtaiyangzhi,
        'kuangchanziyuan': about_fumeng.kuangchanziyuan,
    }
    context = RequestContext(request, {
        'about':about_fumeng_map[about_type],
        about_type: 'her',
    }) 
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/fumeng-bus.html',context)

def fumeng_culture(request, about_type):
    about_list = CompanyCulture.objects.all()
    if len(about_list) == 0:
        raise Exception(u"页面还没有配置呢！")
    about_fumeng = None
    for about in about_list:
        about_fumeng = about
    about_fumeng_map = {
        'guanlizhidao': about_fumeng.guanlizhidao,
        'qiyezongzhi': about_fumeng.qiyezongzhi,
        'qiyejinshen': about_fumeng.qiyejinshen,
        'qiyezuoyong': about_fumeng.qiyezuoyong,
    }
    context = RequestContext(request, {
        'about':about_fumeng_map[about_type],
        about_type: 'her',
    }) 
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/fumeng-culture.html',context)

def fumeng_ability(request, about_type):
    about_list = SocialAbility.objects.all()
    if len(about_list) == 0:
        raise Exception(u"页面还没有配置呢！")
    about_fumeng = None
    for about in about_list:
        about_fumeng = about
    about_fumeng_map = {
        'gongyilinian': about_fumeng.gongyilinian,
        'cishanjuanzhu': about_fumeng.cishanjuanzhu,
        'shehuizanyu': about_fumeng.shehuizanyu,
    }
    context = RequestContext(request, {
        'about':about_fumeng_map[about_type],
        about_type: 'her',
    }) 
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/fumeng-ability.html',context)

def fumeng_resource(request, about_type):
    about_list = HumanResource.objects.all()
    if len(about_list) == 0:
        raise Exception(u"页面还没有配置呢！")
    about_fumeng = None
    for about in about_list:
        about_fumeng = about
    about_fumeng_map = {
        'renlilinian': about_fumeng.renlilinian,
        'shehuizhaopin': about_fumeng.shehuizhaopin,
        'xiaoyuanzhaopin': about_fumeng.xiaoyuanzhaopin,
    }
    context = RequestContext(request, {
        'about':about_fumeng_map[about_type],
        about_type: 'her',
    }) 
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/fumeng-resource.html',context)

def fumeng_contact(request, about_type):
    about_list = ContactUs.objects.all()
    if len(about_list) == 0:
        raise Exception(u"页面还没有配置呢！")
    about_fumeng = None
    for about in about_list:
        about_fumeng = about
    about_fumeng_map = {
        'fumengzongbu': about_fumeng.fumengzongbu,
        'xiashugongsi': about_fumeng.xiashugongsi,
    }
    context = RequestContext(request, {
        'about':about_fumeng_map[about_type],
        about_type: 'her',
    }) 
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/fumeng-contact.html',context)

