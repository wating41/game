# 练习 创建一个变量保存你的名字，然后通过四种格式化字符串的方式
#   在命令行中显示，欢迎 xxx 光临！

a = '驴得水'

# 拼接
print('欢迎' + a + '光临')
# 多个参数
print('欢迎', a, '光临')
# 占位符
print('欢迎 %s 光临！！' % a)
# 格式化字符串
print(f'欢迎 {a} 光临')
print(F'welcome {a} to beijing')

# 布尔值
a = True
print('a = %s' % a)

print('hello') if False else print('ok')

# 练习：
#   现在有a b c三个变量，三个变量中分别保存有三个数值，
#       请通过条件运算符获取三个值中的最大值

a = 100
b = 900
c: int = 90

max = c if c > (a if a > b else b) else (a if a > b else b)
print(max)

max = a if a > b and a > c else b if b > c else c
print(max)