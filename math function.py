a=3.14
round(a)#圆函数可以对数字进行四舍五入。
print(round(a))#-->3
b=-1.8
abs(b)#绝对值函数总是输出positive value.
print(abs(b))
print(abs(-0.8))
#在python中我们有一些内置函数来执行数学计算，
#如果你想写一个涉及复杂数学运算的程序，你就需要导入数学模块。
#python中的模块是一个单独的文件(seperate file)，这些单独的文件具有一些可以反复使用的的代码。我们使用这些模块，
#将我们的代码组织成不同的文件。
import math#调用数学模块
print(math.ceil(3.5))#向上取整函数。
print(math.floor(3.5))#向下取整函数
print(round(3.5))#圆函数，四舍五入。
#谁说的我忘了：It's not what we do once in a while that shapes our lives. It's what we do consistently.
