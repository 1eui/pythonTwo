#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：IdiomSolitaire.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/21 10:46 
"""
import math

import time

import requests
from bs4 import BeautifulSoup


response = requests.get('http://www.hydcd.com/cy/chengyugushi.htm')
print(response.status_code)
response.encoding = response.apparent_encoding
html = response.text
soup = BeautifulSoup(html, 'html.parser')

a_words = soup.findAll('a')

book = []

for word in a_words:
    if len(word.text) == 4:
        book.append(word.text)
book = book[10:-10]
print(len(book))
begin = input("请输入词语：")
while True:
    if len(begin) != 4:
        begin = input("这不是一个四字成语，请重新输入：")
    if len(begin) == 4:
        break
while True:
    header = begin[3]
    next_word = begin
    for word in book:
        if header == word[0] and next_word != word:
            next_word = word
            break
    if next_word == begin:
        print("you win")
        break
    else:
        print(next_word)

    begin_time = time.time()
    next_begin = input(f"请在十秒内输入{next_word[3]}开头的成语：")
    end_time = time.time()

    if end_time - begin_time >= 10 or next_begin[0] != next_word[3] or len(next_begin) != 4:
        print("you lose!")
        break
    else:
        begin = next_begin

# while True:
#     end_time = time.time()
#     print(math.ceil(5 - (end_time - begin_time)))
#     if end_time - begin_time >= 5:
#         print("You lose")
#         break
#     time.sleep(1)


