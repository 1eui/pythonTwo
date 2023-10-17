#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：student_class.py
@IDE     ：PyCharm 
@Author  ：瑞瑞爱躺平..
@Date    ：2023/10/17 14:59 
"""


class Student:
    def __init__(self):
        self.student_id = 1
        self.name = 'the_rui'
        self.age = 18
        self.sex = 'man'
        self.grades = {}

    def add_grades(self, grade):
        self.grades.update(grade)

    def crate_student(self, student_id, name, age, sex, grades):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.sex = sex
        self.grades.update(grades)

    def to_string(self):
        return f"{self.student_id}-{self.name}-{self.age}-{self.sex}-{self.grades}"

    def to_object(self, student_string):
        student_lst = student_string.strip().split('-')
        # print(student_lst)
        self.student_id = int(student_lst[0])
        self.name = student_lst[1]
        self.age = int(student_lst[2])
        self.sex = student_lst[3]
        self.grades.update(eval(student_lst[4]))
        return self

    def print_student(self):
        print(f'{self.student_id}\t {self.name}\t {self.age}\t'
              f' {self.sex}\t {self.grades}\t')


# test
if __name__ == '__main__':
    rui = Student()
    print(rui.name)
    rui.crate_student(1, 'zhang', 19, 'woman', {'math': 90})
    rui.add_grades({'psychology': 99})
    print(rui.name)
    print(rui.grades)
    student_string = rui.to_string()
    print(rui.to_string())
    print(rui.to_object(student_string).grades)
    rui.print_student()
