#-*- coding:utf-8 -*-
#!python3
#定位位置
import webbrowser,sys,pyperclip
if len(sys.argv)>1:
    address=' '.capitalizejoin(sys.argv[1:])
else:
    address=pyperclip.paste()
webbrowser.open('http://www.google.com/maps/place/'+address)
print('1*'*20)

#用requests从web下载文件
import requests
#用requests.get()下载一个网页
#status_code属性返回状态
res=requests.get('http://www.sina.com.cn')
print(res.status_code)
print('2*'*20)

#raise_for_status()方法下载错误会异常，下载正确什么也不做

#iter_content()方法循环返回一段内容，都是bytes类型，可以指定包含字节数

#用beautifulsoup处理html
import bs4
content=bs4.BeautifulSoup(res.text,"html.parser")
print('3*'*20)

#sellect()方法的选择器
'''
soup.select('div')所有名为<div>的元素
soup.select('#author')带有id属性为author的元素
soup.select('.notice')所有使用CSS class属性名为notice的元素
soup.select('div span')所有在<div>元素之内的<span>元素
soup.select('div>span')所有直接在<div>元素之内的<span>元素，中间没有其他元素
soup.select('input[name]')所有名为<input>，并有一个name属性，其值无所谓的元素
soup.select('input[type="button"]')所有名为<input>并有一个type属性，其值为button的元素
'''
#getText()方法可以取得内容
elem=content.select('p')
str(elem[0])
print(elem[0].getText())
print('4*'*20)
