#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：manager_class.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/17 15:47 
"""
import student_class


# curd
class Manager:
    @staticmethod
    def all_student_object():
        students_object_list = []
        with open("students.txt", "r") as file:
            for line in file:
                this_student = student_class.Student()
                this_student.to_object(line)
                students_object_list.append(this_student)
        return students_object_list

    @staticmethod
    def write_students(students_object_list):
        with open("students.txt", "w") as file:
            for student in students_object_list:
                file.write(f'{student.to_string()}\n')

    @staticmethod
    def add_student():
        this_student = student_class.Student()
        student_id = int(input('请输入学生id：'))
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        sex = input("请输入学生性别：")
        grades = {}
        while True:
            subject = input('请输入学科名称：')
            grade = int(input(f'请输入{subject}的分数：'))
            grades[subject] = grade
            flag = int(input('是否继续添加科目成绩（1/是、0/否）:'))
            if flag == 0:
                break
        this_student.crate_student(student_id, name, age, sex, grades)
        with open("students.txt", "a") as file:
            file.write(f'{this_student.to_string()}\n')
        print(f'{this_student.to_string()} 添加成功')

    @staticmethod
    def students_cmp(student=student_class.Student()):
        return student.student_id

    @staticmethod
    def view_students(students_reverse=False):
        print('student_id\t name\t age\t sex\t grades\t')
        students_object_list = Manager.all_student_object()
        students_object_list.sort(key=Manager.students_cmp, reverse=students_reverse)
        for this_student in students_object_list:
            this_student.print_student()

    @staticmethod
    def students_sort():
        flag = int(input('请输入输出学生的顺序：（1/id从大到小、0/id从小到大）:'))
        if flag == 1:
            Manager.view_students(True)
        else:
            Manager.view_students()

    @staticmethod
    def find_student_by_id():
        flag = False
        find_id = int(input("请输入你想查询的学生id: "))
        for student in Manager.all_student_object():
            if student.student_id == find_id:
                student.print_student()
                flag = True
                break
        if not flag:
            print(f'没找到id为{find_id}的学生')

    @staticmethod
    def update_student():
        flag_update = False
        update_id = int(input("请输入你想修改的学生id: "))
        students_object_list = Manager.all_student_object()
        for student in students_object_list:
            if student.student_id == update_id:
                student.print_student()
                name = input("请输入修改后的学生姓名：")
                age = int(input("请输入修改后的学生年龄："))
                sex = input("请输入修改后的学生性别：")
                grades = {}
                while True:
                    subject = input('请输入修改后的学科名称：')
                    grade = int(input(f'请输入{subject}的分数：'))
                    grades[subject] = grade
                    flag = int(input('是否继续添加科目成绩（1/是、0/否）:'))
                    if flag == 0:
                        break
                students_object_list.remove(student)
                new_student = student_class.Student()
                new_student.crate_student(update_id, name, age, sex, grades)
                students_object_list.append(new_student)
                flag_update = True
                print(f'id为{update_id}的学生修改成功\n')
                new_student.print_student()
                break
        if not flag_update:
            print(f'没找到id为{update_id}的学生, 修改失败')
        Manager.write_students(students_object_list)

    @staticmethod
    def delete_student():
        delete_flag = False
        delete_id = int(input("请输入你想删除的学生id: "))
        students_object_list = Manager.all_student_object()
        for student in students_object_list:
            if student.student_id == delete_id:
                student.print_student()
                students_object_list.remove(student)
                delete_flag = True
                print(f'id为{delete_id}的学生删除成功\n')
                break
        if not delete_flag:
            print(f'没找到id为{delete_id}的学生，删除失败')
        Manager.write_students(students_object_list)


if __name__ == '__main__':
    mag = Manager()
    # mag.add_student()
    mag.view_students()
    # mag.students_sort()
    # mag.find_student_by_id()
    # mag.update_student()
    mag.delete_student()
