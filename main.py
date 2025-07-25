
# mian.py

from student import Student
from student_manager import StudentManager

def main():
    manager = StudentManager()

    while True:
        print("\n   Student Management System    ")
        print("1. Add Student.")
        print("2. Show all Students.")
        print("3. Search student by name.")
        print("4. Delete student by name.")
        print("5. Exit.")
        
        choice = input("\n Enter your choice (1-4) : ")
        
        if choice == "1":
            name = input("Enter Name : ")
            dob = input("Enter date of birth (yyyy-mm-dd) : ")
            email = input("Enter Email id : ")
            phone = input("Enter Phone Number : ")

            try:
                student = Student(name, dob, email, phone)
                manager.add_student(student)
            except Exception as e:
                print(f"Error : {e}")

        elif choice == "2":
            manager.show_student()

        elif choice == "3":
            name = input("Enter name to search  : ")
            manager.search_by_name(name)

        elif choice == "4":
            name = input("Enter name to delete : ")
            manager.delete_student_by_name(name)

        elif choice == "5":
            print("Exit program, by by ...")
            break

        else:
            print("Invalid choice.......")

if __name__ == "__main__":
    main()