#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：average.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/27 15:24 
"""


def avg(num_list):
    sum_num = 0
    for num in num_list:
        sum_num += num
    return sum_num / len(num_list)


numbers = [1, 2, 3, 7, 8, 11, 100, 21]
print(avg(numbers))
