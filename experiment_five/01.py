#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：01.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/26 11:07 
"""
import re

from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
for start_num in range(0, 100, 25):
    response = requests.get(f"https://music.douban.com/top250?start={start_num}", headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)
    images = soup.select('a.nbg > img')
    for image in images:
        print(str(image))
        image_url = re.findall(r'src="(.*?)"', str(image))
        image_name = re.findall(r'alt="(.*?)"', str(image))[0]
        image_name = str(image_name).replace(' ', '').replace('/', '-').replace('.', '')
        print(image_name)
        print(image_url[0])
        with open(f'images/{image_name}.jpg', 'wb') as image_jpg:
            image_jpg.write(requests.get(image_url[0]).content)


