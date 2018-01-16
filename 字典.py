#!python3
#-*- coding:utf-8 -*-

#在字典中增加键值对
a={'a':1,'b':2}
print(a)
a['c']=3
print(a)
print('1*'*20)

#修改字典中的值
a['c']=4
print(a)
print('2*'*20)

#删除键值对
del a['c']
print(a)
print('3*'*20)

#字典的另外一种书写形式
a={
    'a':1,
    'b':2,   #最后一行后面要加,号
    }
print(a)
print('4*'*20)

#遍历键值对
for key,value in a.items():
    print(key,end=' ')
    print(value)
print('5*'*20)

#遍历字典中所有的键
for key in a.keys():
    print(key)
print('6*'*20)

#按顺序遍历字典中的所有键
for key in sorted(a.keys()):
    print(key)
print('7*'*20)
 
#遍历字典中所有的值
for value in a.values():
    print(value)
print('8*'*20)

#set()遍历字典中值的时候可以剔除重复的
a['c']=1
print(a)
for value in set(a.values()):
    print(value)
print('9*'*20)

#get()检查该键是否存在于字典中
print(a.get('e'))
print('10*'*20)

#setdefault(a,b)第一个参数a是要检查的值，第二参数b是没有时设置为默认值
a.setdefault('e',3)
print(a)
print('11*'*20)

#字典列表
aliens=[]
for i in range(1,10):
    newAlien={'color':'green','speed':'slow','point':5}
    aliens.append(newAlien)
print(aliens)
print('12*'*20)

#字典中存储列表，并遍历
favoriteLanguages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
    }
for key,values in favoriteLanguages.items():
    print(key+':')
    for value in values:
        print(value,end=' ')
    print('\n')
print('13*'*20)

#字典中存储字典
users={
    'user1':{
        'name':'jen',
        'password':'123',
        },
    'user2':{
        'name':'phil',
        'password':'456',
        },
    }
for key,values in users.items():
    print(key)
    print(values['name'],values['password'])
for key,values in users.items():
    print(key)
    for key1,value in values.items():
        print(key1,value)
print('14*'*20)
