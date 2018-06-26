#!/usr/bin/python3
# * coding:utf-8 *
# 用户 ： Hu
# Time : 2018/6/26 0026  9:40
import urllib,ssl
import urllib.request
import urllib.parse
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%d'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
 }


def write_to_file(content,i):
    with open('./download/贴吧第%d页.html'%(i+1),mode='wb') as fp:
        fp.write(content.encode('utf-8'))
        print('忒把第%d保存成功'%(i+1))


def load_url_data(key,num):
    for i in range(num):
        url_detail = url%(key,i*50)

        request = urllib.request.Request(url=url_detail,headers=headers)
        response = urllib.request.urlopen(request)
        # read()方法只能读一次，第二次吗，内容 了

        content = response.read().decode('utf-8')

        write_to_file(content,i)

        print('----------',response.read())

if __name__ == '__main__':
    # key是str类型的 import urllib.parse转
    key = input('请输入贴吧关键字')
    # urllib.parse.unquote()
    key = urllib.parse.quote(key)
    try:
        num = int(input('请输入页码:'))
    except Exception as e :
        print('请输入数字')

        num = int(input('请输入页码:'))

    load_url_data(key,num)














