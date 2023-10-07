def add_student(student_id, name, phone):
    with open("students.txt", "a") as file:
        file.write(f"{student_id},{name},{phone}\n")


def view_students():
    try:
        list_id = []
        with open("students.txt", "r") as file:
            for line in file:
                student_id, name, phone = line.strip().split(',')
                list_id.append(student_id)
        list_id.sort()
        with open("students.txt", "r") as file:
            print("StudentID\tName\tphone")
            print("-----------------------------")
            for line in file:
                student_id, name, phone = line.strip().split(',')
                print(f"{student_id}\t{name}\t{phone}")
    except FileNotFoundError:
        print("No student data found.")


def find_student_by_id():
    find_id = input("请输入你想查询的学生id: ")
    flag = False
    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_id, name, phone = line.strip().split(',')
                if student_id == find_id:
                    print(f"student_id:{student_id}, name:{name}, phone:{phone}")
                    flag = True
                    break
            if not flag:
                print(f"未找到ID为{find_id}学生！")
    except FileNotFoundError:
        print("No student data found.")


def update_student():
    update_id = input("请输入你想修改的学生id: ")
    try:
        with open("students.txt", 'r') as file:
            lines = file.readlines()

        with open("students.txt", 'w') as file:
            for line in lines:
                student_id, name, phone = line.strip().split(',')
                if student_id == update_id:
                    print(f"student_id:{student_id}, name:{name}, phone:{phone}")
                    # update_msg = input("请输入你想修改的信息：(1-StudentID/2-Name/3-phone)")
                    update_name = input("请输入该学生ID新的姓名：")
                    update_phone = input("请输入该学生ID新的联系方式：")
                    file.write(f"{student_id},{update_name},{update_phone}\n")
                else:
                    file.write(line)
        print(f"修改成功{update_id}")
    except FileNotFoundError:
        print("No student data found.")


def delete_student():
    delete_id = input("请输入你想删除的学生id: ")
    try:
        with open("students.txt", 'r') as file:
            lines = file.readlines()

        with open("students.txt", 'w') as file:
            for line in lines:
                student_id, name, phone = line.strip().split(',')
                if student_id == delete_id:
                    continue
                else:
                    file.write(line)
        print(f"删除成功id为{delete_id}的学生")
    except FileNotFoundError:
        print("No student data found.")


def sort_key(tup):
    return tup[0]


def sort_student(num):
    flag = True
    if num == 1:
        flag = False
    with open("students.txt", 'r') as file:
        lines = file.readlines()
    lst_students = []
    for line in lines:
        student_id, name, phone = line.strip().split(',')
        tup = (int(student_id), name, phone)
        lst_students.append(tup)
    lst_students.sort(key=sort_key, reverse=flag)
    with open('students.txt', 'w') as file:
        for tup in lst_students:
            file.write(f"{str(tup[0])},{tup[1]},{tup[2]}\n")
    view_students()


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

    if choice == "1":
        student_id = input("输入学生ID: ")
        name = input("输入学生姓名: ")
        phone = input("输入学生联系方式: ")
        add_student(student_id, name, phone)
        print("学生添加成功！")
    elif choice == "2":
        view_students()
    elif choice == "3":
        find_student_by_id()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        update_student()
    elif choice == "6":
        num = int(input("请输入排序规则，（升序/1、降序/2）"))
        sort_student(num)
    elif choice == "7":
        print("再见!")
        break
    else:
        print("输入不合法，请重新输入！")
