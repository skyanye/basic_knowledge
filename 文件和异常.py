#!python3
#-*- coding:utf-8 -*-

#打开文件
with open('pi_digits.txt') as file_object:
    contents=file_object.read()
    print(contents)
print('1*'*20)

#逐行读取文件，逐行读取会读到\n这样的字符，同时print也会产生一个换行符
fileName='pi_digits.txt'
with open(fileName) as file_object:
    for line in file_object:
        print(line)
print('2*'*20)

#包含文件各行内容的列表
fileName='pi_digits.txt'
with open(fileName) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line)
print('3*'*20)

#写入多行文件,以w打开时会重写文件
fileName='program.txt'
with open(fileName,'w') as file_object:
    file_object.write('hello,\nworld')
print('4*'*20)

#附加到文件
fileName='program.txt'
with open(fileName,'a') as file_object:
    file_object.write('\nadd')
print('5*'*20)

#将有可能出错的内容放到try里
try:
    print(5/1)#这里改为除以0的话else就不会被执行
except:
    print('不能除0')
else:
    print('pass')#这里只有在try里面成功执行以后才会执行
print('6*'*20)

#JSON方式保存数据，存储使用json.dump()，取出使用json.load()
import json
numbers=[value+2 for value in range(1,10)]
filename='numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
with open(filename) as f_obj:
    nums=json.load(f_obj)
print(numbers)
print(nums)
print('7*'*20)

#split()用于对单词进行拆分
str1="Alic in Wonderland"
list1=str1.split()
print(list1)
print('8*'*20)

#pass语句，什么都不做
