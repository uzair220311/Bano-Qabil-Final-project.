import os

class TeacherDatabase:
    def __init__(self):
        self.teachers = []
        self.file_path = r"C:\Users\aa\Documents\VS Code\DataBase Files\TeacherDatabase.txt"

    def add_teacher(self):
        name = input("Enter teacher's name: ")
        age = input("Enter teacher's age: ")
        gender = input("Enter teacher's gender: ")
        post = input("Enter teacher's post: ")
        salary = input("Enter teacher's salary: ")

        teacher_data = {
            'name': name,
            'age': age,
            'gender': gender,
            'post': post,
            'salary': salary
        }
        self.teachers.append(teacher_data)
        self.save_to_file(teacher_data)
        print("Teacher added successfully.")

    def save_to_file(self, data):
        with open(self.file_path, 'a') as file:
            file.write(f"Name: {data['name']}, Age: {data['age']}, Gender: {data['gender']}, Post: {data['post']}, Salary: {data['salary']}\n")

    def view_data(self):
        if not self.teachers:
            print("No teacher data available.")
        else:
            print("Teacher Data:")
            for i, teacher in enumerate(self.teachers, start=1):
                print(f"Teacher {i}:")
                print(f"Name: {teacher['name']}")
                print(f"Age: {teacher['age']}")
                print(f"Gender: {teacher['gender']}")
                print(f"Post: {teacher['post']}")
                print(f"Salary: {teacher['salary']}")
                print()

    def run(self):
        while True:
            print("\n1. Add Teacher\n2. View Data\n3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_teacher()
            elif choice == '2':
                self.view_data()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter again.")


if __name__ == "__main__":
    teacher_db = TeacherDatabase()
    teacher_db.run()
