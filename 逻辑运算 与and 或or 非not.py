# and连接的是两个不相同但不冲突的条件，如果是两个冲突条件就会运行else命令，必须同时满足两个条件才可以
"""定义一个整数变量 age. 编写代码判断年龄是否正确要求年龄在0——120岁之间"""
age = int(input("请输入你的年龄"))

if age >= 0 and age <= 120:
    print("年龄正确")
else:
    print("年龄错误")
# or连接的是两个条件，只要满足其中任何一个便可以
""""定义两个整数变量 python_score、c_score
要求只要有一门成绩>=60便及格。"""
python_score = int(input("请输入你的成绩"))
c_score = int(input("请输入你的成绩"))
if python_score >=60 or c_score >= 60:
    print("恭喜你，你及格了")
else:
    print("你完了，去从新补考去吧")
# not在开发中，通常希望某个条件不满足时，执行一些代码，可以用not
# 除此之外，如果需要拼接复杂的逻辑计算条件，同样也有可能使用到not
""""定义一个布尔型变量 is_employee,编写代码判断是否为本公司的员工"""
# 在编程中“=”的意义是赋值，如果想用等于号，必须两个等于号连起来“==”
# 同时如果想用不等号“≠”，可以用叹号与等号相连表示不等号“!=”，注意，这里的叹号是英文状态下的叹号!
number = int(input("输入公司密码"))
if number == 123456:
    is_employee = True
else:
    is_employee = False

if not is_employee:
    print("非公司人员不得入内")
else:
    print("快点进去，迟到罚钱")



