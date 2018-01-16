#!python3
#-*- coding:utf-8 -*-
#被测试的代码
def get_formatted_name(first,last):
    full_name=first+' ' +last
    return full_name.title()

#测试上面的函数
import unittest
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name=get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
unittest.main()

#unittest中的断言方法
try:
    assertEqual(a,b)#核实a==b
    assertNotEqul(a,b)#核实a!=b
    assertTrue(x)#核实x为True
    assertFalse(x)#核实x为Flase
    assertIn(item,list)#核实item在list中
    assertNotIn(item,list)#核实item不在list中
except:
    print('断言方法，无显示内容')

#setUp()方法
