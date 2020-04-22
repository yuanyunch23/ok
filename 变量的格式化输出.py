# %s表示字符串
# 定义字符串变量 name 输出 我的名字叫 小明，请多多关照!
name = "小明"
print("我的名字叫%s，请多多关照!" % name)
""" %d表示十进制的整数，%06d其中的6表示整数最小位数，如果不够会以0补齐，如果位数大于6位则会全部显示
# 而%60d则表示输出的数字占得总宽度，而%d60则代表输出的数字后的数字 注：6这个数字可以换，换几就代表几"""
# 定义整数变量 student_no，输出 我的学号是000001
student_no = 1
print("我的学号是%06d" % student_no)
print("我的学号是%60d" % student_no)
print("我的学号是%d60" % student_no)
print("我的学号是%06d60" % student_no)
print("我的学号是%6d60" % student_no)
# %f表示浮数点，但后面会有6位小数，如果不够6位会用0补齐，如果想控制几位小数就改成%._f,例如像改为两位小数，就改为%.2f,如果在f前加数字，则代表总共占得字符宽度=空格数+小数点+小数位数
# 定义小数 price' weight' money,输出 苹果单价9.00元/斤，购买了5.00斤，需要支付45.00元
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价%f元/斤，购买了%f斤，需要支付%f元" % (price, weight, money))
print("苹果单价%.2f元/斤，购买了%.2f斤，需要支付%.2f元" % (price, weight, money))
print("苹果单价%20.2f元/斤，购买了%40.2f斤，需要支付%60.2f元" % (price, weight, money))
print("苹果单价%.2f元/斤，购买了%.2f斤，需要支付%20f元" % (price, weight, money))
# 定义一个小数 scale，输出 数据比例是10.00%,如果数值相差10的倍数，则要在"%后的定义名加上括号并乘以相应的倍数，如果不加括号则会。。。
scale = 0.25
print("数据比例是%.2f%%"%scale*100)
print("数据比例是%.2f%%"%(scale*100))

