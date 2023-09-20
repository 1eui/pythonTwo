#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：testDemo.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/9/5 23:29 
"""
import random


def play_game(player, computer):
    if player == computer:
        return "平局"
    elif (player == '石头' and computer == '剪刀') or (player == '剪刀' and computer == '布') or (
            player == '布' and computer == '石头'):
        return "你赢了"
    else:
        return "电脑赢了"


def get_computer_choice():
    choices = ['石头', '剪刀', '布']
    computer_choice = random.choice(choices)
    return computer_choice


def get_player_choice():
    player_choice = input("请出拳（石头/剪刀/布）：")
    while player_choice not in ['石头', '剪刀', '布']:
        player_choice = input("输入无效，请重新出拳（石头/剪刀/布）：")
    return player_choice


def play_round():
    player_score = 0
    computer_score = 0
    while player_score < 3 and computer_score < 3:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        result = play_game(player_choice, computer_choice)
        print("你选择了：%s，电脑选择了：%s" % (player_choice, computer_choice))
        print("结果：%s" % result)
        if result == "你赢了":
            player_score += 1
        elif result == "电脑赢了":
            computer_score += 1
        else:
            continue
    if player_score > computer_score:
        print("你赢得了游戏！")
    else:
        print("电脑赢得了游戏！")


if __name__ == "__main__":
    play_round()
