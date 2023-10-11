#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：pyRequest.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/6 19:01 
"""
import requests
response = requests.get("http://books.toscrape.com/")
if response.ok:
    print(response.text)
else:
    print("请求失败")

