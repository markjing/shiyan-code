#!/usr/bin/env python3

# listbugtest.py 的作用很简单，就是计算一个列表（base）中所有数字和一个数字（value）的和，并输出。
def compute(base, value):
# 使用append()追加列表的值，所以会让testlist一直追加，所以计算结果都会依次累加，而实际情况是每次调用compute()只是计算本次的base+value的和
    base.append(value)
    result = sum(base)             #here is bug ,result is wrong!
    #result = sum(base) + value               #result is right!
    print(result)

# 预期输出的是：
# python3 /home/shiyanlou/listbugtest.py
# 75
# 85
# 95

# 但现在的程序输出的是：
#
# python3 /home/shiyanlou/listbugtest.py
# 75
# 100
# 135

# if __name__ == '__main__': 这一句相当于 C 语言的 main 函数，作为程序执行的入口
# 实际的作用是让这个程序 python3 listbugtest.py这样执行时可以执行到 if __name__ == '__main__': 这个代码块中的内容
# 当通过 import listbugtest 作为模块导入到其他代码文件时不会执行if __name__ == '__main__':中的内容
if __name__ == '__main__':
    testlist = [10, 20, 30]
    compute(testlist, 15)
    compute(testlist, 25)
    compute(testlist, 35)

