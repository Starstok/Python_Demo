#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#power by Airo

import json

path = './py.json'                          #文件所在路径
file = open(path,'rb')                      #以二进制的方式从文件中读取数据
jsonData = json.load(file)                  #加载json文档

print (jsonData)
arr = jsonData['result']['tracks']          #取json文档里面 “result” 下面的 “tracks”值

for i in range(2):                          #for循环，i 在 range 取值范围内循环
    name = str(i+1) + arr[i]['name']        #序号 + “tracks” 下面的 “name”
    print (name)