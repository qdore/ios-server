# coding:utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Context
from fumeng.models.home_page import HomePage
from fumeng.models.news import News

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
	
def about(request):
    job_list = {}
    context = RequestContext(request, {
    'job_list':job_list,              
    })  
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/fumeng-about.html',context)
def about_overview(request):
    job_list = {}
    context = RequestContext(request, {
    'job_list':job_list,              
    })  
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/about_overview.html',context)
def about_strategy(request):
    job_list = {}
    context = RequestContext(request, {
    'job_list':job_list,              
    })  
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/about_strategy.html',context)
def about_advantage(request):
    job_list = {}
    context = RequestContext(request, {
    'job_list':job_list,              
    })  
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/about_advantage.html',context)
def about_progress(request):
    job_list = {}
    context = RequestContext(request, {
    'job_list':job_list,              
    })  
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/about_progress.html',context)

	
def news(request):
    job_list = {}
    context = RequestContext(request, {
    'job_list':job_list,              
    })  
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/fumeng-news-detail.html',context)

def news_list(request):
    news_list = News.objects.all()
    print news_list
    if len(news_list) == 0:
        raise Exception(u"新闻还没有配置呢！")
    context = RequestContext(request, {
        'news':news_list,
    })
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/fumeng-news-list.html',context)
	
def news_dynamic(request):
    job_list = {}
    context = RequestContext(request, {
    'job_list':job_list,              
    })  
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/news_dynamic.html',context)
	
def news_map(request):
    job_list = {}
    context = RequestContext(request, {
    'job_list':job_list,              
    })  
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/news_map.html',context)
	
def news_attention(request):
    job_list = {}
    context = RequestContext(request, {
    'job_list':job_list,              
    })  
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/news_attention.html',context)
	

def business(request):
    job_list = {}
    context = RequestContext(request, {
    'job_list':job_list,              
    })  
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/fumeng-business.html',context)

def culture(request):
    job_list = {}
    context = RequestContext(request, {
    'job_list':job_list,              
    })  
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/fumeng-culture.html',context)
	
def mission(request):
    job_list = {}
    context = RequestContext(request, {
    'job_list':job_list,              
    })  
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/fumeng-mission.html',context)
	
def hr(request):
    job_list = {}
    context = RequestContext(request, {
    'job_list':job_list,              
    })  
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/fumeng-hr.html',context)
	
def contact(request):
    job_list = {}
    context = RequestContext(request, {
    'job_list':job_list,              
    })  
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/fumeng-contact.html',context)
