marks = int(input("Enter the marks "))

if(marks >= 90 and marks <= 100):
    grade = "Ex"
elif(marks > 80 ):
    grade = "A"
else:
    grade = "F"
    
print("Your grade is : " , grade)
