#!/usr/bin/python3
# * coding:utf-8 *
# 用户 ： Hu
# Time : 2018/6/26 0026  14:27

import urllib
import urllib.request
import re

url = 'http://zs.1000phone.net/Collect/index/zone_id/0/course_id/50'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
           'Cookie':'PHPSESSID=tt905b2lger16dq3q9ijsn3o91'}
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
print(content)
'''招生数量HTML源代码
		<td style="text-align:left;">39</td>

'''
pattern = r'<td style="text-align:left;">([\d]+)</td>'
p = re.compile(pattern=pattern)

data = re.findall(pattern=p,string=content)
print(data)

print(len(data))
with open('./download/qf.html','wb') as fp:
    fp.write(content.encode('utf-8'))

# b = [int(i) for i in s]
# print(sum(b))









































