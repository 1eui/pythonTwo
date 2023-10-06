#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：01.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/6 14:53 
"""


def split_url(url):
    dct = {'dir': url[25:40],
           'file': url[40:],
           'host': url[7:20],
           'port': url[20:25],
           'protocal': url[:4]
           }
    return dct


if __name__ == '__main__':
    url = 'http://www.skyme.org:8080/lqtest/public/index.jsp'
    print(str(split_url(url)))
