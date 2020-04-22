# if嵌套是存在逐级关系的
"""上车流程，先检查是否有票，后检查是否携带管制刀具，易燃易爆物"""
ticket = input("是否有票")
if ticket == "有" or "是":
    print("请进行安检")
    safety_check = input("是否携带管制刀具，易燃易爆物")
    if safety_check == "是" or '有':
        knife_length = int(input("请输入你刀的长度"))
        if knife_length >= 30:
            print("请把危险物品掏出并双手抱头")
        else:
            print("请上车，并把您%dcm的刀具收好，旅途愉快" % knife_length)
    else:
        print("请上车，旅途愉快")
else:
    print('请先去买票')
