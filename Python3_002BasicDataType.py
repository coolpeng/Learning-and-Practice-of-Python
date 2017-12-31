# coding=utf-8

print ("Python3 基本数据类型")

'''
ython 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值
'''

counter = 100 # 整型变量
weight = 75.1 # 浮点型变量
name = "Edward" # 字符串

print (counter)
print (weight)
print (name)

# 1. 多个变量赋值
# 创建一个整型对象，值为1，三个变量被分配到相同的内存空间上
a = b = c = 1

# 为多个对象指定多个变量
#两个整型对象 1 和 2 的分配给变量 x 和 y，字符串对象 "Edward" 分配给变量 c
x, y, z = 3, 4, "Edward"

# 2. 标准数据类型
'''
Python3 中有六个标准的数据类型：
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictionary（字典）
'''

# 2.1 Number（数字）
# Python3 支持 int、float、bool、complex（复数）
a, b, c, d = 10, 3.5, True, 4+2j

# 内置的 type() 函数可以用来查询变量所指的对象类型
print (type(a), type(b), type(c), type(d))

# isinstance
m = 100

if isinstance(m, int):
	print ("m is a int")
else:
	print ("m isn't a int");

# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型

# 数值运算

'''
1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
4、在混合计算时，Python会把整型转换成为浮点数。
'''

a = 1 + 2
b = 4.5 - 2
c = 3 * 8
d = 2 / 4 
e = 13 % 4 # 取余
f = 2 ** 4 # 乘方

print (a,b,c,d,e,f)







