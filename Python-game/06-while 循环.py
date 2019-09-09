# 求100以内所有的奇数之和
# i = 0
# result = 0
# while i < 100:
#     i += 1
#     if i % 2 != 0 :
#         print(i)
#         result += i
# else:
#     # result += i
#     print('100内奇数之和: %2f' % result)

# 求100以内所有7的倍数之和，以及个数
# i = 0
# result = 0
# while i < 100 :
#     i += 1
#     if i % 7 == 0:
#         print(i)
#         result += i
#
# else:
#     print('100以内所有7的倍数之和 :%s' % result)

# # 方法二
# i = 7
# result = 0
# while i < 100:
#
#     if i % 7 == 0:
#         result += i
#         i += 7
#     # print(i)
#
# print('100以内所有7的倍数之和 :%s' % result)
# 求100以内所有7的倍数之和，以及个数
# i = 7
# # 创建一个变量，来保存结果
# result = 0
# # 创建一个计数器，用来记录循环执行的次数
# # 计数器就是一个变量，专门用来记录次数的变量
# count = 0
# while i < 100:
#     # 为计数器加1
#     count += 1
#     result += i
#     i += 7
#
# print('总和为：',result,'总数量为:',count)


# 水仙花数是指一个 n 位数（n≥3 ），它的每个位上的数字的 n 次幂之和等于它本身（例如：1**3 + 5**3 + 3**3 = 153）。
# 求1000以内所有的水仙花数

# i = 100
# while i < 1000:
#     a = i // 100
#     b = (i - 100 * a) // 10
#     c = i % 10
#     if a ** 3 + b ** 3 + c ** 3 == i:
#         print(i)
#     i += 1

# 获取用户输入的任意数，判断其是否是质数。
a = int(input('请输入任意整数：'))

# 判断num是否是质数，只能被1和它自身整除的数就是质数
i = 2
flg = True
while i < a:
    if a % i == 0:
        flg = False
        # pass
    i += 1
if flg:
    print(i,'是质数')
else:
    print(i,'不是质数')
# 获取到所有的可能整除num的整数
# 创建一个变量，用来记录num是否是质数，默认认为num是质数