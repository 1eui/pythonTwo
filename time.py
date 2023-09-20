import tkinter as tk
import time
import math


def update_clock():
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    # 计算指针的角度
    hour_angle = 360 / 12 * (hour % 12) + 360 / 12 / 60 * minute + 360 / 12 / 60 / 60 * second
    minute_angle = 360 / 60 * minute + 360 / 60 / 60 * second
    second_angle = 360 / 60 * second

    # 更新指针的位置
    canvas.delete("all")

    radius = 120  # 表盘的半径

    center_x = 150  # 表盘中心点的x坐标
    center_y = 150  # 表盘中心点的y坐标

    # 绘制表盘
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius)

    # 绘制时针
    hour_hand_length = 0.5 * radius
    hour_hand_x = center_x + hour_hand_length * math.sin(math.radians(hour_angle))
    hour_hand_y = center_y - hour_hand_length * math.cos(math.radians(hour_angle))
    canvas.create_line(center_x, center_y, hour_hand_x, hour_hand_y, width=4, fill='black')

    # 绘制分针
    minute_hand_length = 0.7 * radius
    minute_hand_x = center_x + minute_hand_length * math.sin(math.radians(minute_angle))
    minute_hand_y = center_y - minute_hand_length * math.cos(math.radians(minute_angle))
    canvas.create_line(center_x, center_y, minute_hand_x, minute_hand_y, width=3, fill='black')

    # 绘制秒针
    second_hand_length = 0.9 * radius
    second_hand_x = center_x + second_hand_length * math.sin(math.radians(second_angle))
    second_hand_y = center_y - second_hand_length * math.cos(math.radians(second_angle))
    canvas.create_line(center_x, center_y, second_hand_x, second_hand_y, width=1, fill='red')

    # 显示数字时间
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', current_time)
    time_label.config(text=time_str)

    # 每隔1秒更新一次
    canvas.after(1000, update_clock)


# 创建主窗口
root = tk.Tk()
root.title("时钟程序")

# 创建画布组件用于绘制表盘和指针
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# 创建标签组件用于显示数字时间
time_label = tk.Label(root, font=("Arial", 14))
time_label.pack(pady=10)

# 更新时钟
update_clock()

# 运行主程序
root.mainloop()

