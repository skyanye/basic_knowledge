#!python3
#-*- coding:utf-8 -*-

#参数是有顺序的
def pet(name,petType):
    print(name,petType)
pet('呆呆哒','hamster')
pet('hamster','呆呆哒')
print('*'*20)

#关键字参数可以没有顺序
pet(name='呆呆哒',petType='hamster')
pet(petType='hamster',name='呆呆哒')
print('*'*20)

#定义一个参数的默认值,有默认值的参数应该放在函数的最后面
def pet(name,petType='hamster'):
    print(name,petType)
pet('呆呆哒')
print('*'*20)

#禁止函数修改列表
a=['a','b','c','d']
def test(af):
    af.pop()
    return af
print(a)
print(test(a[:]))#在这里创建一个副本
print(a)
print('*'*20)

#用*号传递任意数量的实参,如果还有其他确定数量的实参，其他确定数量的实参必须在*号实参的前面
#一个*号表示传递一个元组
def makePizza(*toppings):
    print(toppings)
makePizza('a')
makePizza('a','b','c')
print('*'*20)

#使用任意数量的关键字实参,两个*号表示传递一个字典
def buildProfile(first,last,**userInfo):
    proFile={}
    proFile['first_name']=first
    proFile['last_name']=last
    for key,value in userInfo.items():
        proFile[key]=value
    return proFile
userProfile=buildProfile('王','三',loc='guangzhou',dep='bumen')
print(userProfile)
print('*'*20)

#导入模块的时候给模块指定别名
import random as ra
print(ra.randint(1,3))
print('*'*20)

#导入模块中的函数的时候给函数重命名,使用过程中不需要按原来的写模块名.函数名的形式
from random import randint as rad
print(rad(1,3))
print('*'*20)

#导入模块中所有的函数
from random import *
print(randint(1,3))
print('*'*20)

