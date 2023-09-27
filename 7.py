#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：7.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/26 14:57 
"""


def computer_info(name, cpu, *args, **kwargs):
    print(name)
    print(cpu)
    print(args)
    print(kwargs)


computer_info("华硕", "i5", "8g", "1TB+128GB", Graphic="Gtx1050ti")
