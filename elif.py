# elif是可以在if条件之外再增加一些条件，条件不同，执行的代码也是不同的，如果要添加几个条件就用几个elif，与if一样，条件后要加冒号
# elif的条件是与if是平级关系，if的条件并不能影响elif
# elif是不可以单独使用的，都必须和if联合使用，else也是一样的。
age = int(input("输入你的年龄"))
if age >= 80 and age <= 90:
    print("今晚早点睡")
elif age >= 70 and age < 80:
    print("今晚早点休息")
elif age >= 30 and age <= 40:
    print("今晚熬夜加班")
else:
    print("今晚甭想睡了")
"""1.定义holiday_name的字符串变量记录节日名称
2.如果是 情人节，应该 买玫瑰/看电影
3.如果是 平安夜，应该 买苹果/吃大餐
4.如果是 生日，应该 买蛋糕
5.其他节日送包包"""
holiday_name = input("今天什么节日")
if holiday_name == "情人节":
    print("买玫瑰/看电影")
elif holiday_name == "平安夜":
    print("买苹果/吃大餐")
elif holiday_name == "生日":
    print("买蛋糕")
else:
    print("买包包，记住一句话：包治百病")
