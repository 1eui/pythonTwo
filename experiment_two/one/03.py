#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：03.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/6 13:43 
"""
num_str = input('请输入任意个数:')
num_lst = list(map(int, num_str.split(',')))

print(max(num_lst))
print(min(num_lst))
print(sum(num_lst))
print(len(num_lst))
print(sum(num_lst)/len(num_lst))


