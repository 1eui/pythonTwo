#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：04.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/11/3 21:16 
"""
from selenium.webdriver.common.by import By

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.taobao.com/')

driver.maximize_window()

time.sleep(10)

names = driver.find_elements(By.XPATH, '/html/body/div[6]/div/div/div/div/div/a/div[2]/div[1]')
# //*[@id="feedContent0"]/li[1]/a/div[2]/p
prises = driver.find_elements(By.XPATH, '/html/body/div[6]/div/div/div/div/div/a/div[3]/span')

with open('04.txt', 'w', encoding='utf-8') as f:
    for i in range(len(names)):
        f.write(f'name:{names[i].text.encode("utf-8").decode("utf-8")} price:{prises[i].text.encode("utf-8").decode("utf-8")}\n')

# for i in range(1, 10):
#     print(f"name:{names[i].text} price:{price[i]}")

time.sleep(10)
