#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：main_system.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/17 18:42 
"""
import manager_class

if __name__ == "__main__":
    while True:
        print("\nStudent Management System")
        print("1. 添加学生")
        print("2. 展示所有学生")
        print("3. 查找学生")
        print("4. 删除学生")
        print("5. 修改学生")
        print("6. 对学生排序")
        print("7. 退出")

        choice = input("输入你想进行的操作(1/2/3/4/5/6/7): ")

        manger = manager_class.Manager()

        if choice == "1":
            manger.add_student()
        elif choice == "2":
            manger.view_students()
        elif choice == "3":
            manger.find_student_by_id()
        elif choice == "4":
            manger.delete_student()
        elif choice == "5":
            manger.update_student()
        elif choice == "6":
            manger.students_sort()
        elif choice == "7":
            print("再见!")
            break
        else:
            print("输入不合法，请重新输入！")

