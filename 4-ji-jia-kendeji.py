#!/usr/bin/python3
# * coding:utf-8 *
# 用户 ： Hu
# Time : 2018/6/26 0026  10:44
import urllib.parse
import urllib,ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
# ajsx  post
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=pid'

# get  有的可以用 在百度框输入 pageSize相当于数据库limit函数。这个网址是直接和数据库连接的
url_get = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=pid&cname=&pid=13&pageIndex=8&pageSize=10'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
           'Connection':'Keep-alive',
           'Accept-Language':'zh-CN,zh;q=0.9'}
'''
cname=&pid=13&pageIndex=8&pageSize=10

'''



if __name__ == '__main__':
    city = input('请输入查询的城市：')
    page = int(input('请输入查询的页数：'))

    for p in range(1,page+1):

        form = {'cname': city,
                'pid': 31,
                'pageIndex': p,
                'pageSize': 50}
        form = urllib.parse.urlencode(form).encode('utf-8')
        request = urllib.request.Request(url=url,data=form,headers=headers)

        respnose = urllib.request.urlopen(request)

        content = respnose.read().decode('utf-8')

        with open('./download/肯德基第%d页.json'%(p),mode='wb')as fp:
            fp.write(content.encode('utf-8'))
            # 乱码  加载wb utf
            # with open('./download/肯德基第%d页.json' % (p), mode='wb')as fp:
            # fp.write(content.encode('utf-8'))