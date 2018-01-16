#!python3
#-*- coding:utf-8 -*-

#创建一个类
class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.color='black' #默认的值，初始方法中不用这个参数
    def sit(self):
        print(self.name+' sit down')
    def rollOver(self):
        print(self.name+' roll over')
    def showColor(self):
        print(self.color)

#创建实例
myDog=Dog('papi',2)
print(myDog.name,myDog.age)
print('*'*20)

#调用方法
print(myDog.sit(),myDog.rollOver())
print('*'*20)

#调用默认值
print(myDog.color)
print('*'*20)

#通过方法调用默认值
print(myDog.showColor())
print('*'*20)

#继承
class littleDog(Dog):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.disable='no' #给子类新的属性
myLittleDog=littleDog('f',1)
print(myLittleDog.name,myLittleDog.age,myLittleDog.disable)
print(myLittleDog.sit())
print('*'*20)

#重写父类的方法
class littleDog(Dog):
    def __init__(self,name,age):
        super().__init__(name,age)
    def sit(self):#self不能省
        print(self.name+' do not sit dow')
myLD=littleDog('sa',3)
print(myLD.sit())
print('*'*20)

#编码风格：类名一般都每个字母大写
