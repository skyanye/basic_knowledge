import re

"""
| 匹配多个分组
? 表明前面的分组是可选的，或者非贪心匹配
* 匹配0次或多次
+ 匹配1次或多次
{n} 匹配n次前面的分组
{n,} 匹配n次或更多前面的分组
{,m} 匹配0次到m次前面分组
{n,m} 匹配至少n次、至多m次前面的分组
{n,m}? 或*?或+?对前面的分组进行非贪心匹配
^spam 表示字符串必须以spam开始
spam$ 表示字符串必须以spam结束
[abc] 匹配方括号内的任意字符（比如a、b或c）
[^abc] 匹配不在方括号内的任意字符
. 表示只匹配一个字符
.* 表示所有文本
\d 0-9的任何数字
\D 除0-9的数字以外的任何字符
\w 任何字母、数字或下划线字符（可以认为是匹配单字字符）
\W 除字母、数字和下划线以外的任何字符
\s 空格、制表符或换行符（可以认为是匹配“空白”字符）
\S 除空格、制表符和换行符以外的任何字符
"""

#匹配一个内容
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found:'+mo.group())
print('1*'*20)

#分组匹配
phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')#这里是重点
mo=phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found:'+mo.group(1))
print('Phone number found:'+mo.group(0))#方法传入0或者不传入，将返回整个匹配的文本
print('Phone number found:',mo.groups())#一次性获取所有分组
print('2*'*20)

#程序中多数表示的非贪心匹配，用?号可以表示非贪心匹配
greedyHaRegex=re.compile(r'(Ha){3,5}')
mo1=greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
greedyHaRegex=re.compile(r'(Ha){3,5}?')
mo2=greedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
print('3*'*20)

#findall()方法返回一个列表
phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo=phoneNumRegex.findall('Cell: 415-555-4242,Work:212-555-0000')
print(mo)#要取得415这个数字，可以输入mo[0][0]
print('4*'*20)

#自定义字符分类，用方括号定义
vowelRegex=re.compile(r'[aeiouAEIOU]')#在[a的中间加上^即[^a，可以匹配方括号以外的字符
mo=vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)
print('5*'*20)

#^表示以这个符号后面的内容开始匹配
a=re.compile(r'^hello')
s1=a.findall('hello world')
s2=a.findall('no hello world')
print(s1,s2)#s2是没有匹配到内容的
print('6*'*20)

#$符号的应用
a=re.compile(r'hello$')
s1=a.findall('this is end with hello')
s2=a.findall('hello world is end with no')
print(s1,s2)#s2是没有匹配到内容的
print('7*'*20)

#.*?非贪心模式的区别
a=re.compile(r'<.*?>')#去掉问号会得到不同的结果
mo=a.search('<dfafd dfasdf>dfasdf>')
print(mo.group())
print('8*'*20)

#re.DOTALL作为第二参数，会匹配所所有的字符。不加这个为第二个参数，只匹配到换行符的位置
lineRegex=re.compile('.*',re.DOTALL)#去掉re.DOTALL后只匹配到\n前面的内容
mo=lineRegex.search('Serve the public trust.\nProtect the innocent')
print(mo.group())
print('9*'*20)

#re.IGNORECASE或re.I作为第二参数，表示不区分大小写
lineRegex=re.compile('robocop',re.I)
mo=lineRegex.search('Robocop is part man.')
print(mo.group())
print('10*'*20)

#sub()方法替换字符串，第一个参数为字符串，第二个参数匹配的内容
nameRegex=re.compile(r'Agent \w+')
mo=nameRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')#sub()返回值为替换完成的字符串
print(mo)
print('11*'*20)

#re.VERBOSE作为第二参数，表示忽略正则表达中的空白符和注释
phoneRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    #area code
    (\s|-|\.)?
    #separator
    \d{3}
    #first 3 digits
    (\s|-|\.)
    #separator
    \d{4}
    #last 4 digits
    (\s*(ext|x|ext.) \s*\d{2,5})?
    #extension
    )''',re.VERBOSE)
print('12*'*20)

#组合使用re.IGNORECASE、re.DOTALL和re.VERBOSE
someRegexValue=re.compile('foo',re.IGNORECASE|re.DOTALL|re.VERBOSE)
print('13*'*20)
