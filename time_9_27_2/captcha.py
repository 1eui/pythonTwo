#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：captcha.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/27 15:35 
"""
import random


def verify_code():
    code_list = ""
    for i in range(6):
        state = random.randint(1, 3)
        if state == 1:
            first_kind = random.randint(65, 90)
            random_uppercase = chr(first_kind)
            code_list = code_list + random_uppercase
        elif state == 2:
            second_kind = random.randint(97, 122)
            random_lowercase = chr(second_kind)
            code_list = code_list + random_lowercase
        elif state == 3:
            third_kind = random.randint(0, 9)
            code_list = code_list + str(third_kind)
    return code_list


print(verify_code())
