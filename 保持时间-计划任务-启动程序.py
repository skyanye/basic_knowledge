#python3
#-*- coding:utf-8 -*-
import time

#UTC时间
print(time.time())
print('1*'*20)
#应用示例
def calcProd():
    #calculate the product of first 100,000 numbers.
    product=1
    for i in range(1,100000):
        product *=i
    return product

startTime=time.time()
prod=calcProd()
endTime=time.time()
print("The result is %s digits long."%len(str(prod)))
print("Took %s seconds to calculate."%(endTime-startTime))
print("2*"*20)
#以上示例中time.time()可用cProfile.run()

#time.sleep()暂停程序
for i in range(3):
    print("Tick")
    time.sleep(1)
    print("Tock")
    time.sleep(1)
print("3*"*20)
#time.sleep()不会被ctrl-c中断，必须等到暂停结束再中断，要绕过这个问题，不要用一次time.sleep(30),而是使用for循环执行30次time.sleep(1)

#四舍五入用round()函数
now=time.time()
print(now)
print(round(now,2))
print("4*"*20)
