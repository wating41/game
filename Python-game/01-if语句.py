import datetime
# if True :
#     print('hello')

a = '赢'
if False:
    print('你猜 1')
else:
    print('你猜 2')

print('你确认是 %s' % a)

b = 'low'
c = ''
d = '98'

# 在命令行让用户输入一个用户名，获取用户输入，并进行判断
# 如果用户输入的用户名是admin，则显示欢迎管理员光临
# 如果用户输入的是其他的用户名，则什么也不做
name = input('请输入用户名：')

if name == 'admin':
    print('欢迎管理员 %s' % name)
else:
    print('您好！！！欢迎 %s 登录' % name)

# 让用户在控制台中输入一个年龄
# age = int(input('请输入你的年龄：'))

# 如果用户的年龄大于18岁，则显示你已经成年了

age = input('请输入你的年龄：')
# Year = datetime.date.strftime(datetime.date(), '%Y - %m - % d')
nameid = input('请输入你的生日：')
if age >= 18 :
    print('恭喜你已经成年，可以喝酒！！')
else :
    print('您还未成年！！')

# print(Year)


