#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：01bag.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/19 16:57 
"""

"""
时间复杂度：O(n2)
空间复杂度：O(V)
f[v] = w
"""

# N, V = map(int, input().split(' '))
#
# v = []
# w = []
# dp = [0 for i in range(V + 1)]
# # print(dp)
# for i in range(N):
#     a, b = map(int, input().split(' '))
#     v.append(a)
#     w.append(b)
# # dp.append[int(i) for i in input().split()]
#
#
# for i in range(N):
#     for j in range(V, v[i] - 1, -1):
#         dp[j] = max(dp[j], dp[j - v[i]] + w[i])
# print(dp[V])


"""
时间复杂度：O(n2)
空间复杂度：O(V*N)
f[n][v]
"""
N, V = map(int, input().split(' '))

v = [0]
w = [0]
dp = [[0 for i in range(V + 1)] for j in range(N + 1)]
print(dp)
for i in range(N):
    a, b = map(int, input().split(' '))
    v.append(a)
    w.append(b)
# dp.append[int(i) for i in input().split()]


for i in range(1, N + 1):
    for j in range(1, V + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= v[i]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - v[i]] + w[i])

print(dp[N][V])
