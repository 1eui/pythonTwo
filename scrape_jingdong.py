#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：scrape_jingdong.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/6 19:47 
"""
from bs4 import BeautifulSoup
import requests

# 获取京东的url
response = requests.get("http://books.toscrape.com/")
print(response.status_code)
# 获取京东界面的实例对象
html = response.text
# print(html)
soup = BeautifulSoup(html, "html.parser")

all_titles = soup.findAll("h3", "a")
for title in all_titles:
    print(title.string)


# all_computers = soup.findAll("p", attrs={"class": "price_color"})
# for computer in all_computers:
#     print(computer.string)

