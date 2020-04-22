"""在控制台连续输入五行*，且每行星号依次递增
*
**
***
****
*****"""

i = "*"
x = 0
while x < 5:
    x += 1
    print("第%d行" % x)
    print(i * x)

# 在默认情况下，print函数输出内容之后会自动在内容末尾增加换行，如果不想换行的话则可以写成print("*", end=""),例如
print("*")
print("*")
print("*", end="")
print("*")  # 运行后会发现在写了end的print函数会与下一行共占一行并紧挨
# 如果在end=后的引号中填写字符，将会在下行与上行之间出现
print("*", end="123")
print("*")

i = 1
while i <= 5:
    l = 1
    while l <= i:
        print("*", end="")
        l += 1
    i += 1
    print("")
