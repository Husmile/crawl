#!/usr/bin/python3
# * coding:utf-8 *
# 用户 ： Hu
# Time : 2018/6/26 0026  17:23


import urllib
import urllib.request
import os
# 将用户名密码保存到环境变量中


pw = os.environ.get('password')
server =os.environ.get('server')
user = os.environ.get('user')

print(server)
print(user)
# proxies = {'http':'455098435:mima@115.28.67.91:16817'}
proxies = {'http':'%s:%s@%s:%s'%(user,pw,server)}


proxy_handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(proxy_handler)

response = opener.open('http://www.baidu.com/')
print(response.read().decode('utf-8'))