# 打印出九行星号（*）
i = 1
while i <= 9:
    l = 1
    while l <= i:
        print("*", end="")
        l += 1
    i +=1
    print("")

# 打出九九乘法表
i = 1
while i <= 9:
    l = 1
    while l <= i:
        print("%d*%d" % (l,i), end="=")
        print(i*l, end="\t")
        l += 1
    i +=1
    print("")
