#!/usr/bin/python3
# * coding:utf-8 *
# 用户 ： Hu
# Time : 2018/6/26 0026  11:10


import urllib,ssl
import urllib.request

url = 'http://www.asfaff.com'

try :response=urllib.request.urlopen(url=url)
except Exception as e:
    print(e)
#     发起联网请求，将错误发给服务器，log。方便修改代码


print(response.read().decode('utf-8'))