#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：volumes.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/6 15:15 
"""
import math


def cal_sphere(r):
    volume = 4 / 3 * math.pi * pow(r, 3)
    area = math.pi * pow(r, 2) * 4
    tup = (area, volume)
    return tup


def cal_cubid(a, b, c):
    length = (a + b + c) * 4
    area = (a * b + a * c + b * c) * 2
    volume = a * b * c
    tup = (length, area, volume)
    return tup
