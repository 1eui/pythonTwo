#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：main_system.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/17 18:42 
"""
import manager_class
import manager_grades

if __name__ == "__main__":
    while True:
        print("\nStudent Management System")
        print("1. 添加学生")
        print("2. 展示所有学生")
        print("3. 查找学生")
        print("4. 删除学生")
        print("5. 修改学生")
        print("6. 对学生排序")
        print("7. 为单个学生添加成绩")
        print("8. 为所有学生添加成绩")
        print("9. 退出")

        choice = input("输入你想进行的操作(1/2/3/4/5/6/7/8/9): ")

        manger_student = manager_class.Manager()
        manger_grade = manager_grades.ManagerGrades()

        if choice == "1":
            manger_student.add_student()
        elif choice == "2":
            manger_student.view_students()
        elif choice == "3":
            manger_student.find_student_by_id()
        elif choice == "4":
            manger_student.delete_student()
        elif choice == "5":
            manger_student.update_student()
        elif choice == "6":
            manger_student.students_sort()
        elif choice == "7":
            manger_grade.add_grade_to_student()
        elif choice == "8":
            manger_grade.add_grade_to_students()
        elif choice == "9":
            print("再见!")
            break
        else:
            print("输入不合法，请重新输入！")

