#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：filtration.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/20 15:04 
"""
txt = input("Please enter the txt you want check:")

filtration_dict = {'最': '较'}

for filtration in filtration_dict.keys():
    if filtration in txt:
       txt = txt.replace(filtration, filtration_dict[filtration])
print(txt)


