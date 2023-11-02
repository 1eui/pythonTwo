#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：02.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/26 10:32 
"""
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
try:
    for start_num in range(0, 250, 25):
        response = requests.get(f"https://music.douban.com/top250?start={start_num}", headers=headers)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        # print(soup)
        all_titles = soup.select('div.pl2 > a')
        for title in all_titles:
            music_name = title.text.strip().replace(' ', '').replace('\n', '-')
            print(music_name)
            if music_name == 'H³M-H3M' or music_name == 'E=MC²-爱的方程式':
                continue
            with open('02.txt', 'a') as f:
                f.write(f'音乐名：{music_name}\n')
except:
    pass
