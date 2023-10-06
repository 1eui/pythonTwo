#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：04.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/6 13:43 
"""
s = '学习Python编程是一种乐趣。'

print(s.upper())
print(s.lower())
print(s.find('Python'))
print(s.replace('Python', '程序设计'))
print(s.startswith('学习'))
print(s.endswith('。'))
print(s.__contains__('Python'))
print(s[0])
print(s[2:8])
print(s + 'OK！')
print(s + 'OK！' * 5)
