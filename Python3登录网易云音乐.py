#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#power by SEOK

import urllib.request
import urllib.parse
import re
import time
import http.cookiejar
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8') #改变标准输出的默认编码

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

def login():
    url = 'http://music.163.com/weapi/login/cellphone?csrf_token='
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }

    data = {
        'params':'uaffXNZsX/k17ZnfCvE3X0mvI6dztxduvv54unaI+t0ESme9pJX4fWLAGZKNmFuiM+6I0fCrazfuC2jE5qeL4x7GEfNpDWHTpmeTzcqz3YRZrVg9051U/QGh/yiNPuE7n/+OKj3CvdXGm4SUkG4XZYY3H16Oy6EzzIVMjgmPieX3jmU9XfFtIeOX6wMGLLgxPsthl4N02/yR9K8N+Ixv5w==',
        'encSecKey':'a31c6441798085ccf35462b2ce9731ece8dcddc459ded7dfe0a2bcf5490ec617c75ffa7d9b6b5576b548f5499d26c8ec6917c265d3d6b811cf7b264a401a0a88ab6dc23ebbe3e5fa8804aabf3f38503b7d4671c2cdf2ea89cbd1936ea8bfa8d8780ba21a6ae39e04cf06d644009bfc1fe5b931b26625973139f5cd6f2fbc1c68'
        # 'params':'tldRw7De58135MgILPKpQN5CsLn0qQr/MTku5Hbn0PJIHwrVjhHLDhyp1mj28Zfaq0d3Wiy3wvzIlaoco4BwoXKO73q4gCJyMTmyiIEPKphXusKpeT5bS95506AOS5U/J88fDGG3zIP1SkuVy34v6dJQr519XpJ/EHBK5xeVnkViVnnDitzJ/yOZw+4zbtoebqYye/2gtvFiVWAWVyvY9A==',
        # 'encSecKey':'d8ca373059681f7baad586c49d11583efeb64e666ab669c72212a61705cb3b579ff144c1ca21bad3fa084c9d6a53f9e8fad678ef1ee479a8528f757f4c23145c6cd41dd14642d854d24998c0a182d710732e0aa4c5ee5d182a1e2a4e842e944c1cf46019a0c4d1696686c00c26333d6e83e84d27b0b56c6cc8923913a6153ebb'
        }
    postdata = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url,postdata,header)
    #html = urllib.request.urlopen(req).read().decode('utf-8')
    html = opener.open(req).read().decode('utf-8')
#     print (html)
# login()
    return html
if 'loginType":1' in login():
    print ("登录成功")
elif '502' in login():
    print ("登录失败，密码错误")
elif '509' in login():
    print ("登录失败，密码错误超过限制")
else:
    print ("登录失败")

def getlist():
    url = 'http://music.163.com/weapi/user/playlist?csrf_token=5416d095c429bb5d082660abe3677dd6'
    header = {
        'Origin':'http://music.163.com',
        'Referer':'http://music.163.com/user/home?id=49668677',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }

    data = {
        'params':'SuxlK1iHj58OP/gGc3feIPaKIgIhJ+rRQ1YpxvQ3+4aj0V3cuKIBPLLTimN/fX6D/sMrI0wHbTo4Ai8y6mKSUV6+vfdJp3bxVuop+dWfkHGz8VIkS8N0mIbhXNyZnpDyAWnG0PCuPFk+O0oKmlBMOwhmO9fwn3KZVT1T66bliRzSFkZ+U/QQKUQqwUgci9l2UwtE6F6bYc8rbOG4Xkd8Fjz/JUo2cnhxFyCbExjmINI=',
        'encSecKey':'19ddb86b0cb50fe7dc1184765e2958ca5f243d0fcd41362bb46f90add399538379649db3ada792cd2e518e630160a451ca62d969b957e4ee794d72368af27fa9b90a6c36644309de27a2df3d9a196ef0abad15612c839180157239f856f00b75803d53da24e3402fb56aa2757bcc8d830d74f91c57340461e7db92ea563a2391'
    }
    portdata = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url,data=portdata,headers=header)
    html = opener.open(req).read().decode('utf-8')
    #html = str(html)
    print (html)
getlist()



