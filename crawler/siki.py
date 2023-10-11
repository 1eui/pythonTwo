#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：siki.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/11 15:11 
"""
import time

import requests
from bs4 import BeautifulSoup

urls = [f"https://www.sikiedu.com/course/explore?page={page}" for page in range(1, 27)]

print(urls)

begin = time.time()
sum_title = 0
for url in urls:
    response = requests.get(url)
    response.encoding = response.apparent_encoding

    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    titles = soup.select("a.link-dark")

    for title in titles:
        print(title.text)
        sum_title += 1
print(sum_title)
end = time.time()
print(end - begin)

