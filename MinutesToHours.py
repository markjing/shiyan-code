#!/usr/bin/env python3

import math
import sys
# 命令行参数<2，程序异常，退出程序
if len(sys.argv) < 2:
    print("Please enter a parameter.")
    sys.exit(1)

def hours(minutes):
    """
    用户通过命令行参数输入分钟数，函数进行转换成相应的小时数和分钟数，如下示例：
    python3 MinutesToHours.py 80
    输出：1 H, 20M
    :param minutes: 获取用户输入的分钟数
    :return: 返回转换后的小时数和分钟数
    """
    i = 60
    try:
        # 如果arg minutes不是整数，则输入异常信息，退出程序
        minutes = int(minutes)
    except ValueError:
        print("Please enter a positive integer.")
        sys.exit(1)
    
    if minutes < 0:
        try:
            # 这里使用raise自定义异常
            raise ValueError
        except ValueError:
            print('ValueError: Input number cannot be negative.')
            sys.exit(1)
    else:
        # 使用math模块的floor()方法取小于或者等于Hou的最大正整数，如果直接使用format()方法
        # format()方法遵循四舍五入，会使计算结果的精度失准；
        # print("{:.2f}".format(Hou))无法获取想要的结果
        Hou = math.floor(minutes / i)
        Min = minutes % i
        print("{} H, {} M".format(Hou, Min)) 
     
# __name == '__main__': 这一句相当于c语言的main函数，作为程序执行的入口
# 实际作用是让程序python3 MinutesToHours.py xx这样执行时可以执行__name__ == '__main__':中的代码块
# 而当程序作为模块导入到其它代码文件中时，则不会执行__name__ == '__main__':中的内容.
if __name__ == '__main__':
    hours(sys.argv[1])                     
