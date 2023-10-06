#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：05.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/6 13:43 
"""
dct = {'cn': '中国', 'uk': '英国', 'us': '美国', 'de': '德国'}

print(dct['cn'])
print(dct.get('cn'))
dct['fr'] = '法国'
dct.pop('us')
del dct['uk']
print(dct)

print(dct.keys())
print(dct.values())
print(dct.items())
print('ca' in dct)

dct2 = {'au': '澳大利亚', 'cz': '捷克共和国'}

print(dct.update(dct2))
print(dct)
print(len(dct))