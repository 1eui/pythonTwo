#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：01.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/19 11:03 
"""

import time

import requests
from bs4 import BeautifulSoup


def get_house_msg(page):
    try:
        headers = {'User-Agent':
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57'}
        response = requests.get(f'https://bj.zu.ke.com/zufang/pg{page}/#contentList', headers=headers)
        response.encoding = response.apparent_encoding
        html = response.text

        # print(html)
        soup = BeautifulSoup(html, 'html.parser')

        # print(soup)
        msgs = soup.select('div.content__list--item--main')

        # print(msgs)

        for msg in msgs:
            title = msg.select('a.twoline')[0].text.strip()
            price = msg.select('span.content__list--item-price')[0].text
            print(f'房名：{title}   价格：{price}')

        time.sleep(2)
    except:
        pass


if __name__ == '__main__':
    for page in range(1, 10):
        get_house_msg(page)
