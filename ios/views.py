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
            break
    else:
        raise Exception('username or password error !')

def regist(global_params):
    Users.objects.create(
            tel = global_params["tel"],
            password = global_params["pwd"],
            user_id = global_params["user_id"]
            )
    login(global_params)
    ret_json["is_success"] = True

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
