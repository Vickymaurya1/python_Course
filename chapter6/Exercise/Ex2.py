marks = []
total = 0
passed = True

for i in range(3):
    mark  = int (input(f"Enter the marks of {i+1} subject : "))
    marks.append(mark)
    
    if(mark < 33):
        passed = False
        
    total += mark
    
percentage = (total/300) *100

if(passed and percentage >= 40):
    print("result : PASS")
else:
    print("Result : Fail")
    
    
