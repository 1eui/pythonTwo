#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：mysql.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/11/8 14:59 
"""
import re

import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='xxr52013140010',
                     database='py_mysql',
                     charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

with open('../crawler/boss_shanghai.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    name_job = (re.findall(r'岗位名称：(.*?) 岗位', line)[0])
    city_job = (re.findall(r'岗位所在地：(.*?) 岗位', line)[0])
    wake_job = (re.findall(r'岗位工资：(.*?) 岗位', line)[0])
    url_job = (re.findall(r'岗位详情页url：(.*?)=', line)[0])
    print(f"INSERT into job(name, city, wake, url) VALUES('{name_job}', '{city_job}', '{wake_job}', '{url_job}')")
    cursor.execute(f"INSERT into job(name, city, wake, url) VALUES('{name_job}', '{city_job}', "
                   f"'{wake_job}', '{url_job}')")

db.commit()

# 关闭数据库连接
db.close()

