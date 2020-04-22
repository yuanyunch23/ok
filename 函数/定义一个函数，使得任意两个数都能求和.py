def sum_2_number():
    l = (int(input("请输入第一个数")))
    print(l)
    s = (int(input("请输入第二个数")))
    print(s)
    print("%d+%d=%d" % (l, s, l+s))
sum_2_number()

#如果想在定义的函数内部创建一个参数，可以把要创建的参数放入def后的函数名之后的括号里
# 如果想创建多个参数，则要用“,”隔开，逗号是英文版的，而在以后如果想使用定义的参数，可以在调用函数时，在后面括号中输入参数名
# 定义函数时输入的参数叫做形参，而调动函数时输入的参数叫做实参
def sum_2_number2(number1 , number2):

    result=number1 +number2
    print("%d+%d=%d" %(number1,number2,result) )
sum_2_number2(130,40)

