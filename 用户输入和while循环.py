#!python3
#-*- coding:utf-8 -*-
import random
#input()
message=input('请输入一个值：')#只接收一个参数，打印出说明
print(message)
print('*'*20)

#删除列表中所有是1的值
num=[]
for i in range(1,20):
    num.append(random.randint(1,3))
print(num)
while 1 in num:
    num.remove(1)
print(num)
print('*'*20)
