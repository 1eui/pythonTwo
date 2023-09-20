#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：date.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/20 14:55 
"""

split_list = ['-', '/', '.']
c = '1'
date = input("please enter the date:")

for split in split_list:
    if split in date:
      c = split

# print(date.split(c))
if c != '1':
    date_list = date.split(c)
    print(f"{date_list[0]}年{date_list[1]}月{date_list[2]}日")
else:
    print(date)
