#python3
#-*- coding:utf-8 -*-
#转义字符       功能
print('\a')#ASCII响铃符(BEL)
print('\b')#ASCII退格符(BS)
print('\f')#ASCII进纸符(FF)
#print('\N{name}')#Unicode数据库中的字符名，其中name是它的名字，仅适用Unicode，不知道name位置填什么。
print('\u6221')#Unicode16进制值
#print('\U12020201')#Unicode32进制值
print('\v')#ASCII垂直制表符(VT)
print('\ooo')#8进制的oo字符
print('\xff')#16进制数的hh字符
print('1*'*20)

#''和""是一样的
str1='Hello world'
str2="Hello world"
print(str1==str2)

#删除字符串中的空格
str1="   Hello,   world!    "
print(str1+'删除字符串中的空格')
print(str1.rstrip()+'没有了右侧空格')#删除右侧空格
print(str1.lstrip())#删除左侧空格
print(str1.strip())#删除全部空格

#首字母大写
str1='hello world'
print(str1.title())

#全部字符串大写或者小写
print(str1.upper())
print(str1.lower())

#\t和\n以及转义符号\
print('换行\n换行')
print('制表符\t制表符')
print('转义字符\'')

#拆分字符串
print(str1.split())
str1='hello ,alice'
print(str1.split())
print(str1.split(','))#以逗号为分隔符号拆分
