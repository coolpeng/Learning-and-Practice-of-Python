
# coding=utf-8

print ("Hello World!")

# 1.0 注释

# 这是单行注释


'''
这是多行注释
'''

"""
这还是我另外一种多行注释
"""

print ("Hello Python3")


# 1.1 行与缩进

if True:
	print ("True")
else:
	print ("False")

# 1.2 数据类型

'''
python中数有四种类型：整数、长整数、浮点数和复数
整数， 如 1
长整数 是比较大的整数
浮点数 如 1.23、3E-2
复数 如 1 + 2j、 1.1 + 2.2j
'''

#1.3 字符串

word = "string"
sentence = "this is a sentence"
paragraph = """this is a paragraph,
to show the use of many lines."""
print (paragraph)

# 1.4 同一行显示多条语句
# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割

import sys; x = 'Edward'; sys.stdout.write(x + '\n')

#1.5 Print 输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""

x="m"
y="n"

print ("----换行----")
print (x)
print (y)

print ("----不换行----")

# print (x, end = "")
# print (y, end = "")


#1.6 import 与 from...import

'''
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''
# 导入 sys 模块
import sys
print ("===Python import mode===")
print ("命令行参数为：")
for x in sys.argv:
	print (x)
print ("\n python 路径为",sys.path)


# 导入 sys 模块的 argv, path 成员
from sys import argv,path # 导入特定成员

print ("===python from import===")
print ("path: ",path) # 因为已经导入path成员，所以此处引用时不需要加sys.path


print (max.__doc__)


