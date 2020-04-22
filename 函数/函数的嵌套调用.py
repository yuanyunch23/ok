def test1():
    print("*" * int(input("请输入您想打印出*的数量")))
    print("+" * int(input('请输出您想打印出+的数量')))
def test2():
    print("-"*int(input('请输出您想打印出的-号数量')))
    test1()
test2()

def print_line(char,times):
    print(char*times)
    times =int(input())
print_line("-")