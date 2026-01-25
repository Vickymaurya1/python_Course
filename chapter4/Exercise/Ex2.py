students = []

for i in range(6):
    student = input(f"Enter the marks for student {i+1}: ")
    students.append(student)
    
students.sort()
print("\nList of student")
print(students)