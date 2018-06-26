#!/usr/bin/python3
# * coding:utf-8 *
# 用户 ： Hu
# Time : 2018/6/26 0026  11:58



import urllib
import urllib.request

http_handele = urllib.request.HTTPHandler()


opener = urllib.request.build_opener(http_handele)

# 方式一 直接使用opener发起请求
# 方式二 ，将opener作为参数设置为urllib.request.urlopen
# opener就变成全局的联网请求了
urllib.request.install_opener(opener)


# urllib.request.urlopen()#相当于使用oper.open()
response = urllib.request.urlopen('http://www.baidu.com')

print(response.read().decode('utf-8'))