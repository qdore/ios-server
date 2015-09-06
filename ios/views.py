# coding:utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Context
from ios.models.user import Users
from ios.models.status import Status
from ios.models.status_pic import StatusPics
from ios.models.praise_status import PraiseStatus
from django.core.files.base import ContentFile
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
ret_json = {}

def getStatus(status_id, request):
    status =  Status.objects.filter(
                id = status_id
            )
    if not status:
        raise Exception('status not found!')
    for statu in status:
        ret_val = {
            'status_id': statu.id,
            'brief': statu.brief,
        };
        pics = StatusPics.objects.filter(
                status_id = statu.id
                )
        ret_val['pictures'] = []
        for pic in pics:
            ret_val['pictures'].append(
                request.get_host() + '/media/' + str(pic.pic)
                    )
        praises = PraiseStatus.objects.filter(
                status_id = statu.id
                )
        ret_val['praisers'] = []
        for praise in praises:
            ret_val['praisers'].append(praise.tel)
        return ret_val

def getUser(global_params):
    user = Users.objects.filter(
            token = global_params["token"],
            )
    if user:
        for use in user:
            return use
    else:
        raise Exception('token not found!')

# 点赞
def praiseStatus(global_params, request):
    user = getUser(global_params)
    status = Status.objects.filter(
            id = global_params["status_id"]
            )
    if status:
        for statu in status:
            if (PraiseStatus.objects.filter(
                status_id = global_params["status_id"],
                tel = user.tel
            )):
                raise Exception('重复点赞!')
            PraiseStatus.objects.create(
                status_id = global_params["status_id"],
                tel = user.tel
                )
        ret_json["is_success"] = True
    else:
        raise Exception('status not found!')


# 获取我的状态
def getMyStatus(global_params, request):
    user = getUser(global_params)
    status = Status.objects.filter(
            tel = user.tel
            )
    ret_json['value']['status'] = []
    for statu in status:
        ret_json['value']['status'].append(getStatus(statu.id, request))
    ret_json["is_success"] = True

# 发表状态
def publishStatus(global_params, request):
    user = getUser(global_params)
    status = Status.objects.create(
            tel = user.tel,
            brief = global_params["brief"]
            )
    i = 0
    while i >= 0:
        pic = StatusPics.objects.create(
                status_id = status.id
                );
        try:
            file_content = ContentFile(global_params['pic' + str(i)].read()) 
            pic.pic.save(global_params['pic' + str(i)].name, file_content)
            i = i + 1
        except:
            pic.delete()
            break
    ret_json["is_success"] = True

# 注册及登录
def login(global_params, request):
    user = getUser(global_params)
    ret_json["is_success"] = True
    ret_json["value"]["token"] = user.token
    ret_json["value"]["user_type"] = user.user_type

def regist(global_params, request):
    Users.objects.create(
            tel = global_params["tel"],
            password = global_params["pwd"],
            user_type = global_params["user_type"],
            user_id = global_params["user_id"]
            )
    login(global_params)
    ret_json["is_success"] = True

def changePassword(global_params, request):
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

def updateUserInfor(global_params, request):
    user = getUser(global_params)
    user.name = global_params["name"]
    user.gender = global_params["gender"]
    user.brief = global_params["brief"]
    user.save()
    ret_json["is_success"] = True
        
def getUserInforByToken(global_params, request):
    user = getUser(global_params)
    ret_json["value"]["name"] = user.name
    ret_json["value"]["gender"] = user.gender
    ret_json["value"]["brief"] = user.brief
    ret_json["is_success"] = True

def getUserInforByTel(global_params, request):
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
        global_params.update(request.FILES)
        exec(global_params["method"].strip() + "(global_params, request)");
        return HttpResponse(json.dumps(ret_json, ensure_ascii = False),
                content_type="application/json")
    except Exception, e:
        ret_json["is_success"] = False
        ret_json["value"]["error"] = str(e)
        print e
        return HttpResponse(json.dumps(ret_json, ensure_ascii = False),
                content_type="application/json")
