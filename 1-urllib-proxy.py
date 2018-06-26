#!/usr/bin/python3
# * coding:utf-8 *
# 用户 ： Hu
# Time : 2018/6/26 0026  9:28

''''
 <tr class="odd">
    <td class="country"><img src="./免费代理IP_HTTP代理服务器IP_隐藏IP_QQ代理_国内外代理_西刺免费代理IP_files/cn.png" alt="Cn"></td>
    <td>118.190.95.35</td>

    <td>9001</td>

    <td>广西</td>
    <td class="country">高匿</td>
    <td>HTTP</td>
      <td>3天</td>
    <td>1分钟前</td>
  </tr>
  '''

import urllib
import urllib.request
import re

pattern = r'<td>([\d\.a-zA-Z\/]+)</td>'
with open('./proxy.html',mode='r',encoding='utf-8')as fp:
    proxy = fp.read()
    p = re.compile(pattern=pattern)
    proxies = re.findall(pattern=p,string=proxy)

    print(proxies)
    print(len(proxies))
