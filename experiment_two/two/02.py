#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：02.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/6 15:03 
"""


def broca(tup):
    if tup[0] - 110 > tup[1] + 5:
        return "过胖"
    elif tup[0] - 110 < tup[1] - 5:
        return '过廋'
    else:
        return '标准身材'


tup = eval(input('请输入身高cm和体重kg，逗号分隔：'))
ret = broca(tup)
print(ret)
