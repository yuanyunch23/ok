# 注意，定义好函数之后，只表示封装好一段代码
# 如果不主动调动函数，函数是不会主动执行的
# def表示定义一个函数，定义的函数内容包括从def下一行前方空四个格的内容
# 定义的函数只能放在调用函数上方，不能放在下方
def say_hello():
    i = 1
    while i <= 5:
        s = 1
        while s <= i:
            print("hello", end=" ")
            s += 1
        i += 1
        print("")

say_hello()