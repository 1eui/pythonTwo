#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：missing_numbers.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/27 15:20 
"""


def find_miss_number(tup):
    tag_list = []
    for _ in range(len(tup) + 1):
        tag_list.append(0)
    for item in tup:
        tag_list[item - 1] = 1
    return tag_list.index(0) + 1


num_tup = (10, 1, 4, 3, 6, 9, 2, 5, 7)
print(find_miss_number(num_tup))
