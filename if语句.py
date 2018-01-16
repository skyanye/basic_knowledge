#!python3
#-*- coding:utf-8 -*-

#检查是否相等时区分大小写
car='Audi'
print(car=='audi')

#in和not in关键字
name=[value*3 for value in range(1,10)]
if 3 in name:
    print('3 在name里面')

#检查name2的值是不是在name1里
name1=[value for value in range(1,10)]
name2=[value*2 for value in range(1,10)]
print(name1,name2)
for i in name2:
    if i in name1:
        print(str(i)+'在里面')
    else:
        print(str(i)+'不在')
