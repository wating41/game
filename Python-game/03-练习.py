# 练习1：
#     编写一个程序，获取一个用户输入的整数。然后通过程序显示这个数是奇数还是偶数。
num = int(input('请输入一个随机整数：'))
# 获取用户输入的整数

# # 显示num是奇数还是偶数
if num % 2 == 0:
    print(num, '是整数')
else:
    print(num, '不是整数')

# 练习2：
#     编写一个程序，检查任意一个年份是否是闰年。
#     如果一个年份可以被4整除不能被100整除，或者可以被400整除，这个年份就是闰年

# # 检查这个年份是否是闰年
year = int(input('请输入一个年份：'))

if (year % 4 == 0 and (year % 100) != 0) or \
        (year % 400 == 0):
    print('%s 该年份是闰年' % year)
else:
    print('%s 该年份不是闰年' % year)

