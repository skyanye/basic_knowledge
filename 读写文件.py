#-*- coding:utf-8 -*-
import os

#os.path.join()将文件名和路径串连起来
print(os.path.join('usr','bin','spam'))
print('1*'*20)

#os.getcwd()获取当前路径
print(os.getcwd())
print('2*'*20)

#os.chdir()改变路径
os.chdir('C:\\')
print(os.getcwd())
print('3*'*20)

#.表示这个目录，..表示父文件夹

#os.path.abspath(path)返回绝对路径
#os.path.isabs(path)如果参数是一个绝对路径就返回True
#os.path.relpath(path,start)返回从start到path的相对路径
#os.path.dirname(path)将返回一个字符串，它包含path参数中最后一个斜杠前的所有内容
#os.path.basename(path)返回最后一个斜杠后的内容
#需要文件名和基本名就要os.path.split()
print(os.path.split('E:\\python\\a.txt'))
print('4*'*20)

#os.path.sep指文件分隔符号

#os.path.getsize(path)返回path参数中文件的字节数
#os.listdir(path)返回文件名字符串的列表
os.chdir('E:\\python\\')
for i in os.listdir('E:\\python\\'):
    print(i,'文件大小%dKB'% os.path.getsize(i))
print('5*'*20)

#shelve模块保存变量
import shelve
cats=['a','b','c']
with shelve.open('mydata') as fp:
    fp['cats']=cats
    print(fp['cats'])

#pprint.format()保存变量
