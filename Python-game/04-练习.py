# 练习3：
#     我家的狗5岁了，5岁的狗相当于多大年龄的人呢？
#     其实非常简单，狗的前两年每一年相当于人类的10.5岁，然后每增加一年就增加四岁。
#     那么5岁的狗相等于人类的年龄就应该是10.5+10.5+4+4+4 = 33岁

#     编写一个程序，获取用户输入的狗的年龄，然后通过程序显示其相当于人类的年龄。

DagAge = int(input('请输入狗的年龄：'))
age = DagAge * 10.5
if DagAge > 0:
    if DagAge == 2 :
        age = DagAge * 10.5

    else :
        age = 2 * 10.5
        print(age)
        age += (DagAge - 2) * 4
        print('您狗狗的年级相当于人类年级：%s岁' % age)

    print('您狗狗的年级相当于人类年级：%s岁' % age)
else:
    print('输入年龄有误：%s,请输入正确的年龄' % DagAge)
