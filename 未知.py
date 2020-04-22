import random

secret = random.randint(1, 10000)


def int_input(promt=''):
    while True:
        try:
            res = int(input(promt))
            break
        except ValueError:
            print('类型错误,请重新输入')
    return res


count = 15
num = int_input('猜一个一到一万的数,您有{}次机会,请输入：'.format(count))
i = 0
flag = 1
while num != secret:
    if num > secret:
        print('数字大了')
    else:
        print('数字小了')
    i = i + 1
    if i == count:
        flag = 0
        print('次数用完，游戏结束')
        break
    j = str(15 - i)
    num = int_input('还有' + j + '次机会,请重新输入')
if flag == 1:
    print("恭喜你，游戏通关")