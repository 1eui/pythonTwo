#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：boss_msg_to_excel.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/11/5 16:25 
"""
import re

# -*- coding: utf-8 -*-
import xlsxwriter as xw

name_jobs = []
city_jobs = []
wake_jobs = []
url_jobs = []
with open('boss_shanghai.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    name_jobs.append(re.findall(r'岗位名称：(.*?) 岗位', line)[0])
    city_jobs.append(re.findall(r'岗位所在地：(.*?) 岗位', line)[0])
    wake_jobs.append(re.findall(r'岗位工资：(.*?) 岗位', line)[0])
    url_jobs.append(re.findall(r'岗位详情页url：(.*?)=', line)[0])
# print(len(name_jobs))
# print(name_jobs)
# print(len(city_jobs))
# print(city_jobs)
# print(len(wake_jobs))
# print(wake_jobs)
# print(len(url_jobs))
# print(url_jobs)
workbook = xw.Workbook('boss.xlsx')  # 创建工作簿
worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
worksheet1.activate()  # 激活表
title = ['岗位名称', '岗位所在地', '岗位工资', '岗位详情页url']  # 设置表头
worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
line = 2  # 从第二行开始写入数据
for i in range(len(name_jobs)):
    job_data = [name_jobs[i], city_jobs[i], wake_jobs[i], url_jobs[i]]
    row = 'A' + str(line)
    worksheet1.write_row(row, job_data)
    line += 1
workbook.close()  # 关闭表
