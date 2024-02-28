import os

class StudentDatabase:
    def __init__(self):
        self.students = []
        self.file_path = r"C:\Users\aa\Documents\VS Code\DataBase Files\StudentDatabase.txt"

    def add_student(self):
        name = input("Enter student's name: ")
        age = input("Enter student's age: ")
        gender = input("Enter student's gender: ")
        attendance_percentage = float(input("Enter student's attendance percentage: "))
        while attendance_percentage < 0 or attendance_percentage > 100:
            print("Attendance percentage must be between 0 and 100.")
            attendance_percentage = float(input("Enter student's attendance percentage: "))

        marks_urdu = int(input("Enter student's marks in Urdu: "))
        while marks_urdu < 0 or marks_urdu > 100:
            print("Marks must be between 0 and 100.")
            marks_urdu = int(input("Enter student's marks in Urdu: "))

        marks_english = int(input("Enter student's marks in English: "))
        while marks_english < 0 or marks_english > 100:
            print("Marks must be between 0 and 100.")
            marks_english = int(input("Enter student's marks in English: "))

        marks_math = int(input("Enter student's marks in Math: "))
        while marks_math < 0 or marks_math > 100:
            print("Marks must be between 0 and 100.")
            marks_math = int(input("Enter student's marks in Math: "))

        marks_biology = int(input("Enter student's marks in Biology: "))
        while marks_biology < 0 or marks_biology > 100:
            print("Marks must be between 0 and 100.")
            marks_biology = int(input("Enter student's marks in Biology: "))

        marks_chemistry = int(input("Enter student's marks in Chemistry: "))
        while marks_chemistry < 0 or marks_chemistry > 100:
            print("Marks must be between 0 and 100.")
            marks_chemistry = int(input("Enter student's marks in Chemistry: "))

        total_marks = marks_urdu + marks_english + marks_math + marks_biology + marks_chemistry
        percentage = total_marks / 5

        student_data = {
            'name': name,
            'age': age,
            'gender': gender,
            'attendance_percentage': attendance_percentage,
            'marks_urdu': marks_urdu,
            'marks_english': marks_english,
            'marks_math': marks_math,
            'marks_biology': marks_biology,
            'marks_chemistry': marks_chemistry,
            'percentage': percentage
        }
        self.students.append(student_data)
        self.save_to_file(student_data)

        if percentage > 90:
            print("CONGRATULATIONS!! YOU GOT GOLD MEDAL...")

        print("Student added successfully.")

    def save_to_file(self, data):
        with open(self.file_path, 'a') as file:
            file.write(f"Name: {data['name']}, Age: {data['age']}, Gender: {data['gender']}, "
                       f"Attendance Percentage: {data['attendance_percentage']}%, "
                       f"Marks (Urdu): {data['marks_urdu']}, Marks (English): {data['marks_english']}, "
                       f"Marks (Math): {data['marks_math']}, Marks (Biology): {data['marks_biology']}, "
                       f"Marks (Chemistry): {data['marks_chemistry']}, "
                       f"Percentage: {data['percentage']}%\n")

    def view_data(self):
        if not self.students:
            print("No student data available.")
        else:
            print("Student Data:")
            for i, student in enumerate(self.students, start=1):
                print(f"Student {i}:")
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Gender: {student['gender']}")
                print(f"Attendance Percentage: {student['attendance_percentage']}%")
                print(f"Marks (Urdu): {student['marks_urdu']}")
                print(f"Marks (English): {student['marks_english']}")
                print(f"Marks (Math): {student['marks_math']}")
                print(f"Marks (Biology): {student['marks_biology']}")
                print(f"Marks (Chemistry): {student['marks_chemistry']}")
                print(f"Percentage: {student['percentage']}%")
                print()

    def run(self):
        while True:
            print("\n1. Add Student\n2. View Data\n3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_data()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter again.")


if __name__ == "__main__":
    student_db = StudentDatabase()
    student_db.run()
