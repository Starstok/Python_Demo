#!/usr/bin/python3
# -*- encoding:utf-8 -*-



# 网易云音乐批量下载

import urllib.request
import json

# 榜单歌曲批量下载
# r = requests.get('http://music.163.com/api/playlist/detail?id=2884035')  # 网易原创歌曲榜
# r = requests.get('http://music.163.com/api/playlist/detail?id=19723756') # 云音乐飙升榜
# r = requests.get('http://music.163.com/api/playlist/detail?id=3778678')  # 云音乐热歌榜
url = 'http://music.163.com/api/playlist/detail?id=3779629'    # 云音乐新歌榜

# 歌单歌曲批量下载
# r = requests.get('http://music.163.com/api/playlist/detail?id=123415635')    # 云音乐歌单——【华语】中国风的韵律，中国人的印记
# r = requests.get('http://music.163.com/api/playlist/detail?id=122732380')    # 云音乐歌单——那不是爱，只是寂寞说的谎

header = {
         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
   }

req = urllib.request.Request(url,headers=header)      #封装请求
data = urllib.request.urlopen(req).read().decode()    #请求url获取数据并解码，字符串的形式显示
json_Data = json.loads(data)                          #加载字符串并转成json，loads = load string

arr = json_Data['result']['tracks']                   # 提取json数据
#print (arr)

def callback(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum:  已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print ('%.2f%%'% percent)                         # %.2f 表示浮点型保留小数点后两位格式输出，%% 会显示一个%号，% 含有转义功能

for i in range(5):                                    # 输入要下载音乐的数量，1到100。
   name = str(i+1) + arr[i]['name'] + '.mp3'          #序号+name+后缀名，
   link = arr[i]['mp3Url']                            #arr[]下面的mp3Url
   urllib.request.urlretrieve(url,name,callback)      # 下载到当前目录
   print(name + ' 下载完成')