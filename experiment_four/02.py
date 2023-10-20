#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：02.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/20 19:20 
"""

import requests
from bs4 import BeautifulSoup


url = 'https://www.fiftysounds.com/zh/copyright-free-music/trending-tracks.html'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# print(soup)

music_items = soup.find_all('div', class_='col-md-3')

for music in music_items:
    # print(music)
    music_name = music.find('h3', class_='title').text
    audio_link = music.find('a', class_='button2')['href']
    audio_link = 'https://www.fiftysounds.com/zh/copyright-free-music/'+audio_link

    audio_link = audio_link.replace('zh/copyright-free-music/song-', 'music/')
    audio_link = audio_link.replace('html', 'mp3')
    print(f'歌名: {music_name}')
    print(f'音频地址: {audio_link}')
    with open(f'music/{music_name}.mp3', 'wb') as mp:
        mp.write(requests.get(audio_link).content)

