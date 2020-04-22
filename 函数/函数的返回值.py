def sum_2_number(num1,num2):
    result = num1+num2
    return  result
# return表示返回（这个返回就是告诉你你所执行的结果，不是返回上去），下方的代码不会被执行到
num1 = int(input("请输入您要计算的第一个数值"))
num2 = int(input("请输入您要计算的第二个数值"))
sum_result = sum_2_number(num1,num2)
print("计算结果：%d+%d=%d"% ( num1,num2,sum_result))
print('000')