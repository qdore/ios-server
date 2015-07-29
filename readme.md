##接口文档

注册
get/post:
返回的token是用户获取数据的凭据（该token与电话一一绑定，作为请求用户数据的凭证）
```
method: regist
tel: 11111111111
pwd: password
user_id: 身份证号或工号
例:
    http://0.0.0.0:8086/ios/?method=regist&tel=13213211432&pwd=123&user_id=test123
return:
    {"is_success": true, "value": {"token": "umjDMLhnwYBTdEUIvcqVCfWgeNtJXaZKoSPOlzQpxbskARFHyG"}}
```

登录
get/post:
返回的token是用户获取数据的凭据（该token与电话一一绑定，作为请求用户数据的凭证）
```
method: login
tel: 11111111111
pwd: password
例:
    http://0.0.0.0:8086/ios/?method=login&tel=18723111412&pwd=123
return:
    {"is_success": true, "value": {"token": "umjDMLhnwYBTdEUIvcqVCfWgeNtJXaZKoSPOlzQpxbskARFHyG"}}
```




