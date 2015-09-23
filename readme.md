##接口文档

####注册
get/post:
返回的token是用户获取数据的凭据（该token与电话一一对应，作为请求用户数据的凭证）
```
method: regist
tel: 11111111111
pwd: password
user_id: 身份证号或工号
user_type: 0,1 [0:摄影师 1:制片人]
例:
    http://0.0.0.0:8086/ios/?method=regist&tel=13213211432&pwd=123&user_id=test123&user_type=0
return:
    {"is_success": true, "value": {"token": "umjDMLhnwYBTdEUIvcqVCfWgeNtJXaZKoSPOlzQpxbskARFHyG"}}
```

####登录
get/post:
返回的token是用户获取数据的凭据（该token与电话一一对应，作为请求用户数据的凭证）
```
method: login
tel: 11111111111
pwd: password
user_type: 0,1 [0:摄影师 1:制片人]
例:
    http://0.0.0.0:8086/ios/?method=login&tel=18723111412&pwd=123&user_type=0
return:
    {"is_success": true, "value": {"token": "umjDMLhnwYBTdEUIvcqVCfWgeNtJXaZKoSPOlzQpxbskARFHyG"}}
```

####修改密码
get/post:
```
method: changePassword
token: umjDMLhnwYBTdEUIvcqVCfWgeNtJXaZKoSPOlzQpxbskARFHyG
pwd: password
new_pwd: new password
例:
    http://0.0.0.0:8086/ios/?method=changePassword&token=IxZORjTaDEPdbrWficgJwBheXzYqvGVFKMptuLSQlCyANkHsom&pwd=123&new_pwd=12345
return:
    {"is_success": false, "value": {"error": "username or password error!"}}
```

####更新用户信息
get/post:
```
method: updateUserInfor
token: key
name: 用户名
gender: 0,1 [0：男， 1：女]
head_photo: 图片
brief: 简介
例:
    http://0.0.0.0:8086/ios/?method=updateUserInfor&token=IxZORjTaDEPdbrWficgJwBheXzYqvGVFKMptuLSQlCyANkHsom&name=kidney&gender=0&brief=xxx
return:
    {"is_success": true, "value": {}}

```

####获取用户信息
get/post:
```
method: getUserInforByTel
token: key
tel: 13111111111
例:
    http://0.0.0.0:8086/ios/?method=getUserInfor&tel=13111111111
return:
    {"is_success": true, "value": {"gender": "0", "name": "kidney", "brief": "xxx"}}
    增加了返回 head_photo
    增加了返回 status

```

####get/post:
```
method: getUserInforByToken
token: key

例:
    http://0.0.0.0:8086/ios/?method=getUserInfor&token=xxx
return:
    {"is_success": true, "value": {"gender": "0", "name": "kidney", "brief": "xxx"}}
    增加了返回 head_photo
    增加了返回 status

```

####发表状态
post:
```
method: publishStatus
token: key
brief: 发表状态的内容
pic0: 上传的图片0
pic1: 上传的图片1
pic2: 上传的图片
pic3: 上传的图片
pic4: 上传的图片
    ...

return:
    {"is_success": true, "value": {}}

```

####获取我发表的状态
get/post:
```
method: getMyStatus
token: key
例：
    http://0.0.0.0:8086/ios/?method=getMyStatus&token=duCpbeUOTRfvhSkZAzXltnENDHMFwPsBIcryWmaxgKiYjQJVLo

return:
{"is_success": true, "value": {"status": [{"praisers": [], "pictures": [], "brief": "xxx", "status_id": 1}, {"praisers": [], "pictures": [], "brief": "xxx", "status_id": 2}, {"praisers": [], "pictures": ["0.0.0.0:8086/media/./13712045932161_dULEtZO.png"], "brief": "啊收到就好", "status_id": 3}, {"praisers": [], "pictures": ["0.0.0.0:8086/media/", "0.0.0.0:8086/media/./13712045932161.png"], "brief": "xxxxxxx", "status_id": 4}, {"praisers": [], "pictures": [], "brief": "xxxxxxx", "status_id": 5}, {"praisers": [], "pictures": [], "brief": "xxxxxxx", "status_id": 6}]}}

is_success: true
value: {
            status:[
                   {
                        status_id:标识状态的状态码（点赞等操作根据status_id）
                        praisers: {
                            tel:点赞者手机号
                            head_photo: 点赞者头像
                            name: 名称
                        }
                        pictures:状态图片的url
                        brief:状态发表的言论
                        name:发送者的名称
                        head_photo: 发送者头像
                        is_praise:是否点赞
                        comment: [
                            {
                                comment_id: 标识评论
                                content: 评论内容
                                commenter: 评论者
                                commenter_head_photo: 评论者头像
                                comment_by: 被评论者
                                comment_by_head_photo: 被评论者头像
                            },
                            ...
                        ]
                   },
                   ...
            ]
       }
```

####点赞
get/post
```
method: praiseStatus
token: key
status_id: 要点赞的状态标识码
例：
    http://0.0.0.0:8086/ios/?method=praiseStatus&token=duCpbeUOTRfvhSkZAzXltnENDHMFwPsBIcryWmaxgKiYjQJVLo&status_id=2

return:
    {"is_success": false, "value": {"error": "重复点赞!"}}
```

####获取从n条开始的状态记录(全局), 返回42条
get/post:
```
method: getNStatus
token: key
n: n条记录的数值
例：
    http://0.0.0.0:8086/ios/?method=getNStatus&token=duCpbeUOTRfvhSkZAzXltnENDHMFwPsBIcryWmaxgKiYjQJVLo&n=2

```

####获取别人发表的状态
get/post:
```
method: getSomeOneStatusByTel
tel: 12233334444
token: key
例：
    http://0.0.0.0:8086/ios/?method=getSomeOneStatusByTel&tel=12233334444


```

####广场找人
get/post
```
method: findSomeOne
token: key
para: 搜索内容(可以是用户名手机号id等)

例:
    http://0.0.0.0:8086/ios/?method=findSomeOne&para=132132114
return:
    {"is_success": true, "value": {"person": [{"gender": "", "tel": "13213211432", "user_id": "test123", "name": "", "brief": ""}, {"gender": "", "tel": "13213211421", "user_id": "test123", "name": "", "brief": ""}]}}

person:搜索结果
gender：性别
tel: 搜索到的手机号
user_id: 身份证号或者工号
name: 名称
head_photo: 头像
type: 职业
is_friend: 是否是好友
brief: 简介
status: [] //和getMyStatus返回一样
```

####加关注
get/post
```
method: addSomeOneAsFriend
token: key
attented_tel: 我关注的人的手机号

例：
    http://0.0.0.0:8086/ios/?method=addSomeOneAsFriend&token=duCpbeUOTRfvhSkZAzXltnENDHMFwPsBIcryWmaxgKiYjQJVLo&attented_tel=18721919502

return:
    {"is_success": true, "value": {}}
```

####获取某人的关注信息
get/post
```
method: getAttentRelation
tel: `某人`的手机号

例：

return:
    {"is_success": true, "value": {"attent_by_someone": ["18721919502"], "attent_someone": ["18721919502"]}}

attent_by_someone: 被某人关注
attent_someone：关注的人

```

####发送站内信
get/post
```
method: sendMsg
token: key
tel: 接收者的手机号
content: 发送的信息内容
例:
    http://0.0.0.0:8086/ios/?method=sendMsg&token=duCpbeUOTRfvhSkZAzXltnENDHMFwPsBIcryWmaxgKiYjQJVLo&receiver=18392319234&content=test

return:
    {"is_success": true, "value": {}}
```

####接受站内信
get/post
```
method: getMsg
token: key
例:
    http://0.0.0.0:8086/ios/?method=getMsg&token=duCpbeUOTRfvhSkZAzXltnENDHMFwPsBIcryWmaxgKiYjQJVLo

return:
    {"is_success": true, "value": {"msgs": [{"content": "test", "sender": "18721919502"}]}}

注意：每次获取成功之后未读信息列表自动清空

注意：这里需要判断一下， 当sender == "_system_praise" 时返回的结构体是：
sender: _system_praise
status_id: 状态标识
praiser: {
    name
    head_photo
    tel
}

当sender == "_system_comment" 时返回的结构体是：
sender: _system_comment
status_id: 状态标识
commenter: {
    name
    head_photo
    tel
}
content: 评论内容


其它
sender:发信人
sender_head_photo:发信人
content: 内容

```

####取消赞
get/post
```
method: undoPraise
token: key
status_id: 要取消赞的状态标识码
例：
    http://0.0.0.0:8086/ios/?method=undoPraise&token=duCpbeUOTRfvhSkZAzXltnENDHMFwPsBIcryWmaxgKiYjQJVLo&status_id=2

return:
    {"is_success": true, "value": {}}
```

####评论
有两级评论：
1. 评论状态
get/post
```
method: commentStatus
token: key
status_id: 状态的标识码
content: 评论
例：
    http://0.0.0.0:8086/ios/?method=commentStatus&token=duCpbeUOTRfvhSkZAzXltnENDHMFwPsBIcryWmaxgKiYjQJVLo&status_id=2&comment=xxx

return:
    {"is_success": true, "value": {}}
```

2. 评论其它评论
get/post

```
method: commentOtherComment
token: key
comment_id: 评论的状态码
content: 评论
例：
    http://0.0.0.0:8086/ios/?method=commentOtherComment&token=duCpbeUOTRfvhSkZAzXltnENDHMFwPsBIcryWmaxgKiYjQJVLo&comment_id=2&comment=xxx

return:
    {"is_success": true, "value": {}}
```
####获取从n条开始的状态记录(朋友圈), 返回42条
get/post:
```
method: getFriendStatus
token: key
n: n条记录的数值
例：
    http://0.0.0.0:8086/ios/?method=getFriendStatus&token=duCpbeUOTRfvhSkZAzXltnENDHMFwPsBIcryWmaxgKiYjQJVLo&n=2

return:
{"is_success": true, "value": {"status": [{"praisers": [], "pictures": [], "brief": "测试", "status_id": 10}, {"praisers": [], "pictures": ["0.0.0.0:8086/media/./13712045932161_qFgYqIX.png"], "brief": "xxx", "status_id": 9}]}}

is_success: true
```

####取消关注
get/post
```
method: cancelFriend
token: key
tel: 我关注的人的手机号

例：
    http://0.0.0.0:8086/ios/?method=cancelFriend&token=duCpbeUOTRfvhSkZAzXltnENDHMFwPsBIcryWmaxgKiYjQJVLo&tel=18721919502

return:
    {"is_success": true, "value": {}}
```


####发起工作(制片人发起)
post
```
method: sponseJob
title: 工作标题
user_time: 使用时间
city: 城市
authorizer: 批准人
position： 工作单位
reason： 申请理由
details: 设备及人员明细
opinion: 领导人意见
memo： 备注
sponsor_name: 申请人姓名
studio： 演播室
job_number: 部门/工号
time： 申请日期
camera: 摄影机
broadcast_car: 转播车
later_period: 后期
pic: 工作图片

例:

```

####申请工作(摄影师发起)
get/post
```
method: applyJob
job_id: 用来标识job

例: 
    http://0.0.0.0:8086/ios/?method=applyJob&token=144250497398qfFLDwKcvMEHjrlyXRAhVkzOBmaePiNobuCxUZ&job_id=1
```

####我申请的/我发布的工作
```
method: getMyJob

return:
[
    {
	job_id: job id
        title: 工作标题
        user_time: 使用时间
        city: 城市
        authorizer: 批准人
        position： 工作单位
        reason： 申请理由
        details: 设备及人员明细
        opinion: 领导人意见
        memo： 备注
        sponsor_name: 申请人姓名
        sponsor_tel: 发起者手机号
        studio： 演播室
        job_number: 部门/工号
        time： 申请日期
        pic: 工作图片
        camera: 摄影机
        broadcast_car: 转播车
        later_period: 后期
        approve_applier: {
		        gender：性别
		        tel: 搜索到的手机号
		        user_id: 身份证号或者工号
		        name: 名称
		        head_photo: 头像
		        type: 职业
		        is_friend: 是否是好友
		        brief: 简介
                status: 状态
            }

        appliers:[
            {
		        gender：性别
		        tel: 搜索到的手机号
		        user_id: 身份证号或者工号
		        name: 名称
		        head_photo: 头像
		        type: 职业
		        is_friend: 是否是好友
		        brief: 简介
                status: 状态
            },
        ]
        is_applyed: 是否申请
    },
]

```

####广场中的工作
```
method: getSquareJob
status: 状态 '0': '招聘中', '1': '已分配', '2': '已完成',

return:
    同上
```

###确认工作（制片人发起）
get/post
```
method: confirmJob
job_id: 用来标识job
tel: 讲工作分配给谁的手机号
```

###删除工作（制片人发起）
get/post
```
method: delJob
job_id: 用来标识job
```

###提交认证
get/post
```
method: submitAuth
token: key
true_name: 真实姓名
identity: 身份证号
identity_photo: 身份证图
work_photo: 工作图

```

###外出申请
get/post
```
method: applyOut
token: key
start_time: 开始时间
end_time: 结束时间
reason: 原因
```

###获取状态详情
get/post
```
method: getStatusById
token: key
status_id: status标识

return：

value: 
    {
         status_id:标识状态的状态码（点赞等操作根据status_id）
         praisers: {
             tel:点赞者手机号
             head_photo: 点赞者头像
             name: 名称
         }
         pictures:状态图片的url
         brief:状态发表的言论
         name:发送者的名称
         head_photo: 发送者头像
         is_praise:是否点赞
         comment: [
             {
                 comment_id: 标识评论
                 content: 评论内容
                 commenter: 评论者
                 commenter_head_photo: 评论者头像
                 comment_by: 被评论者
                 comment_by_head_photo: 被评论者头像
             },
             ...
         ]
    }

```


