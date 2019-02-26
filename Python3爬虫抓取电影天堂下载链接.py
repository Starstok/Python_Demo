#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#power by Airo
#爬虫阳光电影下载链接


import urllib.request
import re
import time

def get(pages):
    for n in range(1,pages):                                                        #for循环一次从1-pages中取一次值
        url = 'http://www.ygdy8.net/html/gndy/oumei/list_7_'+str(n)+'.html'         #拿for循环中的取值进行拼接请求url，需要对应更新
        header = {                                                                  #请求头部
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
        }
        #print (url)
        req = urllib.request.Request(url,headers=header)                            #封装请求信息
        #html = urllib.request.urlopen(req).read().decode('gb2312')
        html = urllib.request.urlopen(req).read().decode('gbk','ignore')            #打开请求使用bgk编码，ignore属性进行忽略
        reg = r'<a href="(.+?)" class="ulink">(.+?)</a>'                            #正则表达式进行筛选
        reg_list = (re.findall(reg,html))                                           #筛选后的内容
        for i in reg_list:
            url = i[0]                                                              #reg_list内容的url
            #name = i[1]                                                            #reg_list内容的name
            url_1 = 'http://www.ygdy8.net'+url                                      #拼接请求url
            time.sleep(2)                                                           #延迟2s，如果良心尚存，就开启
            #print (url_1,name)                                                     #打印拼接后的url 和 reg_list里的nema
            req_1 = urllib.request.Request(url_1,headers=header)                    #封装请求信息
            html_1 = urllib.request.urlopen(req_1).read().decode('gbk','ignore')    #打开请求使用bgk编码，ignore属性进行忽略
            #html_1.encoding = 'gb2312'                                             #定义文本编码格式
            reg_1 = r'<a href="(.+?)">.+?</a></td>'                                 #正则表达式进行筛选ftp下载链接
            ftp_list = re.findall(reg_1,html_1)                                     #筛选后的内容
            
            fhandle=open('./ygdy.txt','a',encoding='utf-8')                         #写入内容到文件ygdy.txt
            fhandle.write(ftp_list[0]+'\n')                                         #开始写文件并且换行
get(2)                                                                              #调用get()函数，函数里的参数对应着页数内容

