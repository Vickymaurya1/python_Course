def multiplicationTable():
    x = int(input("Enter your number "))
    for i in range(10):
        multiply = x * (i+1)
        ans= f"{x} * {i+1} = {multiply}"
        print (ans) 
    
result = multiplicationTable()
print (result)
