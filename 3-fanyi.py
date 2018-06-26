#!/usr/bin/python3
# * coding:utf-8 *
# 用户 ： Hu
# Time : 2018/6/26 0026  10:03

# 百度翻译
import json
import urllib.parse
import urllib,ssl
import urllib.request
#post请求百度翻译，对form要求严格
url = 'http://fanyi.baidu.com/v2transapi'
ssl._create_default_https_context = ssl._create_unverified_context
'''
from=zh&
to=en&
query=%E8%91%A1%E8%90%84%E7%89%99&
类型
transtype=realtime&
simple_means_flag=3&
sign=218425.505352& 这个参数必须一致
token=11f0f260e25550c970877974d71a9ffb 大部分一样
'''
# 不需要pase转码
key = input('请输入翻译的汉字')

form = {'from':'zh',
        'to':'en',
        'query':key,
        'transtype':'realtime',
        'simple_means_flag':3,
        'sign':'447201.143824',
        'token':'08d1aad7369616eeeda6963a6a1f7a23'}


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
           'Referer':'http://fanyi.baidu.com/?aldtype=16047','Cookie':'__cfduid=d4239d00cf28765faa236f6608b6608881505905792; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSTM=1516063589; BIDUPSID=3F36E6E1D84B20491F59AC388BCE71F2; BDUSS=dkZ1gwSGUzR2hvQ2VER2tVZURRbk51MTlBMzgzRURZRmNTRThjcmNNc0x0ak5iQVFBQUFBJCQAAAAAAAAAAAEAAADcsb9ywre34cCkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAspDFsLKQxbQk; BAIDUID=2C5BBBEC7A2BB76A07710F1974341E48:FG=1; BDRCVFR[mkUqnUt8juD]=mk3SLVN4HKm; PSINO=2; H_PS_PSSID=26654_1463_21084; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1527496949,1527560247,1528420326,1529978381; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1529978381; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D',
           'Host':'fanyi.baidu.com'}
form = urllib.parse.urlencode(form).encode('utf-8')

request = urllib.request.Request(url=url,headers=headers,data=form)

# 构建请求头试一下
response = urllib.request.urlopen(request)
# 'unicode-escape' 加上这句 否则是十六进制的中文吧
# 使用json
content = response.read().decode('utf-8')

print(content)

# 首先使用json加载，编码到utf-8
# 然后dump编码不采用ASCII
content = json.dumps(json.loads(content,encoding='utf-8'),ensure_ascii=False)
print(content)