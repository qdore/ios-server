from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Context
from fumeng.home_page import *


import home_page

# Create your views here.
def home(request):
    home_list = HomePage.objects.all()
    for key in home_list:
        context = RequestContext(request, {
            'home':key,
        })
    print key.image_1
    #return HttpResponse(template.render(context))
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
    return render(request, 'fumeng/fumeng-news.html',context)

def news_news(request):
    job_list = {}
    context = RequestContext(request, {
    'job_list':job_list,              
    })  
    #return HttpResponse(template.render(context))
    return render(request, 'fumeng/news_news.html',context)
	
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
