#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：06.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/6 13:43 
"""
a = {1, 2, 3, 4, 5, 6}
b = {4, 5, 6, 7, 8, 9}

print(a & b)
print(a | b)
print(a - b)
print(a ^ b)

a.add(11)
print(a)

a.update([22, 33, 44])
print(a)

a.discard(55)
print(a)

print(a.issubset([1, 2, 3]))
print(a.issuperset([1, 2, 3]))

lst = []
lst.extend(a)
lst.extend(b)
print(lst)

lst = list(set(lst))
print(lst)
