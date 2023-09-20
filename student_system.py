# Function to add a new student to the system
def add_student(student_id, name, grade):
    with open("students.txt", "a") as file:
        file.write(f"{student_id},{name},{grade}\n")


# Function to view all students in the system
def view_students():
    try:
        with open("students.txt", "r") as file:
            print("StudentID\tName\tGrade")
            print("-----------------------------")
            for line in file:
                student_id, name, grade = line.strip().split(',')
                print(f"{student_id}\t{name}\t{grade}")
    except FileNotFoundError:
        print("No student data found.")


# Main program loop
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        grade = input("Enter Student Grade: ")
        add_student(student_id, name, grade)
        print("Student added successfully.")
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
