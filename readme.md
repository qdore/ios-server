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
tel: 13111111111
例:
    http://0.0.0.0:8086/ios/?method=getUserInfor&tel=13111111111
return:
    {"is_success": true, "value": {"gender": "0", "name": "kidney", "brief": "xxx"}}

```

####get/post:
```
method: getUserInforByToken
token: key

例:
    http://0.0.0.0:8086/ios/?method=getUserInfor&token=xxx
return:
    {"is_success": true, "value": {"gender": "0", "name": "kidney", "brief": "xxx"}}

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
                        praisers:点赞者手机号
                        pictures:状态图片的url
                        brief:状态发表的言论
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

####获取最近的n条状态记录(全局)
get/post:
```
method: getNStatus
token: key
n: n条记录的数值
例：
    http://0.0.0.0:8086/ios/?method=getNStatus&token=duCpbeUOTRfvhSkZAzXltnENDHMFwPsBIcryWmaxgKiYjQJVLo&n=2

return:
{"is_success": true, "value": {"status": [{"praisers": [], "pictures": [], "brief": "测试", "status_id": 10}, {"praisers": [], "pictures": ["0.0.0.0:8086/media/./13712045932161_qFgYqIX.png"], "brief": "xxx", "status_id": 9}]}}

is_success: true
value: {
            status:[
                   {
                        status_id:标识状态的状态码（点赞等操作根据status_id）
                        praisers:点赞者手机号
                        pictures:状态图片的url
                        brief:状态发表的言论
                   },
                   ...
            ]
       }

```

####获取别人发表的状态
get/post:
```
method: getSomeOneStatusByTel
tel: 12233334444
例：
    http://0.0.0.0:8086/ios/?method=getSomeOneStatusByTel&tel=12233334444

return:
{"is_success": true, "value": {"status": [{"praisers": [], "pictures": [], "brief": "xxx", "status_id": 1}, {"praisers": [], "pictures": [], "brief": "xxx", "status_id": 2}, {"praisers": [], "pictures": ["0.0.0.0:8086/media/./13712045932161_dULEtZO.png"], "brief": "啊收到就好", "status_id": 3}, {"praisers": [], "pictures": ["0.0.0.0:8086/media/", "0.0.0.0:8086/media/./13712045932161.png"], "brief": "xxxxxxx", "status_id": 4}, {"praisers": [], "pictures": [], "brief": "xxxxxxx", "status_id": 5}, {"praisers": [], "pictures": [], "brief": "xxxxxxx", "status_id": 6}]}}

```

####广场找人
get/post
```
method: findSomeOne
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
brief: 简介
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

发送站内信(Todo)
接受站内信(Todo)






