def view_teachers_data(teachers_data):
    print("Teacher's Data:")
    print("\n".join(teachers_data))
    while True:
        print("\nOptions:")
        print("1. Male and Female Teachers")
        print("2. Total Salaries")
        print("3. Back")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            num_male_teachers = sum(1 for teacher in teachers_data if 'gender: male' in teacher.lower())
            num_female_teachers = sum(1 for teacher in teachers_data if 'gender: female' in teacher.lower())
            print(f"Number of Male Teachers: {num_male_teachers}")
            print(f"Number of Female Teachers: {num_female_teachers}")
        elif choice == '2':
            total_salary = sum(float(teacher.split(',')[-1].split(':')[-1].strip()) for teacher in teachers_data)
            print(f"Total Finance (Sum of all teachers' salaries): ${total_salary:.2f}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def view_students_data(students_data):
    print("Student's Data:")
    print("\n".join(students_data))
    while True:
        print("\nOptions:")
        print("1. Male and Female Students")
        print("2. Back")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            num_male_students = sum(1 for student in students_data if 'gender: male' in student.lower())
            num_female_students = sum(1 for student in students_data if 'gender: female' in student.lower())
            print(f"Number of Male Students: {num_male_students}")
            print(f"Number of Female Students: {num_female_students}")
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def main():
    teachers_data = []
    students_data = []
    try:
        with open(r'C:\Users\aa\Documents\VS Code\DataBase Files\TeacherDatabase.txt', 'r') as file:
            teachers_data = file.readlines()
    except FileNotFoundError:
        print("Teacher's Database file not found.")
        
    try:
        with open(r'C:\Users\aa\Documents\VS Code\DataBase Files\StudentDatabase.txt', 'r') as file:
            students_data = file.readlines()
    except FileNotFoundError:
        print("Student's Database file not found.")
    
    while True:
        print("\nOptions:")
        print("1. View Teacher's Data")
        print("2. View Student's Data")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_teachers_data(teachers_data)
        elif choice == '2':
            view_students_data(students_data)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
