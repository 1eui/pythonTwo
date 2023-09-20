#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：AncientPoetryTypography.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/20 17:05 
"""

pom = '''静夜思
[唐] 李白
床前明月光，疑是地上霜。
举头望明月，低头思故乡。
'''

print(pom)

strs = pom.split('\n')

print(strs)
print(strs[0].center(30))
print(strs[1].rjust(25))
for i in range(2, len(strs)):
    print(strs[i].center(30))

