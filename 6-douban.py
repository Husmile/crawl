#!/usr/bin/python3
# * coding:utf-8 *
# 用户 ： Hu
# Time : 2018/6/26 0026  14:12
# 登录豆瓣
import urllib,ssl
import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.douban.com/people/164698173/'

# Cookier 模拟登陆
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
           'Cookie':'bid=Xjj632HO9iI; __yadk_uid=pEzIj2tEWsS125GeVKf5SN8rcRRkfmyt; ll="108288"; _ga=GA1.2.557027477.1504366471; _vwo_uuid_v2=938EB395FEDF0DA9E9D90650DE9042F0|e0a43720af285a1e9923074545b60ff1; gr_user_id=d044fe6a-3a16-4f08-ad14-cc71033b6767; ue="455098435@qq.com"; push_noty_num=0; push_doumail_num=0; ap=1; viewed="27055214_30203973_1088812"; _gid=GA1.2.795739151.1529892963; ps=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1529983342%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DK_4sZYVk6X3MTlACiyJ_sqJufjZAEyn-qOrCCUININKU11FQYOau93tYnIT-GH2u%26wd%3D%26eqid%3De44b5c720001feb5000000025b31b169%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.557027477.1504366471.1529939944.1529983346.45; __utmc=30149280; __utmz=30149280.1529983346.45.44.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; dbcl2="164698173:o44aKq3peKI"; ck=7f1r; __utmv=30149280.16469; _pk_id.100001.8cb4=8f22acb72a922fec.1516867546.35.1529983379.1529940121.; __utmb=30149280.5.10.1529983346'}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))






