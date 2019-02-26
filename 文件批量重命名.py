# -*- coding:UTF-8 -*-  
#zc  
import os  
path = input(u'C:\Users\Starstok\AppData\Local\Netease\CloudMusic\Cache:')  
path = path + "/Cache"  
files = os.listdir(path)  
for f in files:  
    name, extname = f.split('.')  
    if extname == "uc":  
        os.chdir(path)  
        print (name, extname)  
        os.rename(f, '%s.mp3' %name)  
