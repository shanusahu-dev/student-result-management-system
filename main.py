def add_student(students):
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    result = "Pass" if marks >= 40 else "Fail"

    students[roll] = {
        "name": name,
        "marks": marks,
        "result": result
    }
    print("Student added successfully!\n")


def view_students(students):
    if not students:
        print("No records found.\n")
        return

    for roll, data in students.items():
        print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}, Result: {data['result']}")
    print()


def search_student(students):
    roll = int(input("Enter Roll Number to search: "))
    student = students.get(roll)

    if student:
        print(f"Name: {student['name']}, Marks: {student['marks']}, Result: {student['result']}\n")
    else:
        print("Student not found.\n")


def main():
    students = {}

    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()
