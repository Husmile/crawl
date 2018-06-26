#!/usr/bin/python3
# * coding:utf-8 *
# 用户 ： Hu
# Time : 2018/6/26 0026  11:49



import urllib
import urllib.request
# 可以获取简单的网页函数
urllib.request.urlopen(url='http://www.baidu.com')



# 构建请求为了添加header，伪装成游览器，
# 可以获取登录之后才能获取得数据（cookie）
#


# header引入  就是为了使用代理


httpHandler = urllib.request.HTTPHandler()
# 打开一个网址
opener = urllib.request.build_opener(httpHandler)

#opener 访问网络数据  urllib.request.urlopen()一样

# 给个http
# response = opener.open(fullurl='http://www.baidu.com')
# 给个request
request = urllib.request.Request(url='http://www.baidu.com')
response = opener.open(request)


print(response.read().decode('utf-8'))
