#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：01.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/12 10:21 
"""
import os
import random
import shutil

# os.makedirs(os.path.join(os.getcwd(), "aaa/bbb/ccc"))

# os.rmdir(os.path.join(os.getcwd(), "aaa/bbb/ccc"))

# with open(os.path.join(os.getcwd(), "aaa/bbb/zzz.txt"), "w") as f:
#     pass

# with open(os.path.join(os.getcwd(), "aaa/bbb/zzz.txt"), "w") as f:
#     f.write("Hello world\n")
#     for i in range(0, 20):
#         random_num = random.randint(20, 100)
#         f.write(str(random_num) + ' ')
#
# with open(os.path.join(os.getcwd(), "aaa/bbb/zzz.txt"), "r") as f:
#     lines = f.readlines()
# lines = lines[1].strip().split(' ')
# list_num = []
# for num_lines in lines:
#     list_num.append(int(num_lines))
# lst = sorted(list_num)
# sum_lst = sum(lst)
# with open(os.path.join(os.getcwd(), "aaa/bbb/zzz.txt"), "a") as f:
#     f.write('\n')
#     for item in lst:
#         f.write(str(item) + ' ')
#     f.write('\n' + str(sum_lst))
#
# with open(os.path.join(os.getcwd(), "aaa/bbb/zzz.txt"), 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)

# shutil.copy(os.path.join(os.getcwd(), "aaa/bbb/zzz.txt"), os.path.join(os.getcwd(), "aaa/yyy.txt"))


# def print_directory_structure(directory):
#     for root, dirs, files in os.walk(directory):
#         level = root.replace(directory, '').count(os.sep)
#         indent = ' ' * 4 * level
#         print('{}{}/'.format(indent, os.path.basename(root)))
#         sub_indent = ' ' * 4 * (level + 1)
#         for file in files:
#             file_path = os.path.join(root, file)
#             file_size = os.path.getsize(file_path)
#             print('{}{} - {} bytes'.format(sub_indent, file, file_size))
#
#
# directory = os.path.join(os.getcwd(), "aaa")
# print_directory_structure(directory)


shutil.rmtree(os.path.join(os.getcwd(), "aaa"))

