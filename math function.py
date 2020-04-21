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
import math
print(math.pi)#圆周率pi
print(math.e)#自然常数e
print(math.degrees(6.28))#弧度转度
print(math.radians(180))#度转弧度
print(math.exp(2))#=print(math.e**2)
print(math.expm1(2))#print(math.exp(2)-1)
print(math.log(math.e))#print(math.log(math.e,math.e))
print(math.log(8,2))#以2为底8的对数。
print(math.log10(100))#=print(math.log(100,10))
print(math.log1p(math.e-1))#=print(math.log((math.e-1)+1,math.e))
print(math.pow(2,3))#2**3
print(math.pow(3,2))#3**2
print(math.sqrt(4))#4的开方
print(math.sqrt(16))#16的开方
print(math.trunc(5.6))#取整数
print(math.trunc(4.2))#取整数
print(math.modf(5.8))#返回x的小数和整数
print(math.modf(3.0))#返回x的小数和整数
print(math.modf(3.1))#返回x的小数和整数
print(math.fabs(-2.9))#取绝对值
print(math.fmod(5,2))#返回x%y（取余）
print(math.fsum([1,2,3]))#返回无损精度的和
print(math.fsum([0.1,0.2,0.3]))
print(math.factorial(4))#返回x的阶乘
print(math.factorial(10))
float("inf") # 正无穷
float("-inf") # 负无穷
float('nan')#not a number.
float('inf')*0#not a number
print(math.isinf(float('inf')))#返回bool类型。
print(math.isinf(float('-inf')))
print(math.isinf(10))
print(math.isnan(float('inf')))
print(math.isnan(10))
print(math.isnan(float('inf')*0))
print(math.isnan(float('nan')))
print(math.isnan(float('inf'))/math.isnan(float('nan')))#???不知道为什么输出0.0？
print(math.hypot(3,4))#勾股定理。
print(math.copysign(5,-2))# 若y<0，返回-1乘以x的绝对值；
                            #否则，返回x的绝对值
print(math.copysign(5,2))
print(math.copysign(-5,-2))
print(math.copysign(-5,2))
print(math.frexp(0))#返回m和i，满足m乘以2的i次方
print(math.frexp(3))#返回m和i，满足m乘以2的i次方
print(math.ldexp(0.75,2))#返回m乘以2的i次方
print(math.sin(math.radians(30)))#-->0.499999999998
print(math.sin(math.radians(90)))#-->1.0
print(math.sin(math.radians(0)))#-->0
print(math.sin(math.pi))#-->1.2246467991473532e-16=1.2*10的-12次幂。
#未完待续......












