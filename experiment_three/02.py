#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：02.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/12 11:26 
"""
import math

try:
    num_int = input("请输入一个数值：")
    num_int = float(num_int)
    res = math.sqrt(num_int)
except ValueError:
    print(f"name \'{num_int}\' is not defined")
    res = None
finally:
    print(f"开平方结果为：{res}")



