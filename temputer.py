#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：temputer.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/14 17:31 
"""


def c_to_f(t):
    f = (t * 9 / 5) + 32
    return f


def f_to_c(t):
    c = (t - 32) * 5 / 9
    return c


if __name__ == '__main__':
    c = 30
    f = c_to_f(c)
    print(f"{c}摄氏度 = {f}华氏度")


    f = 86
    c = f_to_c(f)
    print(f"{f}华氏度 = {c}摄氏度")
