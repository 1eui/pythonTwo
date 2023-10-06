#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：02.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/6 13:43 
"""
import calendar

mon = int(input("输入月份数字："))
day = input("输入第几天数字：")
week = input("输入星期几数字：")

month = calendar.month_name[mon]

if day[-1] == "1":
    day += "st"
elif day[-1] == "2":
    day += "nd"
elif day[-1] == "3":
    day += "rd"
else:
    day += "th"

dct = {'1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六', '7': '日'}

print(f'{month} {day}, 星期{dct[week]}')


