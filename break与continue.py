# break关键字是在程序执行过程中，如果满足了某个条件，就会退出循环，不再执行后续的重复代码,具体可以看下面例子
# continue关键字是在某一条件满足后，不执行后续重复的代码

# 不加break
i = 0
while i < 10:
    i += 1
print(i)

# 加break
i = 0
while i < 10:
    i += 1
    if i == 5:
        break
print(i)

# 不加continue
i = 0
while i < 5:
    i += 1
print(i)

# 加continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        # 注意在循环如要使用continue关键词时，确保循环中的计数器已经发生修改，否则将会产生死循环
        i += 2
        continue
    print(i)
print(i)








