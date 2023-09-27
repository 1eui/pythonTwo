#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：countdown.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/27 15:42 
"""
import datetime

import time

local_time = time.gmtime()


def countdown():
    exam_date = datetime.date(local_time.tm_year + 1, 6, 7)
    current_date = datetime.datetime.now().date()
    remaining_days = (exam_date - current_date).days
    return remaining_days


print('=' * 30)
print(f"{local_time.tm_year + 1}年高考时间是{local_time.tm_year}年06月07日")
print(f"今天是{local_time.tm_year + 1}年{local_time.tm_mon}月{local_time.tm_mday}日")
print(f"距离{local_time.tm_year + 1}年高考还有{countdown()}天")
print('=' * 30)
