# coding:utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Context
from ios.models.user import Users
from ios.models.status import Status
from ios.models.status_pic import StatusPics
from ios.models.attention_relation import AttentionRelation
from ios.models.praise_status import PraiseStatus
from ios.models.chat import Chat
from ios.models.comment import Comment
from ios.models.job import Job
from django.core.files.base import ContentFile
from django.db.models import Q
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def getUserNameByTel(user_tel):
    user = Users.objects.filter(
            tel = user_tel
            )
    if user:
        for use in user:
            return use.name
        return user_tel
    else:
        return user_tel

def getHeadPhotoByTel(user_tel, request):
    user = Users.objects.filter(
            tel = user_tel
            )
    if user:
        for use in user:
            return 'http://' + request.get_host() + '/media/' + str(use.head_photo)
        return "" 
    else:
        return ""


def getStatus(status_id, request):
    global_params = request.GET.copy()
    global_params.update(request.POST)
    me = getUser(global_params)
    status =  Status.objects.filter(
                id = status_id
            )
    if not status:
        raise Exception('status not found!')
    for statu in status:
        ret_val = {
            'status_id': statu.id,
            'brief': statu.brief,
            'name': getUserNameByTel(statu.tel),
            'head_photo': getHeadPhotoByTel(statu.tel, request),
        };
        pics = StatusPics.objects.filter(
                status_id = statu.id
                )
        ret_val['pictures'] = []
        for pic in pics:
            ret_val['pictures'].append(
                'http://' + request.get_host() + '/media/' + str(pic.pic)
                    )
        praises = PraiseStatus.objects.filter(
                status_id = statu.id
                )
        is_praise = False
        ret_val['praisers'] = []
        for user in praises:
            if (user.tel == me.tel):
                continue
            user_status = []
            status = Status.objects.filter(
                    tel = user.tel
                    )
            for statu in status:
                user_status.insert(0, getStatus(statu.id, request))
            user_status = user_status[:3]
            is_friend = False
            relation = AttentionRelation.objects.filter(
                    attent_tel = me.tel,
                    tel_by_attent = user.tel,
                    )
            if relation:
                is_friend = True
            ret_val['praisers'].append({
                "name": user.name,
                "gender": user.gender,
                "brief": user.brief,
                "type": user.user_type,
                "user_id": user.user_id,
                "head_photo": 'http://' + request.get_host() + '/media/' + str(user.head_photo),
                "tel": user.tel,
                "is_friend": is_friend,
                "status": user_status,
            })
        ret_val['is_praise'] = is_praise
        ret_val['comment'] = []
        comments = Comment.objects.filter(
                status_id = statu.id
                )
        for comment in comments:
            ret_val['comment'].append({
                'comment_id': comment.id,
                'content': comment.comment_content,
                'comment_by': getUserNameByTel(comment.comment_by),
                'comment_by_head_photo': getHeadPhotoByTel(comment.comment_by, request),
                'commenter': getUserNameByTel(comment.commenter),
                'commenter_head_photo': getHeadPhotoByTel(comment.commenter, request),
            })
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


def getJobInfo(job_id, request):
    global_params = request.GET.copy()
    global_params.update(request.POST)
    user = getUser(global_params)
    jobs = Job.objects.filter(id = job_id)
    job_info = {}
    for job in jobs:
        job_info = {
		"job_id": job.id,
                "title": job.title,
                "user_time": job.user_time,
                "city": job.city,
                "authorizer": job.authorizer,
                "position": job.position,
                "reason": job.reason,
                "details": job.details,
                "camera": job.camera,
                "broadcast_car": job.broadcast_car,
                "later_period": job.later_period,
                "opinion": job.opinion,
                "memo": job.memo,
                "sponsor_name": job.sponsor_name,
                "job_number": job.job_number,
                "sponsor_tel": job.sponsor_tel,
                "status": job.status,
                "time": str(job.time),
                "pic": 'http://' + request.get_host() + '/media/' + str(job.pic),
                "approve_applier_tel": job.approve_applier,
                "approve_applier_name": getUserNameByTel(job.approve_applier),
                "approve_applier_head_photo": getHeadPhotoByTel(job.approve_applier, request),
        } 
        job_info["appliers"] = []
        is_applyed = False
        for apply in job.appliers.split(';'):
            brackets = apply.find('(')
            if brackets < 0:
                continue
            if apply.find(user.tel) > 0:
                is_applyed = True
            print apply[1:]
            job_info["appliers"].append({
                    "name": apply[0: brackets],
                    "tel": apply[brackets + 1: -1],
                    "head_photo": getHeadPhotoByTel(apply[brackets + 1: -1], request)
                    })
        job_info["is_applyed"] = is_applyed
    return job_info

# 发起工作
def sponseJob(global_params, request, ret_json):
    user = getUser(global_params)
    if user.user_type == '0':
        raise Exception('只有制片人才能发布任务！')
    job = Job.objects.create(
        title = global_params['title'],
        user_time = global_params['user_time'],
        city = global_params['city'],
        authorizer = global_params['authorizer'],
        position = global_params['position'],
        reason = global_params['reason'],
        details = global_params['details'],
        opinion = global_params['opinion'],
        memo = global_params['memo'],
        sponsor_name = global_params['sponsor_name'],
        studio = global_params['studio'],
        job_number = global_params['job_number'],
        camera = global_params['camera'],
        broadcast_car = global_params['broadcast_car'],
        later_period = global_params['later_period'],
        sponsor_tel = user.tel,
        status = 0,
        time = global_params['time'],
        appliers = "",
        approve_applier = "",
    )
    job.save()
    file_content = ContentFile(global_params['pic'].read()) 
    job.pic.save(global_params['pic'].name, file_content)
    ret_json['is_success'] = True

# 申请工作
def applyJob(global_params, request, ret_json):
    user = getUser(global_params)
    if user.user_type == '1':
        raise Exception('只有摄影师才能申请任务！')
    jobs = Job.objects.filter(id = int(global_params["job_id"]))
    if jobs:
        for job in jobs:
            job_str = '%s(%s)' % (user.name, user.tel)
            temp = job.appliers.split(';')
            temp = list(temp)
            temp.append(job_str)
            job.appliers = ';'.join(list(set(temp)))
            job.save()
    else:
        raise Exception("找不到工作！")
            
# 我申请的/我发布的工作
def getMyJob(global_params, request, ret_json):
    user = getUser(global_params)
    jobs = Job.objects.filter(Q(appliers__icontains = user.tel) |
            Q(sponsor_tel = user.tel))
    ret_json['jobs'] = []
    if jobs:
        for job in jobs:
            ret_json['jobs'].insert(0, getJobInfo(job.id, request))

# 广场中的工作
def getSquareJob(global_params, request, ret_json):
    jobs = Job.objects.filter(status = global_params['status'])
    ret_json['jobs'] = []
    print list(jobs)
    global_params['n'] = int(global_params['n'])
    if jobs:
        jobs = jobs[max(0, len(jobs) - global_params['n'] - 42):  max(0, min(len(jobs) - global_params['n'], len(jobs)))]
        print list(jobs)
        for job in jobs:
            ret_json['jobs'].insert(0, getJobInfo(job.id, request))

# 确认工作
def confirmJob(global_params, request, ret_json):
    user = getUser(global_params)
    jobs = Job.objects.filter(id= global_params['job_id'],
            sponsor_tel = user.tel)
    if jobs:
        for job in jobs:
            job.approve_applier = global_params['tel']
            job.save()
    else:
        raise Exception("找不到满足条件的job或者你没有权限！")

# 删除工作
def delJob(global_params, request, ret_json):
    user = getUser(global_params)
    Job.objects.filter(id= global_params['job_id'],
            sponsor_tel = user.tel).delete()

# 评论动态
def commentStatus(global_params, request, ret_json):
    user = getUser(global_params)
    status = Status.objects.filter(
            id = global_params["status_id"]
            )
    if status:
        for statu in status:
            Comment.objects.create(status_id = global_params["status_id"],
                    commenter = user.tel,
                    comment_id = -1,
                    comment_by = statu.tel,
                    comment_content = global_params["content"]
                    )
        ret_json['is_success'] = True
    else:
        raise Exception('status not found!')

# 评论评论
def commentOtherComment(global_params, request, ret_json):
    user = getUser(global_params)
    comments = Comment.objects.filter(
            id = global_params["comment_id"]
            )
    if comments:
        for comment in comments:
            Comment.objects.create(
                    status_id = comment.status_id,
                    comment_id = global_params["comment_id"],
                    commenter = user.tel,
                    comment_by = comment.commenter,
                    comment_content = global_params["content"]
                    )
        ret_json['is_success'] = True
    else:
        raise Exception('comment not found!')

# 发送站内信
def sendMsg(global_params, request, ret_json):
    user = getUser(global_params)
    Chat.objects.create(
            sender = user.tel,
            reciver = global_params['receiver'],
            content = global_params['content']
            )
    ret_json['is_success'] = True
    
# 接受站内信
def getMsg(global_params, request, ret_json):
    user = getUser(global_params)
    msgs = Chat.objects.filter(reciver = user.tel)
    ret_json['value']['msgs'] = []
    for msg in msgs:
        ret_json['value']['msgs'].append({
                'sender': msg.sender,
                'sender_header_photo': getHeadPhotoByTel(msg.sender, request),
                'content': msg.content,
                })
        msg.readed = True
        msg.save()
    ret_json['is_success'] = True

# 取消赞
def undoPraise(global_params, request, ret_json):
    user = getUser(global_params)
    status = Status.objects.filter(
            id = global_params["status_id"]
            )
    if status:
        for statu in status:
            PraiseStatus.objects.filter(
                status_id = global_params["status_id"],
                tel = user.tel
                ).delete()
        ret_json["is_success"] = True
    else:
        raise Exception('status not found!')

# 点赞
def praiseStatus(global_params, request, ret_json):
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

# 获取最新的状态, 从n开始
def getNStatus(global_params, request, ret_json):
    user = getUser(global_params)
    status = Status.objects.all()
    global_params['n'] = int(global_params['n'])
    status = status[max(0, status.count() - global_params['n'] - 42):  max(0, min(status.count() - global_params['n'], status.count()))]
    ret_json['value']['status'] = []
    for statu in status:
        ret_json['value']['status'].insert(0, getStatus(statu.id, request))
    ret_json["is_success"] = True

# 获取我的朋友圈状态，从n开始 42条
def getFriendStatus(global_params, request, ret_json):
    user = getUser(global_params)
    relations = AttentionRelation.objects.filter(
            tel_by_attent = user.tel,
            )
    friends = []
    if relations:
        for relation in relations:
            friends.append(relation.attent_tel)
    status = list(Status.objects.filter(
            tel = friends
            ))
    global_params['n'] = int(global_params['n'])
    status = status[max(0, len(status) - global_params['n'] - 42):  max(0, min(len(status) - global_params['n'], len(status)))]
    ret_json['value']['status'] = []
    for statu in status:
        ret_json['value']['status'].insert(0, getStatus(statu.id, request))
    ret_json["is_success"] = True

# 获取我的状态
def getMyStatus(global_params, request, ret_json):
    user = getUser(global_params)
    status = Status.objects.filter(
            tel = user.tel
            )
    ret_json['value']['status'] = []
    for statu in status:
        ret_json['value']['status'].insert(0, getStatus(statu.id, request))
    ret_json["is_success"] = True

# 获取某人的状态
def getSomeOneStatusByTel(global_params, request, ret_json):
    status = Status.objects.filter(
            tel = global_params['tel']
            )
    ret_json['value']['status'] = []
    for statu in status:
        ret_json['value']['status'].insert(0, getStatus(statu.id, request))
    ret_json["is_success"] = True

# 找人
def findSomeOne(global_params, request, ret_json):
    me = getUser(global_params)
    if global_params['para'] == "":
        users = Users.objects.all()[:3]
    else:
        users = Users.objects.filter(Q(name__icontains = global_params['para']) |
                Q(user_id__icontains = global_params['para']) |
                Q(tel__icontains = global_params['para']))
    ret_json["value"]["person"] = []
    for user in users:
        if (user.tel == me.tel):
            continue
        user_status = []
        status = Status.objects.filter(
                tel = user.tel
                )
        for statu in status:
            user_status.insert(0, getStatus(statu.id, request))
        user_status = user_status[:3]
        is_friend = False
        relation = AttentionRelation.objects.filter(
                attent_tel = me.tel,
                tel_by_attent = user.tel,
                )
        if relation:
            is_friend = True
        ret_json["value"]["person"].append({
            "name": user.name,
            "gender": user.gender,
            "brief": user.brief,
            "type": user.user_type,
            "user_id": user.user_id,
            "head_photo": 'http://' + request.get_host() + '/media/' + str(user.head_photo),
            "tel": user.tel,
            "is_friend": is_friend,
            "status": user_status,
        })
    ret_json["is_success"] = True

# 取消关注
def cancelFriend(global_params, request, ret_json):
    user = getUser(global_params)
    AttentionRelation.objects.filter(
            attent_tel = user.tel,
            tel_by_attent = global_params['tel']
            ).delete()
    ret_json["is_success"] = True

# 加关注
def addSomeOneAsFriend(global_params, request, ret_json):
    user = getUser(global_params)
    AttentionRelation.objects.create(
            attent_tel = user.tel,
            tel_by_attent = global_params['attented_tel']
            )
    ret_json["is_success"] = True

# 获取某人的关注信息
def getAttentRelation(global_params, request, ret_json):
    attent_someone = AttentionRelation.objects.filter(
            attent_tel = global_params['tel']
            )
    attent_by_someone = AttentionRelation.objects.filter(
            tel_by_attent = global_params['tel']
            )
    ret_json['value']['attent_someone'] = []
    ret_json['value']['attent_by_someone'] = []
    for attent in attent_someone:
        ret_json['value']['attent_someone'].append(attent.tel_by_attent)
    for attent in attent_by_someone:
        ret_json['value']['attent_by_someone'].append(attent.attent_tel)
    ret_json["is_success"] = True

# 发表状态
def publishStatus(global_params, request, ret_json):
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
def login(global_params, request, ret_json):
    user = Users.objects.filter(
            tel = global_params["tel"],
            password = global_params["pwd"])
    if not user:
        raise Exception('username or password error')
    for use in user:
        ret_json["value"]["token"] = use.token
        ret_json["value"]["user_type"] = use.user_type
        ret_json["is_success"] = True

def regist(global_params, request, ret_json):
    Users.objects.create(
            tel = global_params["tel"],
            password = global_params["pwd"],
            user_type = global_params["user_type"],
            user_id = global_params["user_id"]
            )
    login(global_params, request, ret_json)
    ret_json["is_success"] = True

def changePassword(global_params, request, ret_json):
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

def updateUserInfor(global_params, reques, ret_json):
    user = getUser(global_params)
    file_content = ContentFile(global_params['head_photo'].read()) 
    user.name = global_params["name"]
    user.gender = global_params["gender"]
    user.brief = global_params["brief"]
    user.save()
    user.head_photo.save(global_params['head_photo'].name, file_content)
    ret_json["is_success"] = True
        
def getUserInforByToken(global_params, request, ret_json):
    user = getUser(global_params)
    ret_json["value"]["name"] = user.name
    ret_json["value"]["gender"] = user.gender
    ret_json["value"]["brief"] = user.brief
    ret_json["value"]["head_photo"] = 'http://' + request.get_host() + '/media/' + str(user.head_photo)
    ret_json["is_success"] = True

def getUserInforByTel(global_params, request, ret_json):
    user = Users.objects.filter(
            tel = global_params["tel"]
            )
    if user:
        for use in user:
            ret_json["value"]["name"] = use.name
            ret_json["value"]["gender"] = use.gender
            ret_json["value"]["brief"] = use.brief
            ret_json["value"]["head_photo"] = 'http://' + request.get_host() + '/media/' + str(use.head_photo)
            ret_json["is_success"] = True
    else:
        raise Exception('tel not found')

def home(request):
    ret_json = {
        "is_success": True,
        "value": {}
    }
    try:
        global_params = request.GET.copy()
        global_params.update(request.POST)
        global_params.update(request.FILES)
        exec(global_params["method"].strip() + "(global_params, request, ret_json)");
        return HttpResponse(json.dumps(ret_json, ensure_ascii = False),
                content_type="application/json")
    except Exception, e:
        ret_json["is_success"] = False
        ret_json["value"]["error"] = str(e)
        print e
        return HttpResponse(json.dumps(ret_json, ensure_ascii = False),
                content_type="application/json")
