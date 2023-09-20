#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：calc.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/19 14:27 
"""


def spr(s):
    book = {'+': 1, '-': 2, '*': 3, '/': 4}
    flag = 1
    a = 0
    b = 0
    for t in s:
        if t in ['+', '-', '*', '/']:
            flag = 2
            c = book[t]
        else:
            if flag == 1:
                a = a * 10 + int(t)
            else:
                b = b * 10 + int(t)
    return [a, b, c]


def calc(li):
    if li[2] == 1:
        print(li[0] + li[1])
    elif li[2] == 2:
        print(li[0] - li[1])
    elif li[2] == 3:
        print(li[0] * li[1])
    elif li[2] == 4:
        if li[1] == 0:
            print("除数不能为0")
        else:
            print(li[0] / li[1])


if __name__ == "__main__":
    flag = 1
    while (flag):
        st = input("请输入")
        calc(spr(st))
        flag = int(input("如果要退出请输出0,继续请输入1"))
