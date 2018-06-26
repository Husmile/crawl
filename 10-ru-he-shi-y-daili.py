#!/usr/bin/python3
# * coding:utf-8 *
# 用户 ： Hu
# Time : 2018/6/26 0026  17:12


import urllib
import urllib.request
# ProxyHandler继承basehandler。httphandler也继承basehandler
# 用法一样
proxies = {'https':'123.161.236.19:30830'}
proxyHandler = urllib.request.ProxyHandler(proxies=proxies)
# 创建open  发起网络请求
opener = urllib.request.build_opener(proxyHandler)
response=opener.open(fullurl='http://www.baidu.com/')
print(response.read().decode('utf-8'))












































