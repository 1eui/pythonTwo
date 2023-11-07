#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：boss_v02.py
@IDE     ：PyCharm
@Author  ：瑞瑞爱躺平..
@Date    ：2023/11/3 22:16
"""
import datetime

from selenium.webdriver.chrome.options import Options

import time


from selenium import webdriver
from selenium.webdriver.common.by import By


def get_job_name(url):
    opt = Options()
    opt.add_experimental_option('excludeSwitches', ['enable-automation'])

    driver = webdriver.Chrome(options=opt)
    driver.get(url)
    driver.maximize_window()
    time.sleep(15)
    name_jobs = driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li/div/a/div['
                                               '1]/span[1]')
    city_jobs = driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li/div/a/div['
                                               '1]/span[2]')
    url_jobs = driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li/div/a')
    url_wakes = driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li/div[1]/a/div['
                                               '2]/span[1]')
    # //*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li[16]/div[1]/a/div[2]/span[1]

    # //*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]/div[1]/a/div[1]/span[1]
    # //*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li[1]/div[1]/a/div[1]/span[1]
    # //*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li[1]/div[1]/a/div[1]/span[1]
    # //*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li[1]/div[1]/a/div[1]/span[1]

    print(f'{len(name_jobs)} {len(city_jobs)} {len(url_jobs)} {len(url_wakes)}')

    for i in range(len(name_jobs)):
        print(f'岗位名称：{name_jobs[i].text} 岗位所在地：{city_jobs[i].text} '
              f'岗位工资：{url_wakes[i].text} 岗位详情页url：{url_jobs[i].get_attribute("href")}\n')
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    # workbook = xw.Workbook('boss.xlsx')  # 创建工作簿
    # worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    # worksheet1.activate()  # 激活表
    # title = ['岗位名称', '岗位所在地', '岗位工资', '岗位详情页url']  # 设置表头
    # worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    # for i in range(len(name_jobs)):
    #     job_data = [name_jobs[i].text, city_jobs[i].text, url_wakes[i].text, url_jobs[i].get_attribute("href")]
    #     row = 'A' + str(line)
    #     worksheet1.write_row(row, job_data)
    #     line += 1
    # workbook.close()  # 关闭表

    with open('boss_guangzhou.txt', 'a', encoding='utf-8') as f:
        for i in range(len(name_jobs)):
            f.write(f'岗位名称：{name_jobs[i].text} 岗位所在地：{city_jobs[i].text} '
                    f'岗位工资：{url_wakes[i].text} 岗位详情页url：{url_jobs[i].get_attribute("href")}\n')
    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    jobs = [100103, 100109]  # java c++ php python
    for job in jobs:
        for page in range(2, 11):
            get_job_name(f"https://www.zhipin.com/web/geek/job?city=101280100&position={job}&page={page}")
            time.sleep(900)
