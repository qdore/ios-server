# coding:utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Context
from ios.models.user import Users
import json

ret_json = {}

# Create your views here.
def login(global_params):
    user = Users.objects.filter(
            tel = global_params["tel"],
            password = global_params["pwd"])
    if user:
        ret_json["is_success"] = True
        for use in user:
            ret_json["value"]["token"] = use.token
            ret_json["value"]["user_type"] = use.user_type
            break
    else:
        raise Exception('username or password error !')

def regist(global_params):
    Users.objects.create(
            tel = global_params["tel"],
            password = global_params["pwd"],
            user_type = global_params["user_type"],
            user_id = global_params["user_id"]
            )
    login(global_params)
    ret_json["is_success"] = True

def changePassword(global_params):
    user = Users.objects.filter(
            token = global_params["token"],
            password = global_params["pwd"]
            )
    if user:
        for use in user:
            use.password = global_params["new_pwd"]
            use.save()
            ret_json["is_success"] = True
    else:
        raise Exception('username or password error!')

def updateUserInfor(global_params):
    user = Users.objects.filter(
            token = global_params["token"]
            )
    if user:
        for use in user:
            use.name = global_params["name"]
            use.gender = global_params["gender"]
            use.brief = global_params["brief"]
            use.save()
            ret_json["is_success"] = True
    else:
        raise Exception('token not found')
        
def getUserInforByToken(global_params):
    user = Users.objects.filter(
            token = global_params["token"]
            )
    if user:
        for use in user:
            ret_json["value"]["name"] = use.name
            ret_json["value"]["gender"] = use.gender
            ret_json["value"]["brief"] = use.brief
            ret_json["is_success"] = True
    else:
        raise Exception('token not found')

def getUserInforByTel(global_params):
    user = Users.objects.filter(
            tel = global_params["tel"]
            )
    if user:
        for use in user:
            ret_json["value"]["name"] = use.name
            ret_json["value"]["gender"] = use.gender
            ret_json["value"]["brief"] = use.brief
            ret_json["is_success"] = True
    else:
        raise Exception('tel not found')

def home(request):
    global ret_json
    ret_json = {
        "is_success": False,
        "value": {}
    }
    try:
        global_params = request.GET.copy()
        global_params.update(request.POST)
        exec(global_params["method"].strip() + "(global_params)");
        return HttpResponse(json.dumps(ret_json), content_type="application/json")
    except Exception, e:
        ret_json["is_success"] = False
        ret_json["value"]["error"] = str(e)
        return HttpResponse(json.dumps(ret_json), content_type="application/json")
