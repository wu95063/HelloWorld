#if 语句在编程中极其重要，
#它允许我们建立一些程序，
#这些程序能做出决定（在基于一些条件的情况下）。
#所以if condition,当条件为真的时候，我们会做一些事情；
#否则我们会做其他事情。
#forexample:
is_water=True
not_water=False
if not_water:#输入的变量不同，会得到不同的两个输出结果。
    print('You can drink that water. ')
else:
    print('You can\'t drink that water. ')
print('Enjoy your day.')
#Another example:利用if语句；
#如果天气热：就输出天气好热，多喝水啊。并说享受你的生活
#如果天气冷：就输出天气好冷，注意保暖，并说享受你的生活
#如果是不冷不热的天气，则说真是一个好天气。并说享受你的生活。
is_hot=False#通过在True和False之间转换会得到不同的输出。
is_cold=False
if is_cold:
    print('天气真冷，一定要注意保暖啊。')
elif is_hot:#elif,是else if的缩写，意思为：否则，如果。
    print('天气真热，一定要多喝水啊。')
else:
    print('今天的天气真好！')
print('祝你健康快乐每一天。')