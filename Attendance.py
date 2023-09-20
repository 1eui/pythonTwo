#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：Attendance.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/20 15:15 
"""

Attendance_s = input("Please enter the employee’s attendance status (p means normal, other means absent):")

Attendance_s = Attendance_s.upper()

# print(Attendance_s)

rate = float(Attendance_s.count('P') / len(Attendance_s))

print(f"{rate * 100}%")


