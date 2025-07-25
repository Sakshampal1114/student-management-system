import json
import os
from student import Student

class StudentManager:
    def __init__(self, filename="data.json"):
        self.students = []
        self.filename = filename
        self.load_students_from_file()

    def add_student(self, student):
        self.students.append(student)
        self.save_students_to_file()
        print("Student added successfully.......")

    def show_student(self):
        if not self.students:
            print("No students found.....")
            return
        print("\nStudent List:")
        for idx, student in enumerate(self.students, start=1):
            print(f"\nStudent {idx}")
            print("Name:", student.name)
            print("DOB:", student.dob)
            print("Email:", student.email)
            print("Phone:", student.phone)
            print("Age:", student.age)

    def search_by_name(self, name):
        found = False
        for student in self.students:
            if student.name.lower() == name.lower():
                print("\nStudent Found:")
                print("Name:", student.name)
                print("DOB:", student.dob)
                print("Email:", student.email)
                print("Phone:", student.phone)
                print("Age:", student.age)
                found = True
                break
        if not found:
            print("Student not found......")

    def delete_student_by_name(self, name):
        found = False
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                self.save_students_to_file()
                print(f"Student '{name}' deleted successfully.")
                found = True
                break
        if not found:
            print(f"Student '{name}' not found....")

    def load_students_from_file(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                for item in data:
                    student = Student.from_dict(item)  # ✅
                    self.students.append(student)
            print("Students loaded from file.")
        except Exception as e:
            print(f"Error loading students: {e}")

    def save_students_to_file(self):
        try:
            data = [student.to_dict() for student in self.students]  # ✅
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)
            print("Students saved to file.")
        except Exception as e:
            print(f"Error saving students: {e}")
