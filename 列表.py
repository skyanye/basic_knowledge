#!python3
#-*- coding:utf-8 -*-

#列表索引可以写成负数，表示从最后一个开始
name=['a','b','c','d','e']
print(name)
print(name[-1])
print(name[-2])
print('1*'*10)

#列表也可以用字符串的一些方法
print(name[0].upper())
print('2*'*10)

#在列表中添加元素
name.append('f')
print(name)
print('3*'*10)

#在列表中插入元素
name.insert(0,'a1')#第一个参数为0，表示在第0位插入
print(name)
print('4*'*10)

#在列表中删除元素
del name[0]
print(name)
print('5*'*10)

#如果删除后还需要使用这个值，那么可以用pop()方法
popName=name.pop()#默认弹出最后一个值
print(name)
print(popName)
print(name.pop(0))#pop()可以有一个参数，位于列表中的位置
print(name)
print('6*'*10)

#remove()删除列表中的值，但不知道该值在列表中的位置
name.remove('d')
name.append('a')
name.append('d')
name.append('a')
print(name)
name.remove('a')#remove()方法只删除出现的第一个值
print(name)
print('7*'*10)

#sort()方法，永久性的排序
name.sort()
print(name)
name.sort(reverse=True)#反向排序
print(name)
print('8*'*10)

#sorted()函数，临时排序
name=['a','c','b','e','d']
print(name)
print(sorted(name))#sorted()这是个函数
print(name)
print(sorted(name,reverse=True))
print('9*'*10)

#reverse()永久反转元素，但不是按字母表顺序，只是将前后反转
print(name)
name.reverse()
print(name)
print('10*'*10)

#列表长度
print(len(name))
print('11*'*10)

#注意，第一个for循环的是列表，第二个for循环的是脚标
for i in name:
    print(i)
for i in range(0,len(name)):#int类型不能迭代，需要迭代要加range()
    print(name[i])
print('12*'*10)

#利用range()创建数字列表，可以用list()创建一个列表,
numbers=list(range(1,5))#range()的第二个参数是指到第几个数字(不包含这个数字），而不是指一共几个数字
print(numbers)
numbers=list(range(1,6,2))#可以设置步长，第三个参数是步长
print(numbers)
print('13*'*10)

#举例列表,得到一个平方数的列表
#方法一
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
    print(squares)
#方法二，优先推荐这个，比方法一好
squares=[]
for value in range(1,11):
    squares.append(value**2)
    print(squares)
print('14*'*10)

#最大值，最小值，总和
print(min(squares))
print(max(squares))
print(sum(squares))
print('15*'*10)

#列表解析
squares=[value*3 for value in range(1,10)]
print(squares)
print('16*'*10)

#切片
print(name)
print(name[1:4])#1和4分别为起始索引和最终索引,当达到4索引位置时终止
print(name[-3:])#从-3位置开始切到最后
print('17*'*10)

#复制列表
name1=name[:]#这里不能用name1=name，name1=name表示的是一个引用
name1.append('1')
print(name1)
print(name)
