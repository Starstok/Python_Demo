#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#power by SEOK

import urllib.request
import http.cookiejar
import re
import time

                                                                        # 自动保存cookie
cj = http.cookiejar.CookieJar()                                         #创建一个cj 来保存cookie
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

                                                                        #登陆请求的url
                                                                        #请求的方式 port
                                                                        #请求的data
def login():
    url ='https://www.ks5u.com/user/inc/UserLogin_Index.asp'            #请求的url
    header = {                                                          #请求头部
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }

    #post请求表单数据
    data = {'username':'928130267@qq.com','password':'LYQH12345','c_add':'1'}
    postdata = urllib.parse.urlencode(data).encode('utf8')              #进行编码
    request = urllib.request.Request(url,postdata,header)
 
    #html=urllib.request.urlopen(request).read().decode('gb2312')       #打开url
    html = opener.open(request)
    #html=str(html)                                                     #转换成str
    return (html.read().decode('gb2312'))
if 'False' in login():
    print ("登录成功")
else:
    print ("登录失败")


def getfile(name,id):
    url = 'https://www.ks5u.com/USER/INC/DownCom.asp?id=%s'             #下载链接+id，就是真实下载地址
    request = urllib.request.Request(url %id)                           #拼接请求链接
    #print (opener.open(request).read())                                #打印下载文件内容
    open('./'+name +'.doc','wb').write(opener.open(request).read())     #wb：以二进制的方式写入


def getlist():
    url = 'https://www.ks5u.com/special/2017/fxhb/yuwen.html'           #请求的url
    header = {                                                          #请求头部
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }
    request = urllib.request.Request(url=url,headers=header)
    html = opener.open(request).read().decode('utf-8')
    #html3=str(html2)                                                   #转换成str
    reg = r'<td align=.+? bgcolor=.+? style=.+?>(.+?)</td>  <td align=.+? bgcolor=.+?><a href=/(.+?) target='
    return re.findall(reg,html)
    #return html
for i in getlist():
    # i = ('名字','url')                                                #i 这个组里有两部分, i 是reg里面的内容
    # i[0]='名字'
    # i[1]='url'
    #print (i)
    name = i[0]
    url = i[1]
    print (name)
    #id = url.split('/')[-1].split('.')[-2]                             #先用/分割拿最后一部分，再次用.分割那倒数第二部分
    id = url.split('/')[-1][:-6]                                        #用/分割那最后一部分，用最后一部分切片，从后面开始切，切掉后面没用的6位
    getfile (name,id)
    time.sleep(2)
    break

