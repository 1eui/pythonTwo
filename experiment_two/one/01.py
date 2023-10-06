#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：01.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/6 13:20 
"""
lst = ['Apple', 'Orange', 1, 55, 55, 3.6, True]
print(lst.count('Orange') != 0)  # 判断是否存在'Orange'

lst.append(100)  # 在末尾追加100
print(lst)

lst.extend(['Python', 'Java'])  # 末尾添加列表['Python', 'Java']
print(lst)

lst.insert(1, 'Banana')
print(lst)

lst[2:2] = [3, 4, 5, 6]
print(lst)

lst.pop()
print(lst)

lst.remove('Apple')
print(lst)

print(lst.index(3.6))

print(lst.count(55))

lst.reverse()
print(lst)

c = lst.copy()
c.clear()
print(c)
