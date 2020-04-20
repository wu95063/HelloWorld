full_name=input('what is your name?  ')#获取用户输入信息，并将用户信息返回给full_name变量，full_name这个变量的类型是字符串
print(full_name)#输出变量full_name
print('Hello '+full_name)#字符串和字符串可以进行拼接，公式：字符串+字符串=字符串
print(full_name*10)#公式：字符串*整数=字符串
print(full_name+str('00'))#字符串
birth_year=input('Please input your birth year:  ')#获取用户输入信息，并将用户信息返回给bitth_year变量，birth_year这个变量的类型是字符串
age=2020-int(birth_year)#定义一个新的变量，调用int函数将birth_year这个字符串类型转换成整数型。
print(age)#输出age这个变量，age这个变量为整数型
print(f'Your age is {age}')#由于age这个变量是整数型，而your age is 是字符串，如果想要把二者直接进行拼接是无法达到的。所以我们调用format函数，↓↓
                           #来格式化字符串，format函数即为格式化的意思。
                           #利用大括号{},age的类型是整数型，{age}={整数型}=字符串型，'your age is {age}'即为'字符串 字符串 字符串 字符串'，进而输出这些字符串。
