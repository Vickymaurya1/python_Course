ans = []

def greatestOfThree():
    for i in range(3):
        a = input(f"Enter your {i+1} number: ")
        ans.append(a)

    greatest = ans[0]
    for i in range(1 , len(ans)):
        if(ans[i] > greatest):
            greatest = ans[i]
    print("Greatest of three is " , greatest)
            
greatestOfThree()
    
    

   