#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：03.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/11/1 22:48 
"""
from selenium.webdriver.common.by import By

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://book.douban.com/subject/36497587/?icn=index-latestbook-subject')

driver.maximize_window()

time.sleep(10)

comments = driver.find_elements(By.XPATH, '//*[@id="score"]/ul/li/div/p/span')
# //*[@id="score"]/ul/li[2]/div/p/span
with open('03.txt', 'w') as f:
    for comment in comments:
        f.write(f'{comment.text}\n')

time.sleep(10)
