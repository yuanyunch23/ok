def text(x):
    if x > 10000:
        return
        print("test_return") # 这一行代码永远不会运行
    elif x > 1000:
        return 100
    elif x > 100:
        return 10
    elif x > 10:
        return 1
    else:
        return 0

print(text(int(input("请输入您要输入的值"))))
