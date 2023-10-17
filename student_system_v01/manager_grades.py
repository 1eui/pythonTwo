#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：manager_grades.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/17 19:21 
"""
import student_class
import manager_class


class ManagerGrades:
    manger = manager_class.Manager()

    def add_grade_to_student(self):
        flag = False
        add_student_id = int(input("请输入你想添加成绩的学生id: "))
        students_object_list = self.manger.all_student_object()
        for student in students_object_list:
            if student.student_id == add_student_id:
                student.print_student()
                grades = {}
                while True:
                    subject = input('请输入学科名称：')
                    grade = int(input(f'请输入{subject}的分数：'))
                    grades[subject] = grade
                    flag = int(input('是否继续添加科目成绩（1/是、0/否）:'))
                    if flag == 0:
                        break
                student.add_grades(grades)
                print(f'id为{add_student_id}的学生成绩添加成功')
                student.print_student()
                flag = True
                break
        if not flag:
            print(f'未找到id为{add_student_id}的学生，添加成绩失败')
        self.manger.write_students(students_object_list)

    def add_grade_to_students(self):
        while True:
            subject = input('请输入学科名称：')
            students_object_list = self.manger.all_student_object()
            for student in students_object_list:
                grades = {}
                grade = int(input(f'请输入{student.name}同学{subject}课程的成绩：'))
                grades[subject] = grade
                student.add_grades(grades)
            self.manger.write_students(students_object_list)
            flag = int(input('是否继续添加科目成绩（1/是、0/否）:'))
            if flag == 0:
                break
        self.manger.view_students()


if __name__ == '__main__':
    mag = ManagerGrades()
    # mag.add_grade_to_student()
    mag.add_grade_to_students()



