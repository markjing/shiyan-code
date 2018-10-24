#!/usr/bin/env python3
###
# 导入sys模块
# 在这个文件中，我们需要实现以下需求：

# 执行程序可以输入多个命令行参数
# 每个命令行参数中间都有一个冒号，需要使用字符串的 split() 进行切分并存储到字典中
# 按照示例的格式要求输出重新处理后的数据
import sys
output_dict = {}

# handle_data() 用来处理参数并将处理的结果存入到 output_dict
def handle_data(arguments):
    data = arguments
    key = data.split(':', 1)[0]
    value = data.split(":", 1)[1]
    output_dict[key] = value

# print_data() 用来按照格式打印输出。
def print_data(key1, value1):
    print("ID:{}".format(key1), "Name:{}".format(value1))

# if __name__ == '__main__': 这一句相当于 C 语言的 main 函数，作为程序执行的入口
# 实际的作用是让这个程序 python3 dicttest.py arg arg1...这样执行时可以执行到 if __name__ == '__main__': 这个代码块中的内容
# 当通过 import dicttest 作为模块导入到其他代码文件时不会执行if __name__ == '__main__':中的内容。

if __name__ == '__main__':

    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in output_dict:
        print_data(key, output_dict[key])
