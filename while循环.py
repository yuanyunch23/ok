# 打印 5遍 hello，python
print("hello,python " * 5)
# while 循环函数是为了重复执行一个程序，直到满足一个条件后才会停止
# 不要忘了while中的计数器，否则就会无限循环，同时不要忘记条件后的英文的冒号
# 定义一个整数变量，记录循环次数
i = 0

# 开始循环
while i < 5:
    # 希望在循环内执行的代码
    print("hello,python")

    # 处理计数器
    i += 1
    print("i=%d" % i)
# 计算0--100之间所有数字的累计求和
result = 0
i = 0
while i < 100:
    i += 1
    result += i
print("0-100之间的整数计数和为%d" % result)


result = 0
i = 0
while i <= 100:
    result += i
    i += 1
print("0-100之间的整数计数和为%d" % result)


# 计算0-100之间所有的偶数整数的累计求和
result = 0
i = 0
while i < 100:
    i += 2
    result += i
print("0-100之间的偶数整数计数和为%d" % result)


result = 0
i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        result += i
print("0-100之间的偶数整数计数和为%d" % result)


# 0--100所有奇数整数的求和

result = 0
i = 0
while i < 100:
    i += 1
    if i % 2 != 0:
        result += i
print("0-100,之间所有奇数的整数计数和为%d" % result)
