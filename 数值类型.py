# bool是表示数字类型的，True代表1，False代表0，可以直接进行数值运算
i = 10
t = 10.5
b = True
f = False
print(i + b)
print(i + f)
# 字符串之间是可以用+来生成一个新的字符串，例如：
name = "小明"
name1 = "小红"
print(name + name1)
# 字符串与数值除了乘法之外，再不能进行任何其他计算
print(name + name1 * 10)
print((name1 + name) * 10)
print(name + name1+"10")
