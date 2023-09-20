#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：fibonacci.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/5 22:44 
"""


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
        return sequence


if __name__ == '__main__':
    res = fibonacci(9)
    print(res)
