import os
import pickle

students = []

def load_file():
    global students
    filename = input("Enter filename to open: ")
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            students = pickle.load(f)
        print("File loaded successfully.")
    else:
        print("File not found.")

def save_file():
    filename = input("Enter filename to save: ")
    with open(filename, 'wb') as f:
        pickle.dump(students, f)
    print("File saved successfully.")

def show_all():
    print("\nAll Students Record:")
    for s in students:
        print(s)
    print()

def order_by_last_name():
    sorted_students = sorted(students, key=lambda x: x[1][1])
    print("\nStudents Ordered by Last Name:")
    for s in sorted_students:
        print(s)
    print()

def order_by_grade():
    sorted_students = sorted(students, key=lambda x: (0.6 * x[2] + 0.4 * x[3]), reverse=True)
    print("\nStudents Ordered by Grade:")
    for s in sorted_students:
        print(s)
    print()

def show_student():
    student_id = input("Enter Student ID: ")
    for s in students:
        if s[0] == student_id:
            print("\nStudent Record:")
            print(s)
            return
    print("Student not found.")

def add_record():
    student_id = input("Enter Student ID (6 digits): ")
    if len(student_id) != 6 or not student_id.isdigit():
        print("Invalid ID. Must be a 6-digit number.")
        return
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    exam_grade = float(input("Enter Major Exam Grade: "))
    students.append((student_id, (first_name, last_name), class_standing, exam_grade))
    print("Record added successfully.")

def edit_record():
    student_id = input("Enter Student ID to edit: ")
    for i, s in enumerate(students):
        if s[0] == student_id:
            first_name = input("Enter New First Name: ")
            last_name = input("Enter New Last Name: ")
            class_standing = float(input("Enter New Class Standing Grade: "))
            exam_grade = float(input("Enter New Major Exam Grade: "))
            students[i] = (student_id, (first_name, last_name), class_standing, exam_grade)
            print("Record updated successfully.")
            return
    print("Student not found.")

def delete_record():
    student_id = input("Enter Student ID to delete: ")
    for i, s in enumerate(students):
        if s[0] == student_id:
            del students[i]
            print("Record deleted successfully.")
            return
    print("Student not found.")

def main():
    while True:
        print("\nSTUDENT RECORD MANAGEMENT")
        print("1. Open File")
        print("2. Save File")
        print("3. Show All Students Record")
        print("4. Order by Last Name")
        print("5. Order by Grade")
        print("6. Show Student Record")
        print("7. Add Record")
        print("8. Edit Record")
        print("9. Delete Record")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            load_file()
        elif choice == '2':
            save_file()
        elif choice == '3':
            show_all()
        elif choice == '4':
            order_by_last_name()
        elif choice == '5':
            order_by_grade()
        elif choice == '6':
            show_student()
        elif choice == '7':
            add_record()
        elif choice == '8':
            edit_record()
        elif choice == '9':
            delete_record()
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
