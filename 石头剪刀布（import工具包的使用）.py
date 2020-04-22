""""1.输入要出的拳---石头（1）/剪刀（2）/布（3）
2.电脑随机出拳---先假定电脑只会出石头，完成整体代码功能
3.比较胜负"""
# 导入工具包的函数是import 而random代表的是产生一个随机整数，如果要取一个范围，则要在random后加（_, _）例如random(1, 10)表示的是在1--10之间任意产生一个整数
# 注：产生的数字是包括1和10的，且前面的数字是必须小于后面的数字的
import random
player = int(input("请输入您要出的拳 石头（1）/剪刀（2）/布（3）"))
computer: int = int(random.randint(1, 3))
print("玩家要出的拳是：%d-电脑出的拳是%d" % (player, computer))
"""比赛胜负
   1.石头胜剪刀
   2.剪刀胜布
   3.布胜石头"""
# 如果输入的代码过长的话可以在开头函数后加一个小括号和在结尾加一个小括号，然后可以在代码中间回车，会另起一行
# 如果不加小括号，便会在回车前自动增加一个'\'以保持代码的连续性
if((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("恭喜玩家胜利，奖励作业一本")
elif player == computer:
    print("平局，再来一局吧")
else:
    print("电脑胜利，惩罚玩家作业一本")
